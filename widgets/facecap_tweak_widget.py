from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from .picker import Picker
from .editor_view import EditorView


class FacecapTweak(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        :param config_data:
        :type config_data:
        :param parent:
        :type parent:
        """
        super(FacecapTweak, self).__init__(parent)
        self.setMouseTracking(True)
        self.picker = Picker()
        self.editor = EditorView()
        self.editor.setVisible(True)
        self.picker.setVisible(False)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.picker)

        self.main_layout.addWidget(self.editor)
        self.setLayout(self.main_layout)
        self.picker.area_clicked.connect(self.on_area_clicked)
        # self.editor.goBackPushButton.clicked.connect(self._switch_widgets)

    def setModel(self, model):
        self.editor.setModel(model)

    def _switch_widgets(self):
        self.picker.setVisible(not self.picker.isVisible())
        self.editor.setVisible(not self.editor.isVisible())

    def on_area_clicked(self, clr):
        if clr == Picker.kTopSelected:
            self._switch_widgets()
        elif clr == Picker.kMidSelected:
            self._switch_widgets()
        elif clr == Picker.kBottomSelected:
            self._switch_widgets()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        self.picker.mouseMoveEvent(event)
