#! /usr/bin/env python3

import os, sys, time, re, fileinput

pid = os.getpid()
args = ["wc", "poo.py"]

pr, pw = os.pipe()
for f in (pr, pw):
    os.set_inheritable(f, True)

rc = os.fork()

if rc == 0:
    os.close(1)
    os.dup(pw)

    for fd in (pr, pw):
        os.close(fd)

    for dire in re.split(":", os.environ['PATH']):
        program = "%s/%s" % (dire, args[0])
        try:
            os.execve(program, args, os.environ)
        except FileNotFoundError:
            pass

else:

    os.wait()

    '''os.wait()

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



