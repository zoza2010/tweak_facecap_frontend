from .primitives.slidersWidget import Ui_Form
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets


class SlidersPane(QtWidgets.QWidget):
    clamp_max_changed = QtCore.Signal(float)
    clamp_min_changed = QtCore.Signal(float)
    offset_changed = QtCore.Signal(float)
    scale_changed = QtCore.Signal(float)

    def __init__(self, osc_client, parent=None):
        super(SlidersPane, self).__init__(parent)
        # by default all sliders will be set to 0
        self.config_data_block = dict()
        self.osc_client = osc_client

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.int_validator = QtGui.QDoubleValidator(self)

        self.ui.clampMaxLineEdit.setValidator(self.int_validator)
        self.ui.clampMinLineEdit.setValidator(self.int_validator)
        self.ui.offsetLineEdit.setValidator(self.int_validator)
        self.ui.scaleLineEdit.setValidator(self.int_validator)

        # default line edit fill with sliders values
        self.ui.clampMaxLineEdit.setText(str(self.ui.clampMaxSlider.value()))
        self.ui.clampMinLineEdit.setText(str(self.ui.clampMinSlider.value()))
        self.ui.offsetLineEdit.setText(str(self.ui.offsetSlider.value()))
        self.ui.scaleLineEdit.setText(str(self.ui.scaleSlider.value()))

        # connections
        # line edit fields to sliders
        self.ui.clampMaxLineEdit.editingFinished.connect(
            lambda: self.ui.clampMaxSlider.setValue(
                float(self.ui.clampMaxLineEdit.text())
            )
        )
        self.ui.clampMinLineEdit.editingFinished.connect(
            lambda: self.ui.clampMinSlider.setValue(
                float(self.ui.clampMinLineEdit.text())
            )
        )
        self.ui.offsetLineEdit.editingFinished.connect(
            lambda: self.ui.offsetSlider.setValue(float(self.ui.offsetLineEdit.text()))
        )
        self.ui.scaleLineEdit.editingFinished.connect(
            lambda: self.ui.scaleSlider.setValue(float(self.ui.scaleLineEdit.text()))
        )

        # sliders to edit fields
        self.ui.clampMaxSlider.valueChanged.connect(self.onClampMaxSliderValueChanged)
        self.ui.clampMinSlider.valueChanged.connect(self.onClampMinSliderValueChanged)
        self.ui.offsetSlider.valueChanged.connect(self.onOffsetSliderValueChanged)
        self.ui.scaleSlider.valueChanged.connect(self.onScaleSliderValueChanged)

    def set_data_block_values(self, setting, value):
        if self.config_data_block:
            self.config_data_block[setting] = int(value)


    # TEMP SOLUTIONS
    def onClampMaxSliderValueChanged(self):
        self.ui.clampMaxLineEdit.setText(str(self.ui.clampMaxSlider.value()))
        self.set_data_block_values("Clamp Max", self.ui.clampMaxSlider.value())
        if self.config_data_block:
            self.osc_client.send_message(((self.config_data_block['index'] - 1 )* 4) + 2, self.ui.clampMaxSlider.value())

    def onClampMinSliderValueChanged(self):
        self.ui.clampMinLineEdit.setText(str(self.ui.clampMinSlider.value()))
        self.set_data_block_values("Clamp Min", self.ui.clampMinSlider.value())
        if self.config_data_block:
            self.osc_client.send_message(((self.config_data_block['index'] - 1) * 4) + 1, self.ui.clampMinSlider.value())

    def onOffsetSliderValueChanged(self):
        self.ui.offsetLineEdit.setText(str(self.ui.offsetSlider.value()))
        self.set_data_block_values("Offset", self.ui.offsetSlider.value())
        if self.config_data_block:
            self.osc_client.send_message(((self.config_data_block['index'] - 1) * 4) + 3,
                                         self.ui.offsetSlider.value())


    def onScaleSliderValueChanged(self):
        self.ui.scaleLineEdit.setText(str(self.ui.scaleSlider.value()))
        self.set_data_block_values("Scale Factor", self.ui.scaleSlider.value())
        if self.config_data_block:
            self.osc_client.send_message(((self.config_data_block['index'] - 1) * 4) + 4,
                                         self.ui.scaleSlider.value() * 0.01)

    def reset(self):
        self.config_data_block = dict()
        self.ui.clampMaxSlider.setValue(0)
        self.ui.clampMinSlider.setValue(0)
        self.ui.offsetSlider.setValue(0)
        self.ui.scaleSlider.setValue(0)

    def set_data(self, data):
        self.config_data_block = data
        self.ui.clampMaxSlider.setValue(float(self.config_data_block.get("Clamp Max", 0)))
        self.ui.clampMinSlider.setValue(float(self.config_data_block.get("Clamp Min", 0)))
        self.ui.offsetSlider.setValue(float(self.config_data_block.get("Offset", 0)))
        self.ui.scaleSlider.setValue(float(self.config_data_block.get("Scale Factor", 0)))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    wgt = SlidersPane()
    wgt.show()
    app.exec()
