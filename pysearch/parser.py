

class Parser:
    def __init__(self, parser):
        self.parser = parser

    def parse(self, text):
        return self.parser.parse(text)


class NgramParser:
    @classmethod
    def parse(cls, n, text):
        if len(text) < n:
            return [text]
        return [text[i: i + n] for i in range(0, len(text) - (n-1))]


class BigramParser(NgramParser):
    @classmethod
    def parse(cls, text):
        return super(BigramParser, cls).parse(2, text)
