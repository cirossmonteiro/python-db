import pickle

import avl

class Document:
    def __init__(self, obj: dict):
        self.obj = obj
    
    def __eq__(self, other):
        return self.obj == other.obj
    
MAP_OPERATORS = {
    "eq": "==",
    "ne": "!=",
    "lt": "<",
    "le": "<=",
    "gt": ">",
    "ge": ">="
}

def fix_query(query: dict):
    for field, value in query.items():
        if type(value) == str:
            if value[0] != "$":
                value = {
                    "$eq": value
                }
        else:
            value = {
                "$eq": value
            }
        query[field] = value
    return query

def condition(document, field, op, v):
    op = MAP_OPERATORS[op[1:3]]
    if type(v) == str and v[0] == "$":
        v = document[v[1:]]
    return eval(f"{document[field]}{op}{v}")


class Index:
    tree = avl.AVLTree()
    def __init__(self, field: str):
        self.field = field

class Collection:
    documents = []
    indexes = []
    def __init__(self, name: str):
        self.name = name
    
    def insert(self, obj: dict):
        self.documents.append(Document(obj))

    def find(self, query: dict):
        # to-do: use project: dict
        # to-do: convert non-$eq to $eq: [a,b]
        if len(query):
            return self.documents

        result = []
        for field, value in fix_query(query).items():
            for index in self.indexes:
                if index.field == field:
                    pass
            else:
                for document in self.documents:
                    for op, v in value.items():
                        if condition(document, field, op, v):
                            result.append(document)

    def __eq__(self, other):
        if self.name == other.name and len(self.documents) == len(other.documents):
            for self_document, other_document in zip(self.documents, other.documents):
                if self_document != other_document:
                    return False
        else:
            return False

        return True

class Database:
    collections = []
    def __init__(self, name: str):
        self.name = name
    
    def create_collection(self, name: str):
        self.collections.append(Collection(name))
    
    def dump(self):
        with open(f"{self.name}.dump", "wb") as fh:
            pickle.dump(self, fh)
    
    def load(self, filename=None):
        with open(f"{self.name}.dump" if filename is None else filename, "rb") as fh:
            self = pickle.load(fh)

    def __eq__(self, other):
        if self.name == other.name and len(self.collections) == len(other.collections):
            for self_col, other_col in zip(self.collections, other.collections):
                if self_col != other_col:
                    return False
        else:
            return False

        return True