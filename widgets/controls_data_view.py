from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets

"""
temp solution for extracting data from list view
"""

class ControlsDataView(QtWidgets.QListView):
    item_changed = QtCore.Signal(object)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        result = super(ControlsDataView, self).mousePressEvent(event)
        indexes = self.selectedIndexes()
        assert len(indexes) < 2
        self.item_changed.emit(self.model().data(indexes[0], QtCore.Qt.DisplayRole))
        return result