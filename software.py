class Software:
    def __init__(self, name, producer, keys, _id=None):
        if _id is not None:
            self._id = _id
        self.name = name
        self.producer = producer
        self.keys = keys

    def get_id(self):
        return str(self._id)
