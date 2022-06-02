# coding=utf-8
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from .ui.editor_view import Ui_Form


from pynput.keyboard import Key, Controller


class _ControlsDataView(QtWidgets.QTableView):
    selection_changed = QtCore.Signal(object)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        result = super(_ControlsDataView, self).mousePressEvent(event)
        self.selection_changed.emit(self.selectedIndexes())
        return result


class EditorView(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EditorView, self).__init__(parent)
        self.setupUi(self)
        self._overrideWidgets()
        self._model = None
        # mapper settings
        self._mapper_start_column = 1
        self._mapper_row = 0
        self._mapper = QtWidgets.QDataWidgetMapper(self)

        # setup search filter
        self._filter_proxy_model = QtCore.QSortFilterProxyModel()
        self._filter_proxy_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.filterLineEdit.textChanged.connect(
            self._filter_proxy_model.setFilterRegularExpression
        )

        # change mapping section on item changed
        self.listView.selection_changed.connect(self._on_list_view_selection_changed)

        # trick for force updating model with enter press event
        self.clampMaxSlider.valueChanged.connect(self.force_press_enter)
        self.clampMinSlider.valueChanged.connect(self.force_press_enter)
        self.offsetSlider.valueChanged.connect(self.force_press_enter)
        self.scaleSlider.valueChanged.connect(self.force_press_enter)

    def force_press_enter(self):
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def _overrideWidgets(self):
        # replace list view with custom list view
        tmp = _ControlsDataView()
        self.verticalLayout_5.replaceWidget(self.listView, tmp)
        self.listView.close()
        self.listView = tmp

    def _on_list_view_selection_changed(self, selected_indexes):
        if not selected_indexes:
            return
        elif len(selected_indexes) > 1:
            raise Exception("unhandled behaviour, more than one index was selected")

        self._mapper.setCurrentIndex(self._filter_proxy_model.mapToSource(selected_indexes[0]).row())


    def _attach_mappings(self):
        # self._line_edits_mapper.clearMapping()
        self._mapper.clearMapping()

        self._mapper.addMapping(self.clampMinSlider, self._mapper_start_column + 1)
        self._mapper.addMapping(self.clampMaxSlider, self._mapper_start_column)
        self._mapper.addMapping(self.offsetSlider, self._mapper_start_column + 2)
        self._mapper.addMapping(self.scaleSlider, self._mapper_start_column + 3)
        # # map line edits
        self._mapper.addMapping(self.clampMaxLineEdit, self._mapper_start_column)
        self._mapper.addMapping(self.clampMinLineEdit, self._mapper_start_column + 1)
        self._mapper.addMapping(self.offsetLineEdit, self._mapper_start_column + 2)
        self._mapper.addMapping(self.scaleLineEdit, self._mapper_start_column + 3)

        # self._line_edits_mapper.toFirst()
        self._mapper.toFirst()

    def _on_layout_changed(self):
        self._attach_mappings()

    def model(self):
        return self._model

    def setModel(self, model):

        self._filter_proxy_model.setSourceModel(model)
        # TODO temp solution
        self._model = self._filter_proxy_model
        model.all_data_changed.connect(self._on_layout_changed)

        self.listView.setModel(self._model)
        # self._line_edits_mapper.setModel(self._model)
        # self._clamp_min_slider_mapper.setModel(self._model)
        # self._clamp_max_slider_mapper.setModel(self._model)
        # self._offset_slider_mapper.setModel(self._model)
        # self._scale_slider_mapper.setModel(self._model)

        self._mapper.setModel(model)

        # map sliders and line edits
        self._attach_mappings()
