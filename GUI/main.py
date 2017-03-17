
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
from mainWindow import *
from terminal import *
from local_settings import *
from utils import _sudo_exec, _makeFile



class Main(QtGui.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setMinimumWidth(1200)
        self.setMinimumHeight(600)
        self._initUI()


    def _initUI(self):

        self.center()
        self.setWindowTitle('Testing')

        mainLayout = QVBoxLayout()

        self.widget=mainWindow(self)

        scrollArea = QScrollArea()
        self.console = embeddedTerminal(self)
        scrollArea.setWidget(self.console)
        #scrollArea.setFixedSize(550,310)  # set this to make console bigger
        scrollArea.setFixedSize(550,200)

        scrollArea2 = QScrollArea()
        self.termianlTextEdit = QTextEdit()
        scrollArea2.setWidget(self.termianlTextEdit)
        scrollArea2.setWidgetResizable(True)
        scrollArea2.setFixedSize(550,200)
        #self.termianlTextEdit.setFixedSize(500,300)
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

        # iconHelp = QtGui.QIcon('icons/qs_mark.png')
        # helpAction = QtGui.QAction(iconHelp, '&Help', self)
        # helpAction.setShortcut('Ctrl+H')
        # helpAction.setStatusTip('Help')
        # helpAction.triggered.connect(self._render_help_dialog)


        menubar = QtGui.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 2000, 23))
        menufile = menubar.addMenu('File')

        #menufile.addAction(helpAction)
        menufile.addAction(exitAction)


    def _writeOutputInSecondTerminal(self, text):
        self.termianlTextEdit.setText(str(self.termianlTextEdit.toPlainText()) + text )

    def runCommandInSecondTerminal(self, command= "sudo chipsec_main -i"):

        stdouterr = _sudo_exec(command, ROOT_PASSWORD)
        self._writeOutputInSecondTerminal(stdouterr)
        #_makeFile(stdouterr)

    def runCommandInFirstTerminal(self,command):
        self.console.runCommand(command)

    # def _render_help_dialog(self):
    #     w = QtGui.QWidget()
    #     Qv = QVBoxLayout()
    #     label1 = QLabel()
    #     label1.setText("Terminal(TMUX) Scroll Mode Keys:")
    #     label2 = QLabel()
    #     label2.setText("Press: CTRL + b + [ to switch to  scroll mode")
    #     label3 = QLabel()
    #     label3.setText("press: q to exit scroll mode")
    #     Qv.addWidget(label2)
    #     Qv.addWidget(label2)
    #     Qv.addWidget(label3)
    #     w.setLayout(Qv)
    #     w.show()



def main():
    #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('SGI'))
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('CleanLooks'))
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icons/cr2.png'))

    ex = Main()
    ex.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


