from PySide6 import QtGui
from PySide6 import QtWidgets

class ManupulatorsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ManupulatorsWidget, self).__init__(parent)
        # layouts
        self.main_layout = QtWidgets.QVBoxLayout()
        self.manipulators_layout = QtWidgets.QHBoxLayout()
        self.search_layout = QtWidgets.QHBoxLayout()

        self.search_line_edit = QtWidgets.QLineEdit()
        self.search_label = QtWidgets.QLabel()
        self.search_label.setText('search field: ')
        self.search_line_edit.setToolTip('type name or regexp')

        self.list_view = QtWidgets.QListView()
        self.back_button = QtWidgets.QPushButton()
        self.back_button.setText('go back')

        # sliders
        self.clamp_max_manipulator = QtWidgets.QSlider(QtGui.Qt.Vertical)
        self.clamp_min_manipulator = QtWidgets.QSlider(QtGui.Qt.Vertical)
        self.offset_manipulator = QtWidgets.QSlider(QtGui.Qt.Vertical)
        self.scale_factor_manipulator = QtWidgets.QSlider(QtGui.Qt.Vertical)
        # add search widgets to layout
        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_line_edit)



        # add sliders to layout
        self.manipulators_layout.addWidget(self.clamp_max_manipulator)
        self.manipulators_layout.addWidget(self.clamp_min_manipulator)
        self.manipulators_layout.addWidget(self.offset_manipulator)
        self.manipulators_layout.addWidget(self.scale_factor_manipulator)

        # add layouts to each other
        self.main_layout.addLayout(self.search_layout)
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addLayout(self.manipulators_layout)
        self.main_layout.addWidget(self.back_button)
        self.setLayout(self.main_layout)




if __name__=='__main__':
    app = QtWidgets.QApplication([])
    wgt = ManupulatorsWidget()
    wgt.show()
    app.exec()

