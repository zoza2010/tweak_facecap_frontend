from pythonosc import udp_client
from PySide6 import QtCore
import logging

logger = logging.getLogger(__name__)


class OSCDataMapper(object):
    """
    maps model data to osc command
    """

    def __init__(self, parent):
        self.parent = parent

    def setParent(self, parent):
        self.parent = parent

    def _converter(self, top_left: QtCore.QModelIndex, bottom_right, roles):

        if (1 <= top_left.column() < self.parent.model.columnCount() - 1
        ):
            anim_channel_id_relative = top_left.column() - 1
            blend_shape_id = self.parent.model.configData()[top_left.row()][-1]
            anim_channel_id_absolute = (
                blend_shape_id - 1
            ) * 4 + anim_channel_id_relative
            channel_value = float(top_left.data(QtCore.Qt.DisplayRole))

            if top_left.column() == 4:
                channel_value *= 0.01

            return "/E", (anim_channel_id_absolute, channel_value)

    def map_to_commad(self, top_left: QtCore.QModelIndex, bottom_right, roles) -> any:
        return self._converter(top_left, bottom_right, roles)


class OSCClient(object):
    def __init__(self, ip="127.0.0.1", port=9001):
        self.model = None
        self.paused = False
        self._ip = ip
        self._port = port
        self._setup_client()
        self._mapper = OSCDataMapper(self)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        logger.debug(f'changing ip to: "{value}"')
        self._ip = value
        self._setup_client()

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        logger.debug(f'changing port to: "{value}"')
        self._port = value
        self._setup_client()

    def setModel(self, model: QtCore.QAbstractItemModel):
        self.model = model
        self.model.dataChanged.connect(self._on_item_changed)
        self.model.all_data_changed.connect(self._on_all_data_changed)

    def setMapper(self, mapper):
        mapper.setParent(self)
        self._mapper = mapper

    def _send_message(self, *args):
        if not self.paused:
            logger.debug(f"streaming: {args}")
            self._client.send_message(*args)

    def _setup_client(self):
        self._client = udp_client.SimpleUDPClient(self.ip, int(self.port))

    def _on_all_data_changed(self):
        logger.debug("OSC sending all data")

        for i in range(self.model.rowCount()):
            for j in range(self.model.columnCount()):

                index = self.model.index(i, j)
                command = self._mapper.map_to_commad(index, index, [])
                if command:
                    self._send_message(*command)

    def _on_item_changed(
        self, top_left: QtCore.QModelIndex, bottom_right: QtCore.QModelIndex, roles
    ):
        command = self._mapper.map_to_commad(top_left, bottom_right, roles)
        if command:
            self._send_message(*command)
