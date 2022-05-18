from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from picker import Picker
from manipulators_widget import ManupulatorsWidget




class TweakFacecapWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TweakFacecapWidget, self).__init__(parent)
        self.setMouseTracking(True)
        self.picker = Picker()
        self.manipulators_widget = ManupulatorsWidget()
        self.manipulators_widget.setVisible(False)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.picker)
        self.main_layout.addWidget(self.manipulators_widget)
        self.setLayout(self.main_layout)
        self.picker.area_clicked.connect(self.on_area_clicked)
        self.manipulators_widget.back_button.clicked.connect(self.switch_widgets)
        # TODO temp solution
        self.setFixedWidth(500)
        self.setFixedHeight(700)

    def switch_widgets(self):
        self.picker.setVisible(not self.picker.isVisible())
        self.manipulators_widget.setVisible(not self.manipulators_widget.isVisible())


    def on_area_clicked(self, clr):
        if clr ==  Picker.kTopSelected:
            self.switch_widgets()
        elif clr== Picker.kMidSelected:
            self.switch_widgets()
        elif clr == Picker.kBottomSelected:
            self.switch_widgets()


    def mouseMoveEvent(self, event:QtGui.QMouseEvent) -> None:
        self.picker.mouseMoveEvent(event)

if __name__=='__main__':
    app = QtWidgets.QApplication([])
    app.setStyleSheet(open(r'.\resources\Darkeum.qss').read())
    wgt = TweakFacecapWidget()
    wgt.show()
    app.exec()