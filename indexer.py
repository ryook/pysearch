from pymongo import MongoClient


db_client = MongoClient('localhost', 27017)
DB = db_client.fulltext_search

class Indexer:
    def __init__(self, parser):
        self.parser = parser

    def add_document(self, text):
        # dbに登録する処理
        collections = DB.text
        doc = collections.insert_one({'text': text})
        return str(doc.inserted_id)

    def tokenize(self, text):
        return self.parser.parse(text)

    def create_new_posting_list(self, tokens, document_id):
        return [(document_id, token, position) for position, token in enumerate(tokens)]

    def update_index(self, text):
        document_id = self.add_document(text)
        tokens = self.tokenize(text)
        posting_list = self.create_new_posting_list(tokens, document_id)

        ## dbに登録する処理
        collections = DB.index
        for p in posting_list:
            doc = collections.find_one({'keyword': p[1]})
            if doc:
                doc['documents'].append('{}:{}'.format(p[0], p[2]))
                collections.save(doc)
            else:
                collections.insert_one({
                    "keyword": p[1],
                    "documents": ['{}:{}'.format(p[0], p[2])]
                })
        return "doc:{} OK".format(document_id)
