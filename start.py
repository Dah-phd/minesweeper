import subprocess
from sys import platform
input('Press ENTER to start game!')
if platform[:3] == 'win':
    cmd = 'modules\\GUI.pyw'
else:
    cmd = 'python3 ./modules/GUI.py'
subprocess.Popen(cmd, shell=True, stdin=None,
                 stdout=None, stderr=None, close_fds=True, creationflags=subprocess.DETACHED_PROCESS)
