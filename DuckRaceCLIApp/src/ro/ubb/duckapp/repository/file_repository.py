from ro.ubb.duckapp.domain.duck_entity import Duck
from ro.ubb.duckapp.domain.lane_entity import Lane
from ro.ubb.duckapp.domain.validators import DuckAppException, DuckValidator, LaneValidator
from ro.ubb.duckapp.repository.generic_repository import Repository
import tempfile
import shutil

class FileRepositoryException(DuckAppException):
    pass


class FileRepository(Repository):
    def __init__(self, entity_validator, file_name):
        super().__init__(entity_validator)
        self.__file_name = file_name
        self.__entity_validator = entity_validator
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name, 'r') as file:
            lines = file.readlines()

        # Parse first line
        n, m = map(int, lines[0].strip().split())

        # Parse subsequent lines
        speed_values = list(map(int, lines[1].strip().split()))
        resistance_values = list(map(int, lines[2].strip().split()))
        length_values = list(map(int, lines[3].strip().split()))

        if len(speed_values) != n or len(resistance_values) != n:
            raise FileRepositoryException("Mismatch between number of ducks and provided attributes.")
        if len(length_values) != m:
            raise FileRepositoryException("Mismatch between number of lanes and provided lengths.")

        if isinstance(self.__entity_validator, DuckValidator):
            for i in range(n):
                duck = Duck(int(i+1), speed_values[i], resistance_values[i])
                super().save(duck)

        if isinstance(self.__entity_validator, LaneValidator):
            for i in range(m):
                lane = Lane(int(i+1), length_values[i])
                super().save(lane)

    def save(self, entity):
        super().save(entity)
        with open(self.__file_name, "r") as file, tempfile.NamedTemporaryFile("w", delete = False) as temp_file:
            lines = file.readlines()

            #make sure the number of lines is always 4, to not get error in case of an empty file, etc.
            while len(lines) < 4:
                lines.append("")
            # number_ducks, number_lanes  = map(int, lines[0].strip().split())
            # line1_values = lines[0].strip().split()
            # line2_values = lines[1].strip().split()
            # line3_values = lines[2].strip().split()
            # line4_values = lines[3].strip().split()
            line1_values = lines[0].strip().split() if lines[0].strip() else ["0", "0"]
            line2_values = lines[1].strip().split() if len(lines) > 1 and lines[1].strip() else []
            line3_values = lines[2].strip().split() if len(lines) > 2 and lines[2].strip() else []
            line4_values = lines[3].strip().split() if len(lines) > 3 and lines[3].strip() else []
            number_ducks, number_lanes = map(int, lines[0].strip().split())

            #per case: duck
            if isinstance(entity, Duck):
                number_ducks = number_ducks + 1
                # line1_values[0] = f"{number_ducks}"
                line1_values[0] = str(number_ducks)
                line2_values.append(str(entity.speed))
                line3_values.append(str(entity.resistance))
            #per case: lane
            if isinstance(entity, Lane):
                number_lanes = number_lanes + 1
                # line1_values[1] = f"{number_lanes}"
                line1_values[1] = str(number_lanes)
                line4_values.append(str(entity.length))

            #Part of code that deal with writing the new lines to file
            temp_file.write(" ".join(line1_values)+ "\n")
            temp_file.write(" ".join(line2_values)+ "\n")
            temp_file.write(" ".join(line3_values)+ "\n")
            temp_file.write(" ".join(line4_values)+ "\n")
        shutil.move(temp_file.name, self.__file_name)




#TODO: Try to improve the app by not allowing the user to give id by hand, but instead when saving an entity, set the id to be the length of the enityt list + 1
