class Lane(object):
    def __init__(self, id, length):
        self.__id = id
        self.__length = length

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    def __str__(self):
        return f"Lane ID: {self.id}, length: {self.length}"

    def __repr__(self):
        return self.__str__()