import json
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from widgets.facecap_tweak_widget import FacecapTweak
from widgets.stream_pane import StreamPane
from copy import deepcopy
from osc_client import OSCClient
from config_model import ConfigModel
import os
import logging

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)


class FacecapTweakMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FacecapTweakMainWindow, self).__init__(
            parent, QtCore.Qt.WindowStaysOnTopHint
        )
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_widget = QtWidgets.QWidget(self)
        self._default_config = self.read_config(
            os.path.join(os.environ["FACECAP_TWEAK_ROOT"], "default_config.json")
        )
        self.osc_client = OSCClient()
        self.stream_pane = StreamPane(self)

        self.facecap_tweak_widget = FacecapTweak(self)
        self.config_model = ConfigModel()

        self.main_layout.addWidget(self.stream_pane)
        self.main_layout.addWidget(self.facecap_tweak_widget)
        self.set_model(self.config_model)
        self.config_model.setConfigData(self.default_config)

        # Creating menus
        self.create_menu()

        # bindings
        self.stream_pane.enableStreamCheckBox.stateChanged.connect(
            self._onEnableStreamCheckBoxStateChanged
        )
        self.stream_pane.ipAdressLineEdit.editingFinished.connect(
            self._onIpAdressLineEditEditingFinished
        )
        self.stream_pane.portLineEdit.editingFinished.connect(
            self._onPortLineEditEditingFinished
        )

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def _onPortLineEditEditingFinished(self):
        text = self.stream_pane.portLineEdit.text()
        self.osc_client.port = text

    def _onIpAdressLineEditEditingFinished(self):
        text = self.stream_pane.ipAdressLineEdit.text()
        self.osc_client.ip = text

    def _onEnableStreamCheckBoxStateChanged(self):
        state = self.stream_pane.enableStreamCheckBox.isChecked()
        self.osc_client.paused = not state

    def set_model(self, model):
        self.osc_client.setModel(model)
        self.facecap_tweak_widget.setModel(model)

    @property
    def default_config(self):
        return deepcopy(self._default_config)

    def create_menu(self):
        main_menu = self.menuBar()
        fileMenu = main_menu.addMenu("File")

        newAction = QtGui.QAction("New", self)
        newAction.setShortcut("Ctrl+N")
        fileMenu.addAction(newAction)
        newAction.triggered.connect(self.on_file_new)

        openAction = QtGui.QAction("Open", self)
        openAction.setShortcut("Ctrl+N")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.on_file_open)

        fileMenu.addSeparator()

        saveAsAction = QtGui.QAction("SaveAs", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        fileMenu.addAction(saveAsAction)
        saveAsAction.triggered.connect(self.on_file_save_as)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options,
        )
        if fileName:
            return fileName

    def saveAsFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            "",
            "All Files (*);;Text Files (*.json)",
            options=options,
        )
        if fileName:
            return fileName

    def on_file_new(self):
        self.config_model.setConfigData(self.default_config)

    def on_file_open(self):
        file_name = self.openFileNameDialog()
        if not file_name:
            return
        self.config_model.setConfigData(self.read_config(file_name))

    def on_file_save_as(self):
        file_name = self.saveAsFileDialog()
        if not file_name:
            return
        self.write_config(file_name)

    def read_config(self, path):
        logger.debug(f'reading config from: "{path}"')
        with open(path, "r") as f:
            config_object = json.load(f)
            data = []
            for key, values in config_object.items():
                attr_values = list(values.values())
                attr_values.insert(0, key)
                data.append(attr_values)
            return data

    def write_config(self, path):
        logger.error(f'writing config to: "{path}"')
        # back serialize
        config_data = self.config_model.configData()
        to_save = dict()
        for i in config_data:
            to_save[i[0]] = {
                "Clamp Max": i[1],
                "Clamp Min": i[2],
                "Offset": i[3],
                "Scale Factor": i[4],
                "index": [5],
            }
        with open(path, "w") as f:
            f.write(json.dumps(to_save, indent=4))


if __name__ == "__main__":
    os.environ["FACECAP_TWEAK_ROOT"] = os.path.join(os.path.dirname(__file__))

    os.environ["FACECAP_TWEAK_RESOURCES"] = os.path.join(
        os.environ["FACECAP_TWEAK_ROOT"], "resources"
    )
    app = QtWidgets.QApplication([])
    app.setStyleSheet(
        open(os.path.join(os.environ["FACECAP_TWEAK_RESOURCES"], "Darkeum.qss")).read()
    )
    wgt = FacecapTweakMainWindow()
    wgt.show()
    app.exec()
