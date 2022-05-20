import json
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets
from widgets.facecap_tweak import FacecapTweak
from copy import deepcopy
from osc_client import OSCCLient


class FacecapTweakMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(FacecapTweakMainWindow, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)
        self._default_config = self.read_config("default_config.json")
        self.osc_client = OSCCLient()
        self.main_layout = QtWidgets.QHBoxLayout()
        self.facecap_tweak_widget = FacecapTweak(self.osc_client, parent=self)
        self.facecap_tweak_widget.set_config_data(self.default_config)
        self.send_all_osc()


        # Creating menus
        self.create_menu()

        # FIXME TEMP SOLUTION
        self.setFixedHeight(self.facecap_tweak_widget.height())
        self.setFixedWidth(self.facecap_tweak_widget.width())
        # FIXME______________________________________________

        self.main_layout.addWidget(self.facecap_tweak_widget)
        self.setLayout(self.main_layout)

    def send_all_osc(self):
        for i in self.facecap_tweak_widget.get_config_data().values():
            self.osc_client.send_message(((i['index'] - 1) * 4) + 2, i["Clamp Max"])
            self.osc_client.send_message(((i['index'] - 1) * 4) + 1, i["Clamp Min"])
            self.osc_client.send_message(((i['index'] - 1) * 4) + 3, i["Offset"])
            self.osc_client.send_message(((i['index'] - 1) * 4) + 4, i["Scale Factor"] * 0.01)







    @property
    def default_config(self):
        return deepcopy(self._default_config)

    def create_menu(self):
        main_menu = self.menuBar()
        fileMenu = main_menu.addMenu("File")

        newAction = QtGui.QAction("New", self)
        newAction.setShortcut("Ctrl+N")
        fileMenu.addAction(newAction)
        newAction.triggered.connect(self.on_file_new)

        openAction = QtGui.QAction("Open", self)
        openAction.setShortcut("Ctrl+N")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.on_file_open)

        fileMenu.addSeparator()

        # saveAction = QtGui.QAction("Save", self)
        # saveAction.setShortcut("Ctrl+S")
        # fileMenu.addAction(saveAction)
        # saveAction.triggered.connect(self.on_file_save)

        saveAsAction = QtGui.QAction("SaveAs", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        fileMenu.addAction(saveAsAction)
        saveAsAction.triggered.connect(self.on_file_save_as)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options,
        )
        if fileName:
            return fileName

    # def openFileNamesDialog(self):
    #     options = QtWidgets.QFileDialog.Options()
    #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
    #     files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
    #                                             "All Files (*);;Python Files (*.py)", options=options)
    #     if files:
    #         print(files)

    def saveFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            "",
            "All Files (*);;Text Files (*.json)",
            options=options,
        )
        if fileName:
            return fileName

    def on_file_new(self):
        self.facecap_tweak_widget.set_config_data(self.default_config)
        print("new file")
        self.send_all_osc()

    def on_file_open(self):
        path = self.openFileNameDialog()
        if path:
            self.facecap_tweak_widget.set_config_data(self.read_config(path))
            self.send_all_osc()
        print(f'opening file: "{path}"')

    # def on_file_save(self):
    #     print('saving file')

    def on_file_save_as(self):
        save_path = self.saveFileDialog()
        if save_path:
            self.write_config(save_path)
        print(f'saving as file to: "{save_path}"')

    def read_config(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def write_config(self, path):
        with open(path, "w") as f:
            f.write(json.dumps(self.facecap_tweak_widget.get_config_data(), indent=4))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet(open(r".\resources\Darkeum.qss").read())
    wgt = FacecapTweakMainWindow()
    # wgt = FacecapTweak([])
    wgt.show()
    app.exec()
