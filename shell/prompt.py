class Prompt:
    # defPrompt = os.environ['PS1']
    defPrompt = '$'

    def __init__(self):
        self.currentPrompt = self.defPrompt

    def talk(self):
        user = input(self.currentPrompt + " ")
        return user

    def changePrompt(self, user_input):
        self.currentPrompt = user_input
