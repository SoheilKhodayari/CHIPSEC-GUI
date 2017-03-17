import platform, os, logging
import subprocess, pexpect
import uuid
from local_settings import REPORT_PATH

log = logging.getLogger(__name__)

def _sudo_exec(cmdline, passwd):
    """ run a sudo command and returns stdouterr """
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

