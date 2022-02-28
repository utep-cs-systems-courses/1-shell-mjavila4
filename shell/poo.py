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

args1 = 'ls'
args2 = 'sort'

rc1 = os.fork()

    if rc1 == 0:

        os.close(1)
        os.dup(pw)
        os.set_inheritable(1, True)

        for fd in (pw, pr):
            os.close(fd)

        Exec.execProgram(arg.split())

    else:

        os.wait()
        rc2 = os.fork()

        if rc2 == 0:
            os.close(0)
            os.dup(pr)
            os.set_inheritable(0, True)

            for fd in (pw, pr):
                os.close(fd)

            Exec.execProgram(nextArg.split())

        else:
            os.wait()
            sys.exit()
