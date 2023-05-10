import pickle

class Document:
    def __init__(self, obj: dict):
        self.obj = obj
    
    def __eq__(self, other):
        return self.obj == other.obj

class Collection:
    documents = []
    def __init__(self, name: str):
        self.name = name
    
    def insert(self, obj: dict):
        self.documents.append(Document(obj))

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