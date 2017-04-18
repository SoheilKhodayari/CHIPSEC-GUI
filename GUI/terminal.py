# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
import uuid, time
from local_settings import ROOT_PASSWORD
from utils import _sudo_exec

class embeddedTerminal(QWidget):

    def __init__(self, parent):
        super(embeddedTerminal, self).__init__()
        self._processes = []
        self.parent = parent
        self.uuid = uuid.uuid4()

        #self.terminal = QWidget(self)
        # self.terminal = QtGui.QTextBrowser()
        # self.terminal.setFixedSize(730, 440)
        # self.terminal.setFrameStyle(QtGui.QTextEdit.DrawWindowBackground)

        listBox = QVBoxLayout(self)
        self.setLayout(listBox)

        scroll = QScrollArea(self)
        listBox.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrollContent = QWidget(scroll)

        scrollLayout = QVBoxLayout(scrollContent)
        scrollContent.setLayout(scrollLayout)
        scroll.setWidget(scrollContent)
        scroll.setFixedSize(487,300)



        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.terminal)
        # parentHLayout.addLayout(self.layout)

        self._start_process(
            'xterm',
            ['-into', str(scroll.winId()),
             '-e', 'tmux', 'new-session', '-s', '{0}'.format(self.uuid),'-x','50','-y','50']
        )

    def _start_process(self, prog, args):
        child = QProcess()
        self._processes.append(child)
        child.start(prog, args)
        # self.child.terminate()
        # self.child.waitForFinished()

    def _list_files(self):
        self._start_process(
            'tmux', ['send-keys', '-t', '{0}:0'.format(self.uuid), 'ls', 'Enter'])

    def _terminate_tmux(self):
        # self._start_process(
        #     'tmux', ['send-keys', '-t', '%s:0'%self.uuid, 'exit', 'Enter'])
        for process in self._processes:
            process.terminate()

    def _resize_tmux(self):
        self._start_process(
            'tmux', ['send-keys', '-t', '%s:0'%self.uuid, 'resize-pane -t 0 -R 500', 'Enter'])

    def _switch_to_root(self, password= ROOT_PASSWORD):
        self._start_process(
            'tmux', ['send-keys', '-t', '%s:0'%self.uuid,"sudo su", 'Enter'])
        time.sleep(0.5)
        self._start_process(
            'tmux', ['send-keys', '-t', '%s:0'%self.uuid, str(password) , 'Enter'])


    def runCommand(self,command, password_prompt_req_flag=False):
        if password_prompt_req_flag: # if expecting sudo in command and already not a sudoer
            self._start_process(
                'tmux', ['send-keys', '-t', '%s:0'%self.uuid, '%s'%command, 'Enter'])
            time.sleep(1)
            self._start_process(
                'tmux', ['send-keys', '-t', '%s:0'%self.uuid, str(ROOT_PASSWORD) , 'Enter'])

        else:
            self._start_process(
                'tmux', ['send-keys', '-t', '%s:0'%self.uuid, '%s'%command, 'Enter'])

        self._start_process(
                'tmux', ['capture-pane', '-t', '%s:0'%self.uuid])

        #stdout, stderr = process.communicate()
        # tmux capture-pane -pS -32768
        #print Popen(['tmux', 'capture-pane','-pS','-32768'], stdout=PIPE).communicate()[1]

        # tmux help, See link below
        # http://unix.stackexchange.com/questions/125647/get-tmux-scroll-buffer-contents
        QtCore.QTimer.singleShot(3000, lambda: self._callback_tmux())

    def _callback_tmux(self):
        stderr = _sudo_exec("tmux capture-pane -pS -32768 -t {0}".format(self.uuid), ROOT_PASSWORD)
        msg =""
        try:
            idx = stderr.rindex("SUMMARY")
            msg = stderr[idx-5:-65]
        except:
            msg = "\n[Error] SUMMARY NOT YET AVAILABLE!\n This will happen if: \n\n (1) The specified tests have internal error(s) or \n (2) A very time-consuming/long output test was running .\n\nIf you want to know more, Here's what you can do:\n\n(1) check the rear terminal for errors/outputs!! \n(2) DO \"tmux capture-pane -pS -32768\" on terminal without quotes TO SEE THE RESULT MANUALLY"
        
        # Uncomment this to print chipsec summary in second terminal
        #self.parent._writeOutputInSecondTerminal(msg)  




