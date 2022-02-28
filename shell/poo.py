#! /usr/bin/env python3

import os, fileinput, re

pid = os.getpid()
args = ["wc", "poo.py"]

pr, pw = os.pipe()

rc = os.fork()

for f in (pr, pw):
    os.set_inheritable(f, True)

if rc == 0:
    os.close(1)
    os.dup(pw)
    #os.set_inheritable(1, True)

    for fd in (pr, pw):
        os.close(fd)

    for dire in re.split(":", os.environ['PATH']):
        program = "%s/%s" % (dire, args[0])
        try:
            os.execve(program, args, os.environ)
        except FileNotFoundError:
            pass

else:

    os.close(0)
    os.dup(pr)
    #os.set_inheritable(0, True)

    for fd in (pw, pr):
        os.close(fd)

    for line in fileinput.input():
        print("From child: <%s>" % line)

    '''

    rc2 = os.fork()

    if rc2 == 0:

        os.close(0)
        os.dup(pr)

        for fd in (pw, pr):
            os.close(fd)

        for line in fileinput.input():
            print("From child: <%s>" % line)

        sys.exit()

    else:

        os.wait()'''



