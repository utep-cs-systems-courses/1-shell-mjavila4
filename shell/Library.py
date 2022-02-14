class Library:

    keyword_dict = {'change': }

    @classmethod
    def to_string(cls):
        print(cls.keywordDict)

    @classmethod
    def add(cls, key, data):
        cls.keywordDict[key] = data

    @classmethod
    def get(cls, key):
        cls.keyword_dict[key]()
