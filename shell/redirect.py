import os


class Redirect:

    @staticmethod
    def checkOp(args):
        hasOperator = False
        for word in args:
            if word == ">":
                hasOperator = True
                break
        return hasOperator

    @staticmethod
    def checkIndex(args):
        index = -1
        counter = 0
        for word in args:
            if word == ">":
                index = counter + 1
                break
            counter += 1
        return index

    @staticmethod
    def checkRedirect(args):
        if Redirect.checkOp(args) and len(args) >= Redirect.checkIndex(args):
            os.close(1)
            os.open(args[Redirect.checkIndex(args)], os.O_CREAT | os.O_WRONLY)
            os.set_inheritable(1, True)
