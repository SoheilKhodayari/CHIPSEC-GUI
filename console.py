#!/usr/bin/env python
#-*- coding:utf-8 -*-


#  tmux source-file ~/.tmux.conf

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import uuid

class embeddedTerminal(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self._processes = []
        self.resize(800, 600)
        self.terminal = QWidget(self)
        self.id = uuid.uuid4()
        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)
        self._start_process(
            'xterm',
            ['-into', str(self.terminal.winId()),
             '-e', 'tmux', 'new', '-s', '%s'%self.id]
        )

    def _start_process(self, prog, args):
        child = QProcess()
        self._processes.append(child)
        child.start(prog, args)

    def _list_files(self):
        self._start_process(
            'tmux', ['send-keys', '-t', '%s:0'%self.id, 'ls', 'Enter'])

    def _terminate_tmux(self):
        self._start_process(
            'tmux', ['send-keys', '-t', '%s:0'%self.id, 'tmux kill-window -t 0', 'Enter'])

    def closeEvent(self, event):
        self._terminate_tmux()

    def switchToScrollMode(self):


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = embeddedTerminal()
    main.show()
    sys.exit(app.exec_())