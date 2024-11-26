import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap

from iter import IteratorInDir


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.iterator_folder = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(65, 65, 65);\ncolor: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 50, MainWindow.size().width()-100, MainWindow.size().height()-100))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_prev = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_prev.setStyleSheet("background-color: rgb(0, 121, 255);\n")
        self.button_prev.setObjectName("button_prev")
        self.horizontalLayout.addWidget(self.button_prev)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.button_next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy)
        self.button_next.setStyleSheet("background-color: rgb(0, 121, 255);\n")
        self.button_next.setObjectName("button_next")
        self.horizontalLayout.addWidget(self.button_next)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_name.setStyleSheet("font-size: 20px")
        self.file_name.setObjectName("file_name")
        self.verticalLayout.addWidget(self.file_name)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.triggered.connect(self.open_folder)
        self.menuFile.addAction(self.action)
        self.menubar.addAction(self.menuFile.menuAction())

        self.button_next.clicked.connect(self.show_next)
        self.button_prev.clicked.connect(self.show_prev)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def insert_image(self, path_to_image: str):
        self.image = QImage(path_to_image)
        if self.image.isNull():
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Невозможно отобразить этот файл")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            error.setInformativeText("Возможно данный файл не имеет расширение типа изображение")
            error.setDetailedText("QPixmap::scaled: Pixmap is a null pixmap")
            error.exec_()
        pixmap = QPixmap.fromImage(self.image)
        scaled_pixmap = pixmap.scaled(700, 700, Qt.KeepAspectRatio)
        self.label.setPixmap(scaled_pixmap)
        self.label.setAlignment(Qt.AlignCenter)


    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory()
        if folder_path != "":
            self.iterator_folder = IteratorInDir(folder_path)
            if len(self.iterator_folder.filenames) != 0:
                 self.insert_image(next(self.iterator_folder))
                 self.file_name.setText(self.iterator_folder.filenames[self.iterator_folder.counter])
            elif len(self.iterator_folder.filenames) == 0:
                 self.label.setAlignment(Qt.AlignCenter)
                 self.label.setText("The folder is not include images")
                 self.file_name.setText((""))


    def show_next(self):
        if self.iterator_folder != None and len(self.iterator_folder.filenames) != 0:
            self.insert_image(str(next(self.iterator_folder)))
            self.file_name.setText(self.iterator_folder.filenames[self.iterator_folder.counter])


    def show_prev(self):
        if self.iterator_folder != None and len(self.iterator_folder.filenames) != 0:
            self.insert_image(self.iterator_folder.prev())
            self.file_name.setText(self.iterator_folder.filenames[self.iterator_folder.counter])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_prev.setText(_translate("MainWindow", "Previous"))
        self.button_next.setText(_translate("MainWindow", "Next"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
