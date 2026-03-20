import traceback

from ro.ubb.duckapp.domain.validators import ValidatorException
from ro.ubb.duckapp.repository.generic_repository import RepositoryException


class AppConsole(object):
    def __init__(self, duck_service, lane_service, reports_service):
        self.__duck_service = duck_service
        self.__lane_service = lane_service
        self.__reports_service = reports_service

    @property
    def duck_service(self):
        return self.__duck_service

    @duck_service.setter
    def duck_service(self, value):
        self.__duck_service = value

    @property
    def lane_service(self):
        return self.__lane_service

    @lane_service.setter
    def lane_service(self, value):
        self.__lane_service = value

    @property
    def reports_service(self):
        return self.__reports_service

    @reports_service.setter
    def reports_service(self, value):
        self.__reports_service = value

    @staticmethod
    def __show_options():
        print("Welcome to the duck app!")
        print("Choose an option from below:")
        print("1.Add a duck")
        print("2.Update a duck")
        print("3.Delete a duck")
        print("4.Show all ducks")
        print("5.Add a lane")
        print("6.Update a lane")
        print("7.Delete a lane")
        print("8.Show all lanes")
        print("9.Get possible pairs")
        print("10.Get optimal pair")
        print("11.Get optimal timing")
        print("12.Exit")

    def run_menu(self):
        while True:
            self.__show_options()
            try:
                option = input("Enter your option: ")
                if option == "1":
                    self.__ui_add_duck()
                if option == "2":
                    self.__ui_update_duck()
                if option == "3":
                    self.__remove_duck()
                if option == "4":
                    self.__get_all_ducks()
                if option == "5":
                    self.__ui_add_lane()
                if option == "6":
                    self.__ui_update_lane()
                if option == "7":
                    self.__ui_remove_lane()
                if option == "8":
                    self.__ui_get_all_lanes()
                if option == "9":
                    self.__ui_get_possible_pair()
                if option == "10":
                    self.__ui_get_optimal_pair()
                if option == "11":
                    self.__ui_schema()
                if option == "12":
                    break
            except KeyError as e:
                print(f"Option not implemented", e)
                traceback.print_exc()

    def __ui_add_duck(self):
        try:
            duck_id = int(input("Enter duck id: "))
            speed = int(input("Enter speed: "))
            resistance = int(input("Enter resistance: "))
            try:
                self.duck_service.add_duck(duck_id, resistance, speed)
            except RepositoryException as e:
                print(f"Duck with this ID already exists ", e)
                traceback.print_exc()
        except ValidatorException as e:
            print(f"Invalid inputs", e)
            traceback.print_exc()

    def __remove_duck(self):
        try:
            duck_id = int(input("Enter duck id: "))
            try:
                self.duck_service.remove_duck(duck_id)
            except RepositoryException as e:
                print(f"Duck with this ID does not exist ", e)
                traceback.print_exc()
        except ValidatorException as e:
            print(f"ID must be a positive integer", e)

    def __ui_update_duck(self):
            try:
                duck_id = int(input("Enter duck id: "))
                speed = int(input("Enter speed: "))
                resistance = int(input("Enter resistance: "))
                try:
                    self.duck_service.update_duck(duck_id, resistance, speed)
                except RepositoryException as e:
                    print(f"Duck with this ID does not exists ", e)
                    traceback.print_exc()
            except ValidatorException as e:
                print(f"Invalid inputs", e)
                traceback.print_exc()

    def __ui_add_lane(self):
        try:
            lane_id = int(input("Enter lane id: "))
            length = int(input("Enter length: "))
            try:
                self.lane_service.add_lane(lane_id, length)
            except RepositoryException as e:
                print(f"Lane with this ID already exists ", e)
                traceback.print_exc()
        except ValidatorException as e:
            print(f"Invalid inputs", e)
            traceback.print_exc()

    def __ui_update_lane(self):
        try:
            lane_id = int(input("Enter lane id: "))
            length = int(input("Enter length: "))
            try:
                self.lane_service.update_lane(lane_id, length)
            except RepositoryException as e:
                print(f"Lane with this ID does not exist ", e)
                traceback.print_exc()
        except ValidatorException as e:
            print(f"Invalid inputs", e)
            traceback.print_exc()

    def __ui_remove_lane(self):
        try:
            lane_id = int(input("Enter a lane id:"))
            try:
                self.lane_service.remove_lane(lane_id)
            except RepositoryException as e:
                print(f"Lane with this ID does not exist ", e)
                traceback.print_exc()
        except ValidatorException as e:
            print(f"Invalid inputs", e)
            traceback.print_exc()

    def __get_all_ducks(self):
        print(*self.duck_service.get_ducks())

    def __ui_get_all_lanes(self):
        print(*self.lane_service.get_lanes())


    def __ui_get_possible_pair(self):
        print(*self.reports_service.find_valid_pairings())

    def __ui_get_optimal_pair(self):
        valid_pairings = self.reports_service.find_valid_pairings()
        print(f"Best pair is:" , *self.reports_service.find_best_pairing(valid_pairings))

    def __ui_schema(self):
        self.reports_service.schema()
        # self.reports_service.minimum_time()
        # valid_pairings = self.reports_service.find_valid_pairings()
        # optimal_pair = self.reports_service.find_best_pairing(valid_pairings)
        # self.reports_service.find_best_time(optimal_pair)



