class Library:
    keywordDict = dict()

    @classmethod
    def foo(self):
        print("This is foo!")

    @classmethod
    def to_string(self):
        print(self.keywordDict)

    @classmethod
    def add(self, key, data):
        self.keywordDict[key] = data

    @classmethod
    def get(self, key):
        self.keywordDict[key]()
