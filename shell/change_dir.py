import os, re


class ChangeDir:

    @staticmethod
    def change(user_input):
        try:
            os.chdir(user_input)
            return 0
        except FileNotFoundError:
            os.write(1, "Incorrect Path, File Not Found\n".encode())
            return -1

    @staticmethod
    def back():
        pattern = re.compile(r'\\')
        last_match = 0
        matches = pattern.finditer(os.getcwd())
        for match in matches:
            last_match = match

        os.chdir(os.getcwd()[:match.span()[0]])
