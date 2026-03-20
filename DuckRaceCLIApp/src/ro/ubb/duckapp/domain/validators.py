from abc import abstractmethod

from ro.ubb.duckapp.domain.duck_entity import Duck
from ro.ubb.duckapp.domain.lane_entity import Lane


class DuckAppException(Exception):
    pass

class ValidatorException(DuckAppException):
    pass

class EntityValidator:
    @abstractmethod
    def validate(self, entity):
        pass


class BaseEntityValidator(EntityValidator):
    def validate(self, entity):
        entity_id = entity.id
        if isinstance(entity_id, tuple):
            if not all(isinstance(id_part, int) and id_part >= 0 for id_part in entity_id):
                raise ValidatorException("All IDs in the tuple must be positive integers")
        else:
            if not isinstance(entity_id, int) or entity_id < 0:
                raise ValidatorException("ID must be a positive integer")


class DuckValidator(EntityValidator):
    def validate(self, duck):
        if not isinstance(duck, Duck):
            raise ValidatorException("Duck must be a Duck object")
        super().validate(duck)
        if not isinstance(duck.speed, int) or duck.speed <= 0:
            raise ValidatorException("Speed must be a positive integer")
        if not isinstance(duck.resistance, int) or duck.resistance <= 0:
            raise ValidatorException("Resistance must be a positive integer")

class LaneValidator(EntityValidator):
    def validate(self, lane):
        if not isinstance(lane, Lane):
            raise ValidatorException("Lane must be a Lane object")
        super().validate(lane)
        if not isinstance(lane.length, int) or lane.length <= 0:
            raise ValidatorException("Length must be a positive integer")