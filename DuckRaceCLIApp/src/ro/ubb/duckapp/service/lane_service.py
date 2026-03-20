from ro.ubb.duckapp.domain.lane_entity import Lane


class LaneService():
    def __init__(self, lane_repository):
        self.__lane_repository = lane_repository

    @property
    def lane_repository(self):
        return self.__lane_repository

    def find_lane_by_id(self, lane_id):
        return self.lane_repository.find_by_id(lane_id)

    def get_lanes(self):
        return self.lane_repository.find_all()

    def remove_lane(self, lane_id):
        return self.lane_repository.delete_by_id(lane_id)

    def add_lane(self, lane_id, length):
        lane = Lane(lane_id, length)
        self.lane_repository.save(lane)

    def update_lane(self, lane_id, length):
        lane = Lane(lane_id, length)
        self.lane_repository.update(lane)