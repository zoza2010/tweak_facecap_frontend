# coding=utf-8
from .ui.stream_pane import Ui_Form
from PySide6 import QtWidgets
from PySide6 import QtCore
import tempfile


class StreamPane(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(StreamPane, self).__init__(parent)
        self.setupUi(self)
        self.ipAdressLineEdit.setText("127.0.0.1")
        self.portLineEdit.setText("9001")
        self.enableStreamCheckBox.setChecked(True)
