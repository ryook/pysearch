import pytest
from pysearch.indexer import Indexer


@pytest.fixture
def indexer():
    from pysearch.parser import BigramParser
    return Indexer(BigramParser)


class TestIndexer:

    @pytest.mark.skip(reason='dbが仮のため')
    def test_add_document(self, indexer):
        actual = indexer.add_document('test')
        assert actual == '1'

    @pytest.mark.parametrize(
        'text,expected',
        [
            ('test', ['te', 'es', 'st'])
        ]
    )
    def test_tokenize(self, indexer, text, expected):
        actual = indexer.tokenize(text)
        assert actual == ['te', 'es', 'st']

    @pytest.mark.parametrize(
        "tokens,document_id, expected",
        [
            (['te', 'es', 'st'], 1, [
                (1, 'te', 0),
                (1, 'es', 1),
                (1, 'st', 2),
            ])
        ]
    )
    def test_create_new_posting_list(self, indexer, tokens, document_id, expected):
        actual = indexer.create_new_posting_list(tokens, document_id)
        assert actual == [
            (document_id, 'te', 0),
            (document_id, 'es', 1),
            (document_id, 'st', 2)
        ]

    @pytest.mark.skip(reason='dbが仮のため')
    def test_update_index(self, indexer):
        actual = indexer.update_index('東京タワー')
        assert False, actual
        # assert actual == 'doc:1 OK'
