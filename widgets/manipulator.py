# coding=utf-8
# TODO попробовать унифицировать данные и Model сейчас они работают отдельно

from PySide6 import QtGui
from PySide6 import QtWidgets
from .controls_data_model import ControlsDataModel
from .controls_data_view import ControlsDataView
from .sliders_pane import SlidersPane


class Manipulator(QtWidgets.QWidget):
    def __init__(self, osc_client, config_data=None, parent=None):
        super(Manipulator, self).__init__(parent)
        self.config_data = config_data or {}
        self.osc_client = osc_client

        self.current_item = None  # currently selected item

        # layouts
        self.main_layout = QtWidgets.QVBoxLayout()
        self.manipulators_layout = QtWidgets.QHBoxLayout()
        self.search_layout = QtWidgets.QHBoxLayout()

        self.search_line_edit = QtWidgets.QLineEdit()
        self.search_label = QtWidgets.QLabel()
        self.search_label.setText("search (text or regexp): ")

        self.search_line_edit.setToolTip("type name or regexp")
        self.item_name_label = QtWidgets.QLabel(
            self.current_item or "item is not selected"
        )

        self.list_view = ControlsDataView()
        # add model
        self.data_model = ControlsDataModel(list(self.config_data.keys()))
        # set model to view
        self.list_view.setModel(self.data_model)

        self.back_button = QtWidgets.QPushButton()
        self.back_button.setText("go back")

        # sliders
        self.sliders_pane = SlidersPane(self.osc_client)

        # self.clamp_max_slider = QtWidgets.QSlider(QtGui.Qt.Vertical)
        #         # self.clamp_min_slider = QtWidgets.QSlider(QtGui.Qt.Vertical)
        #         # self.offset_slider = QtWidgets.QSlider(QtGui.Qt.Vertical)
        #         # self.scale_factor_slider = QtWidgets.QSlider(QtGui.Qt.Vertical)
        #         # add search widgets to layout
        #         # self.search_layout.addWidget(self.search_label)
        #         # self.search_layout.addWidget(self.search_line_edit)
        #
        #         # add sliders to layout
        #         # self.manipulators_layout.addWidget(self.clamp_max_slider)
        #         # self.manipulators_layout.addWidget(self.clamp_min_slider)
        #         # self.manipulators_layout.addWidget(self.offset_slider)
        #         # self.manipulators_layout.addWidget(self.scale_factor_slider)

        # add layouts to each other
        self.main_layout.addLayout(self.search_layout)
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addWidget(self.item_name_label)

        self.main_layout.addWidget(self.sliders_pane)
        self.main_layout.addWidget(self.back_button)
        self.setLayout(self.main_layout)

        # connections
        # TODO temp solution
        self.list_view.item_changed.connect(self.on_list_view_item_changed)

    def set_config_data(self, config_data):
        self.config_data = config_data
        # update all views with new data
        self.data_model.items = list(self.config_data.keys())
        self.data_model.layoutChanged.emit()
        # update controllers
        self.sliders_pane.reset()

    def get_config_data(self):
        return self.config_data


    def on_list_view_item_changed(self, item):
        self.item_name_label.setText(item)
        self.sliders_pane.set_data(self.config_data[item])

    # def on_list_view_item_changed(self, item):
    #     self.current_item = item
    #     self.item_name_label.setText(item)
    #     print(self._config_data[item])
    #     self.update_slider_values()
    #
    # def update_slider_values(self):
    #     """
    #     this updates slider values with config values for current item
    #     :param item:
    #     :type item:
    #     :return:
    #     :rtype:
    #     """
    #     if not self.current_item:
    #         return
    #     self.clamp_max_slider.setValue(self._config_data[self.current_item]['Clamp Max'])
    #     self.clamp_min_slider.setValue(self._config_data[self.current_item]['Clamp Min'])
    #     self.offset_slider.setValue(self._config_data[self.current_item]['Offset'])
    #     self.scale_factor_slider.setValue(self._config_data[self.current_item]['Scale Factor'])
    #
    #
    # def update_config_value(self, slider_name, value):
    #     if self.current_item is None:
    #         return
    #     self._config_data[self.current_item][slider_name] = value
    #
    # def on_clamp_max_slider_value_changed(self):
    #     self.update_config_value('Clamp Max', self.clamp_max_slider.value())
    #
    # def on_clamp_min_slider_value_changed(self):
    #     self.update_config_value('Clamp Min', self.clamp_min_slider.value())
    #
    # def on_offset_slider_value_changed(self):
    #     self.update_config_value('Offset', self.offset_slider.value())
    #
    # def on_scale_factor_slider_changed(self):
    #     self.update_config_value('Scale Factor', self.scale_factor_slider.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    wgt = Manipulator()
    wgt.show()
    app.exec()
