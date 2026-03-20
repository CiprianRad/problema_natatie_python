from ro.ubb.duckapp.domain.validators import DuckAppException


class RepositoryException(DuckAppException):
    pass

class Repository():
    def __init__(self, validator):
        self.__all_entities = {}
        self.__validator = validator

    @property
    def all_entities(self):
        return self.__all_entities

    def find_by_id(self, id):
        if id in self.all_entities.keys():
            return self.all_entities[id]
        return None

    def find_all(self):
        return list(self.all_entities.values())

    def delete_by_id(self, id):
        if self.find_by_id(id) is None:
            raise RepositoryException("Entity with this id does not exist.")
        else:
            del self.all_entities[id]

    def save(self, entity):
        self.__validator.validate(entity)
        if self.find_by_id(entity.id) is not None:
            raise RepositoryException("Entity with this id already exists.")
        self.__all_entities[entity.id] = entity

    def update(self, entity):
        self.__validator.validate(entity)
        if self.find_by_id(entity.id) is None:
            raise RepositoryException("Entity with this id does not exist.")
        self.__all_entities[entity.id] = entity
