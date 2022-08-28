from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 292)
        MainWindow.setMinimumSize(QtCore.QSize(553, 292))
        MainWindow.setMaximumSize(QtCore.QSize(553, 292))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{\n"
                                 "background-image: url(:/images/bg.jpg);\n"
                                 "}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 220, 551, 71))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.btn_start = QtWidgets.QPushButton(self.page)
        self.btn_start.setGeometry(QtCore.QRect(10, 0, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_start.setFont(font)
        self.btn_start.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_start.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_start.setAutoFillBackground(False)
        self.btn_start.setStyleSheet("QPushButton#btn_start{\n"
                                     "    border-radius: 20px;\n"
                                     "    background-color: rgb(0, 255, 0);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#btn_start:hover{\n"
                                     "    background-color: rgb(0, 170, 0);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton#btn_start:pressed{\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-top: 5px;\n"
                                     "}")
        self.btn_start.setAutoDefault(False)
        self.btn_start.setDefault(False)
        self.btn_start.setObjectName("btn_start")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.btn_stop = QtWidgets.QPushButton(self.page_2)
        self.btn_stop.setGeometry(QtCore.QRect(9, 0, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setStyleSheet("QPushButton#btn_stop{\n"
                                    "    border-radius: 20px;\n"
                                    "    background-color: rgb(255, 0, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton#btn_stop:hover{\n"
                                    "    background-color: rgb(170, 0, 0);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "QPushButton#btn_stop:pressed{\n"
                                    "    padding-left: 5px;\n"
                                    "    padding-top: 5px;\n"
                                    "}")
        self.btn_stop.setObjectName("btn_stop")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.btn_reset = QtWidgets.QPushButton(self.page_3)
        self.btn_reset.setGeometry(QtCore.QRect(10, 0, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("QPushButton#btn_reset{\n"
                                     "    border-radius: 20px;\n"
                                     "    background-color: rgb(255, 255, 0);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#btn_reset:hover{\n"
                                     "    background-color: rgb(255, 255, 127);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton#btn_reset:pressed{\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-top: 5px;\n"
                                     "}")
        self.btn_reset.setObjectName("btn_reset")
        self.btn_continue = QtWidgets.QPushButton(self.page_3)
        self.btn_continue.setGeometry(QtCore.QRect(274, 0, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_continue.setFont(font)
        self.btn_continue.setStyleSheet("QPushButton#btn_continue{\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color: rgb(85, 255, 127);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#btn_continue:hover{\n"
                                        "    background-color: rgb(0, 255, 0);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "QPushButton#btn_continue:pressed{\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 5px;\n"
                                        "}")
        self.btn_continue.setObjectName("btn_continue")
        self.stackedWidget.addWidget(self.page_3)
        self.widget_time = QtWidgets.QWidget(self.centralwidget)
        self.widget_time.setGeometry(QtCore.QRect(-1, 19, 551, 161))
        self.widget_time.setObjectName("widget_time")
        self.label = QtWidgets.QLabel(self.widget_time)
        self.label.setGeometry(QtCore.QRect(0, -20, 551, 221))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(87)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.btn_continue.setText(_translate("MainWindow", "Continue"))
        self.label.setText(_translate("MainWindow", "00:00:00"))
