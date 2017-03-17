import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 


import platform, os, logging
import subprocess, pexpect

log = logging.getLogger(__name__)

def sudo_exec(cmdline, passwd):
    osname = platform.system()
    if osname == 'Linux':
        prompt = r'\[sudo\] password for %s: ' % os.environ['USER']
    elif osname == 'Darwin':
        prompt = 'Password:'
    else:
        assert False, osname

    child = pexpect.spawn(cmdline)
    idx = child.expect([prompt, pexpect.EOF], 3)
    if idx == 0: # if prompted for the sudo password
        log.debug('sudo password was asked.')
        child.sendline(passwd)
        child.expect(pexpect.EOF)
    return child.before


 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
        # create objects
        label = QLabel(self.tr("Enter command and press Return"))
        self.le = QLineEdit()
        self.te = QTextEdit()

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 

        # create connection
        self.connect(self.le, SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        cmd = "sudo chipsec_main -i"
        # #stdouterr = os.popen4(cmd)[1].read()
        # stdouterr = os.popen("sudo -S %s"%(cmd), 'w').write('mypass')
        stdouterr = sudo_exec(cmd,"9759865")
        with open("output.txt","w+") as out:
            out.write(stdouterr)


  
if __name__ == "__main__": 
    main()