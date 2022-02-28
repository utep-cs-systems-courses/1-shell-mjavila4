#! /usr/bin/env python3

import os, sys, re, fileinput
from prompt import Prompt
from change_dir import ChangeDir
from redirect import Redirect
from exec import Exec
from pipe import Pipe

prompt = Prompt()

pid = os.getpid()

while 1:

    args = prompt.talk()
    argsList = args.split()

    if argsList[0] == 'exit':
        sys.exit()

    if len(argsList) > 1 and argsList[0] == 'cd':
        ChangeDir.change(argsList[1])
        sys.exit()

    rc = os.fork()

    if rc == 0:

        if argsList[0] == 'show':
            os.write(1, os.getcwd().encode())
            sys.exit()

        if '|' in args:
            Exec.execPipe(argsList)
            sys.exit()

        Exec.execProgram(argsList)
        sys.exit()

    else:
        os.wait()
















