#! /usr/bin/env python3

import os, sys, time, re, fileinput

pid = os.getpid()
args = ["ls", "|", "sort"]

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
            os.execve(program, args[:args.index("|")], os.environ)
        except FileNotFoundError:
            pass
    
else:

    rc2 = os.fork()

    if rc2 == 0:

        os.close(0)
        os.dup(pr)

        for dire in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dire, args[args.index("|")+1])
        try:
            os.execve(program, args[args.index("|")+1:], os.environ)
        except FileNotFoundError:
            pass

    else:
        os.wait()
        for fd in (pw, pr):
            os.close(fd)



