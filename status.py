import subprocess
import sys
from xmpp import *
FORTUNE_COMMAND="fortune -n 200 -s wisdom"
USERNAME = "username"       
PASSWORD = "password"
RESOURCE = "gmail.com"
AVAILABLE = "default"
def stat():
    status=subprocess.check_output(FORTUNE_COMMAND.split())[:-1]
    cl=Client(server='gmail.com',debug=[])
    if not cl.connect(server=('talk.google.com',5222)):
	    raise IOError('Can not connect to server.')
    if not cl.auth(USERNAME, PASSWORD, RESOURCE):
        raise IOError('Can not auth with server.')
    cl.send(Iq('set','google:shared-status',payload=[Node('show',payload=[AVAILABLE]),Node('status',payload=[status])]))
    cl.disconnect()

if __name__=="__main__":
    stat()

