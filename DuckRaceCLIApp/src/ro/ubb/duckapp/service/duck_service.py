from ro.ubb.duckapp.domain.duck_entity import Duck

class DuckService:
    def __init__(self, duck_repository):
        self.__duck_repository = duck_repository

    @property
    def duck_repository(self):
        return self.__duck_repository

    def find_duck_by_id(self, id):
        return self.duck_repository.find_by_id(id)

    def get_ducks(self):
        return self.duck_repository.find_all()

    def remove_duck(self, id):
        self.duck_repository.delete_by_id(id)

    def add_duck(self, duck_id, resistance, speed):
        duck = Duck(duck_id, resistance, speed)
        self.duck_repository.save(duck)

    def update_duck(self, duck_id, resistance, speed):
        duck = Duck(duck_id, resistance, speed)
        self.duck_repository.update(duck)