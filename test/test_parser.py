import pytest


class TestParser:

    def test_2gram_parser(self):
        from pysearch.parser import Parser, BigramParser

        parser = Parser(BigramParser)
        actual = parser.parse('test')
        assert actual == ['te', 'es', 'st']


class TestNgramParser:
    @pytest.mark.parametrize(
        "n,text,expected",
        [
            (1, 'test', ['t', 'e', 's', 't']),
            (2, 'test', ['te', 'es', 'st']),
            (3, 'test', ['tes', 'est']),
            (4, 'test', ['test']),
            (5, 'test', ['test'])
        ]
    )
    def test_parse(self, n, text, expected):
        from pysearch.parser import NgramParser

        actual = NgramParser.parse(n, text)
        assert actual == expected


class TestBigramParser:

    def test_parse(self):
        from pysearch.parser import BigramParser

        actual = BigramParser.parse('test')
        assert actual == ['te', 'es', 'st']
