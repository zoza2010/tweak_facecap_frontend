from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from .picker import Picker
from .manipulator import Manipulator


class FacecapTweak(QtWidgets.QWidget):
    def __init__(self, osc_client, parent=None):
        """
        :param config_data:
        :type config_data:
        :param parent:
        :type parent:
        """
        super(FacecapTweak, self).__init__(parent)
        self.osc_client = osc_client
        self.setMouseTracking(True)
        self.picker = Picker()
        self.manipulators_widget = Manipulator(self.osc_client)
        self.manipulators_widget.setVisible(False)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.picker)
        self.main_layout.addWidget(self.manipulators_widget)
        self.setLayout(self.main_layout)
        self.picker.area_clicked.connect(self.on_area_clicked)
        self.manipulators_widget.back_button.clicked.connect(self._switch_widgets)

        # TODO temp solution
        self.setFixedWidth(500)
        self.setFixedHeight(700)

    def set_config_data(self, config_data):
        self.manipulators_widget.set_config_data(config_data)

    def get_config_data(self):
        print(self.manipulators_widget.get_config_data().get('browDown_L'))
        return self.manipulators_widget.get_config_data()



    def _switch_widgets(self):
        self.picker.setVisible(not self.picker.isVisible())
        self.manipulators_widget.setVisible(not self.manipulators_widget.isVisible())

    def on_area_clicked(self, clr):
        if clr == Picker.kTopSelected:
            self._switch_widgets()
        elif clr == Picker.kMidSelected:
            self._switch_widgets()
        elif clr == Picker.kBottomSelected:
            self._switch_widgets()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        self.picker.mouseMoveEvent(event)
