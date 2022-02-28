#! /usr/bin/env python3

import os, sys, re, fileinput
from prompt import Prompt
from change_dir import ChangeDir
from redirect import Redirect
from exec import Exec
from pipe import Pipe

prompt = Prompt()
pid = os.getpid()

pr, pw = os.pipe()

for f in (pr, pw):
    os.set_inheritable(f, True)

args = prompt.talk()
firstArg = ""
secondArg = ""

rc1 = os.fork()

if rc1 == 0:

    firstArg = args[:args.index('|')]
    print(firstArg)
    secondArg = args[args.index('|') + 2:]

    os.close(1)
    os.dup(pw)
    os.set_inheritable(1, True)

    for fd in (pw, pr):
        os.close(fd)

    Exec.execProgram(["ls"])

else:

    rc2 = os.fork()

    if rc2 == 0:
        os.close(0)
        os.dup(pr)
        os.set_inheritable(0, True)

        for fd in (pw, pr):
            os.close(fd)

        Exec.execProgram(["sort"])

    else:
        os.wait()

    for fd in (pw, pr):
        os.close(fd)

    os.wait()
