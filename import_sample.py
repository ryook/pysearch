from indexer import Indexer
from parser import BigramParser


with open("sample.txt", "r") as f:
    indexer = Indexer(BigramParser)
    for l in f:
        res = indexer.update_index(l.strip())
        break
