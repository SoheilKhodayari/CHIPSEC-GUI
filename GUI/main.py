
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
from mainWindow import *
from terminal import *
from local_settings import *
from utils import _sudo_exec, _makeFile



class Main(QtGui.QMainWindow):

    def __init__(self, appModel):

        super(Main, self).__init__()
        self.setMinimumWidth(1200)
        #self.setMinimumHeight(600)
        self.setMinimumHeight(450)

        # @Note
        # appModel is "py" or "pyc", f\etched from argv
        # this will determine how to treat other python file extentions
        self.appModel = appModel  

        self._initUI()

    def _initUI(self):

        self.center()
        self.setWindowTitle(MAIN_WINDOW_APP_TITLE)

        self.mainLayout = QVBoxLayout()

        self.widget=mainWindow(self)

        self.scrollArea = QScrollArea()
        self.console = embeddedTerminal(self)
        self.scrollArea.setWidget(self.console)
        self.scrollArea.setFixedSize(550,200)

        self.scrollArea2 = QScrollArea()
        self.termianlTextEdit = QTextEdit()
        self.scrollArea2.setWidget(self.termianlTextEdit)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setFixedSize(550,200)
        self.termianlTextEdit.setFixedSize(900,200)
        self.termianlTextEdit.setReadOnly(True)
        self.termianlTextEdit.setStyleSheet("color: white; background-color: #0D0C0C;")


        self.terminalsHorizonalPane = QHBoxLayout()
        self.terminalsHorizonalPane.addWidget(self.scrollArea)
        self.terminalsHorizonalPane.addWidget(self.scrollArea2)


        self.mainLayout.addWidget(self.widget)
        self.mainLayout.addLayout(self.terminalsHorizonalPane)
        self.mainWidget = QWidget(self)
        self.mainWidget.setLayout(self.mainLayout)


        self.setCentralWidget(self.mainWidget)

        self.scrollArea.hide()
        self.scrollArea2.hide()

        self.makeMenu()
        self.show()

        self._writeOutputInSecondTerminal("[Chipsec] >\n")

    def get_app_model(self):
        return self.appModel

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to Exit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.console._terminate_tmux()
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def makeMenu(self):
        iconExit = QtGui.QIcon('icons/exit.png')
        exitAction = QtGui.QAction(iconExit, '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        iconTestSummary = QtGui.QIcon('icons/attach.png')
        summaryAction = QtGui.QAction(iconTestSummary, '&Test Summary', self)
        summaryAction.setShortcut('Ctrl+D')
        summaryAction.setStatusTip('Test Summary Window')
        summaryAction.triggered.connect(self._render_test_summary_window_now)

        iconShowConsole= QtGui.QIcon('icons/autopilot.png')
        self.showConsoleAction = QtGui.QAction(iconShowConsole, '&Show Console', self, checkable= True)
        self.showConsoleAction.setShortcut('Ctrl+W')
        self.showConsoleAction.setStatusTip('Show Console Window')
        self.showConsoleAction.triggered.connect(self._show_or_hide_terminal)

        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 2000, 23))
        menufile = menubar.addMenu('File')

        menufile.addAction(summaryAction)
        menufile.addAction(self.showConsoleAction)
        menufile.addAction(exitAction)

    def _show_or_hide_terminal(self):

        if self.showConsoleAction.isChecked():
            self.resize(1200,600)
            self.scrollArea2.show()
            self.scrollArea.show()
        else:
            self.resize(1200,450)
            self.scrollArea2.hide()
            self.scrollArea.hide()



    def _render_test_summary_window_now(self):
        if self.widget.test_summary_widget is not None:
            self.widget.test_summary_widget.show()
        else:
            QtGui.QMessageBox.information(self, SHOW_TEST_SUMMARY_REQUEST_ERROR_TITLE, SHOW_TEST_SUMMARY_REQUEST_ERROR_LMSG)

    def _writeOutputInSecondTerminal(self, text):
        self.termianlTextEdit.setText(str(text))

    def appendOutputInSecondTerminal(self, text):
        self.termianlTextEdit.setText(str(self.termianlTextEdit.toPlainText()) + text )       

    def runCommandInSecondTerminal(self, command= "sudo chipsec_main -i"):

        stdouterr = _sudo_exec(command, ROOT_PASSWORD)
        self._writeOutputInSecondTerminal(stdouterr)

    def runCommandInFirstTerminal(self,command):
        self.console.runCommand(command)




def main(argv=None):
    
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('CleanLooks'))
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icons/cr2.png'))

    if (argv is not None) and (len(argv)!=0):
        appModel = argv[0]
    else:
        appModel = "py"


    splash_pix = QtGui.QPixmap('icons/logoMain.png')
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.show()

    def render_main_app(appModel):
        splash.close()
        global ex
        ex = Main(appModel)
        ex.show()


    QtCore.QTimer.singleShot(1000, lambda appModel=appModel: render_main_app(appModel))
    sys.exit(app.exec_())



if __name__ == '__main__':
    main(sys.argv[1:])


