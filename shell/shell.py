#! /usr/bin/env python3

import os, sys, re
from prompt import Prompt

prompt = Prompt()

pid = os.getpid()
rc = os.fork()

if rc < 0:
    os.write(2, ("fork failed, returning %d\n" % rc).encode())
    sys.exit(1)

elif rc == 0:
    while 1:

        args = prompt.talk()

        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                os.write(2, (("Child:    Could not exec %s\n" % args[0]).encode()))

    sys.exit(1)

else:
    childPidCode = os.wait()
