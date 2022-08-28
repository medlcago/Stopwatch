import time
import ResourceCollectionFiles

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from UiFiles import Ui_MainWindow


class Stopwatch(QMainWindow):
    def __init__(self):
        self.TIME = 0
        super(Stopwatch, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon(".\\img\\IconWindow.png"))

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.stopwatch)

        self.get_buttons()

    def get_buttons(self):
        self.ui.btn_start.clicked.connect(self.btn_start)
        self.ui.btn_stop.clicked.connect(self.btn_stop)
        self.ui.btn_continue.clicked.connect(self.btn_continue)
        self.ui.btn_reset.clicked.connect(self.btn_reset)

    def btn_start(self):
        self.timer.start()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def btn_stop(self):
        self.timer.stop()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def btn_continue(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.timer.start()

    def btn_reset(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.timer.stop()
        self.TIME = 0
        self.ui.label.setText("00:00:00")

    def stopwatch(self):
        self.ui.label.setText(time.strftime("%H:%M:%S", time.gmtime(self.TIME)))
        self.TIME += 1


if __name__ == '__main__':
    app = QApplication([])
    sw = Stopwatch()
    sw.show()
    app.exec_()
