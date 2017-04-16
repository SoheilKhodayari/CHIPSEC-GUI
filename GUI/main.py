
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
        self.setMinimumHeight(600)

        # @Note
        # appModel is "py" or "pyc", fetched from argv
        # this will determine how to treat other python file extentions
        self.appModel = appModel  

        self._initUI()

    def _initUI(self):

        self.center()
        self.setWindowTitle('Platform Security Assessment Framework')

        mainLayout = QVBoxLayout()

        self.widget=mainWindow(self)

        scrollArea = QScrollArea()
        self.console = embeddedTerminal(self)
        scrollArea.setWidget(self.console)
        scrollArea.setFixedSize(550,200)

        scrollArea2 = QScrollArea()
        self.termianlTextEdit = QTextEdit()
        scrollArea2.setWidget(self.termianlTextEdit)
        scrollArea2.setWidgetResizable(True)
        scrollArea2.setFixedSize(550,200)
        self.termianlTextEdit.setFixedSize(500,200)
        self.termianlTextEdit.setReadOnly(True)
        self.termianlTextEdit.setStyleSheet("color: white; background-color: #0D0C0C;")


        terminalsHorizonalPane = QHBoxLayout()
        terminalsHorizonalPane.addWidget(scrollArea)
        terminalsHorizonalPane.addWidget(scrollArea2)


        mainLayout.addWidget(self.widget)
        mainLayout.addLayout(terminalsHorizonalPane)
        mainWidget = QWidget(self)
        mainWidget.setLayout(mainLayout)


        self.setCentralWidget(mainWidget)

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


        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 2000, 23))
        menufile = menubar.addMenu('File')

        menufile.addAction(summaryAction)
        menufile.addAction(exitAction)


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
        #_makeFile(stdouterr)

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


