from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets


class ConfigModel(QtCore.QAbstractTableModel):
    all_data_changed = QtCore.Signal()

    def __init__(self, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._config_data = dict()

    def configData(self):
        return self._config_data

    def setConfigData(self, data):
        self.beginResetModel()
        self._config_data = data
        self.endResetModel()
        self.all_data_changed.emit()

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return [
                    "blendshape name",
                    "clamp min",
                    "clamp max",
                    "offset",
                    "scale",
                    "index",
                ][section]

    def columnCount(self, parent=QtCore.QModelIndex()):
        if not self._config_data:
            return
        return len(self._config_data[0])

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._config_data)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        row = index.row()
        col = index.column()

        if role == QtCore.Qt.EditRole:
            return self._config_data[row][col]
        elif role == QtCore.Qt.DisplayRole:
            return self._config_data[row][col]

    def flags(self, index):
        flags = super(ConfigModel, self).flags(index)

        if index.isValid():
            flags |= QtCore.Qt.ItemIsEditable
            flags |= QtCore.Qt.ItemIsDragEnabled
        else:
            flags = QtCore.Qt.ItemIsDropEnabled

        return flags

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid() or role != QtCore.Qt.EditRole:
            return False

        self._config_data[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True
