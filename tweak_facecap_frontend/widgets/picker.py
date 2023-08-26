from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
import os


class Picker(QtWidgets.QLabel):
    kTopSelected = 4278190335
    kMidSelected = 4281007872
    kBottomSelected = 4294901760
    area_clicked = QtCore.Signal(object)

    def __init__(self, parent=None):
        super(Picker, self).__init__(parent)
        self.default_pixmap = QtGui.QPixmap(
            os.path.join(os.environ["FACECAP_TWEAK_RESOURCES"], "woman_face_beauty.png")
        )
        self.highlight_top = QtGui.QPixmap(
            os.path.join(os.environ["FACECAP_TWEAK_RESOURCES"], "highlight_top.png")
        )
        self.highlight_mid = QtGui.QPixmap(
            os.path.join(os.environ["FACECAP_TWEAK_RESOURCES"], "highlight_mid.png")
        )
        self.highlight_bottom = QtGui.QPixmap(
            os.path.join(os.environ["FACECAP_TWEAK_RESOURCES"], "highlight_bottom.png")
        )
        self.matte_pixmap = QtGui.QImage(
            os.path.join(os.environ["FACECAP_TWEAK_RESOURCES"], "puzzle_matte.png")
        )
        self.setPixmap(self.default_pixmap)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, ev):
        self.clr = self.matte_pixmap.pixel(ev.pos())
        if self.clr == 4278190335:
            self.setPixmap(self.highlight_top)
        elif self.clr == 4281007872:
            self.setPixmap(self.highlight_mid)
        elif self.clr == 4294901760:
            self.setPixmap(self.highlight_bottom)
        else:
            self.setPixmap(self.default_pixmap)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.area_clicked.emit(self.clr)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    wgt = Picker()
    wgt.show()
    app.exec()
