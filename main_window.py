import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMessageBox
import cv2

from oper_with_file import show_image_from_file, open_and_write, write_file_abs_rel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63)\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, -1, 681, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 310, 201, 132))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy)
        self.button_up.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.button_up.setObjectName("button_up")
        self.verticalLayout.addWidget(self.button_up)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.button_down = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_down.sizePolicy().hasHeightForWidth())
        self.button_down.setSizePolicy(sizePolicy)
        self.button_down.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.button_down.setObjectName("button_down")
        self.verticalLayout.addWidget(self.button_down)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.button_view = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_view.sizePolicy().hasHeightForWidth())
        self.button_view.setSizePolicy(sizePolicy)
        self.button_view.setStyleSheet("background-color: rgb(0, 115, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"")
        self.button_view.setObjectName("button_view")
        self.verticalLayout.addWidget(self.button_view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 37))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionDelete_all = QtWidgets.QAction(MainWindow)
        self.actionDelete_all.setObjectName("actionDelete_all")
        self.menuFile.addAction(self.actionOpen)
        self.actionOpen.triggered.connect(self.open_dir_write)
        self.menuFile.addAction(self.actionSave_as)
        self.actionSave_as.triggered.connect(self.save_in_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDelete_all)
        self.actionDelete_all.triggered.connect(self.delete_table)
        self.menubar.addAction(self.menuFile.menuAction())

        self.button_up.clicked.connect(self.move_up)
        self.button_down.clicked.connect(self.move_down)
        self.button_view.clicked.connect(self.show_image)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_dir_write(self) -> None:
        folder_path = QFileDialog.getExistingDirectory()
        if folder_path != "":
            self.write_in_table(folder_path)


    def save_in_file(self) -> None:
        save_file = QFileDialog.getSaveFileName()[0]
        if save_file != "":
            open_and_write(save_file, self.list_from_table())


    def delete_table(self) -> None:
        self.tableWidget.clear()


    def write_in_table(self, path_to_dir) -> None:
        all_path = []
        all_path = write_file_abs_rel(all_path, path_to_dir)
        self.tableWidget.setRowCount(len(all_path))
        for index in range(0, len(all_path)):
            element = QTableWidgetItem(all_path[index][0])
            self.tableWidget.setItem(index, 0, element)
            element = QTableWidgetItem(all_path[index][1])
            self.tableWidget.setItem(index, 1, element)


    def list_from_table(self) -> list[list[str]]:
        all_path = []
        for row in range(0, self.tableWidget.rowCount()):
            for colom in range(0, self.tableWidget.columnCount()):
                all_path.append(["",""])
                element = self.tableWidget.item(row,colom)
                all_path[row][colom] = element.text()
        return all_path


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Абсолютный путь (ПК)"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Относительный путь (ПК)"))
        self.button_up.setText(_translate("MainWindow", "Up"))
        self.button_down.setText(_translate("MainWindow", "Down"))
        self.button_view.setText(_translate("MainWindow", "View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionDelete_all.setText(_translate("MainWindow", "Delete all"))


    def move_up(self) -> None:
        current_row = self.tableWidget.currentRow()
        if current_row > 0:
            self.tableWidget.selectRow(current_row - 1)


    def move_down(self) -> None:
        current_row = self.tableWidget.currentRow()
        if current_row < (self.tableWidget.rowCount() - 1):
            self.tableWidget.selectRow(current_row + 1)


    def show_image(self) -> None:
        element = self.tableWidget.item(self.tableWidget.currentRow(), 1)
        if element.text != "":
            try:
                image = cv2.imread(element.text())
                show_image_from_file(image)
            except Exception as ex:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Невозможно отобразить этот файл")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                error.setInformativeText("Возможно данный файл не имеет расширение типа изображение")
                error.setDetailedText(str(ex))
                error.exec_()
                print(ex)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
