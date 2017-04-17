import platform, os, logging
import subprocess, pexpect
import uuid
from local_settings import REPORT_PATH, ENV

log = logging.getLogger(__name__)

def _sudo_exec(cmdline, passwd):
    """ run a sudo command and returns stdouterr """
    output = ""
    if ENV == "LIVE":
        # LIVE mode does not prompt for sudo password
        output = exec_with_sudo_privilige(cmdline, passwd)
    else:
        output = exec_with_sudo_privilige(cmdline, passwd)

    return output

def exec_with_user_privilige(cmdline):
    process = subprocess.Popen(cmdline.split(), stdout=subprocess.PIPE, cwd="/home/soheil/Desktop/iust/chipsec/GUI")
    output, error = process.communicate()
    return output

def exec_with_sudo_privilige(cmdline, passwd):
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

def _makeFile(content, base_path = REPORT_PATH, ext = ".txt"):
    filename = str(uuid.uuid4())
    absolute_name = base_path + "/" + filename + ext
    with open(filename,"w+") as file:
        file.write(content)