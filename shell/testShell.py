import os, sys, re, fileinput
from prompt import Prompt

prompt = Prompt()
pid = os.getpid()

pr, pw = os.pipe()

for f in (pr, pw):
    os.set_inheritable(f, True)

args = prompt.talk()

args1 = args[:args.index('|')]
args2 = args[args.index('|')+1:]

rc = os.fork()

if rc == 0:

    os.close(1)
    os.dup(pw)

    for fd in (pr, pw):
        os.close(fd)

    for dir in re.split(":", os.environ['PATH']):
        program = "%s/%s" % (dir, args1[0])
        try:
            os.execve(program, args, os.environ)
        except FileNotFoundError:
            pass
    sys.exit(1)

else:

    pipeRC = os.fork()

    if pipeRC == 0:
        os.close(0)
        os.dup(pr)
        for fd in (pw, pr):
            os.close(fd)

        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir, args2[0])
        try:
            os.execve(program, args, os.environ)
        except FileNotFoundError:
            pass
        sys.exit(1)

    else:
        os.wait()

    childPidCode = os.wait()
