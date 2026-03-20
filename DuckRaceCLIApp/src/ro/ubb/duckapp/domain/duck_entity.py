class Duck(object):
    def __init__(self, id, speed, resistance):
        self.__id = id
        self.__resistance = resistance
        self.__speed = speed

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def resistance(self):
        return self.__resistance

    @resistance.setter
    def resistance(self, value):
        self.__resistance = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    def __str__(self):
        return f"Duck id: {self.id}, Resistence: {self.resistance}, Speed: {self.speed}"

    def __repr__(self):
        return self.__str__()