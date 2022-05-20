from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets


class ControlsDataModel(QtCore.QAbstractListModel):
    def __init__(self, data):
        super(ControlsDataModel, self).__init__()
        self.items = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            text = self.items[index.row()]
            return text


    def rowCount(self, index):
        return len(self.items)