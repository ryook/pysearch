from pymongo import MongoClient
from parser import BigramParser
from bson.objectid import ObjectId

db_client = MongoClient('localhost', 27017)
DB = db_client.fulltext_search
index_collection = DB.index
text_collection = DB.text


def search(query, slop=0, parser=BigramParser):
        tokens = parser.parse(query)
        docs = []
        for token in tokens:
            keyword = index_collection.find_one({"keyword": token})
            if keyword:
                docs += keyword['documents']
        doc_position = [d.split(':') for d in docs]

        result = []
        doc_ids = set([d[0] for d in doc_position])
        for doc_id in doc_ids:
            doc = text_collection.find_one({'_id': ObjectId(doc_id)})
            result.append(doc["text"])
        return result


if __name__ == "__main__":
    result = search('みなとみらい')
    for r in result:
        print(r)


