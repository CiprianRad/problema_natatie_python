from itertools import combinations


class ReportsService(object):
    def __init__(self, duck_repository, lane_repository):
        self.__duck_repository = duck_repository
        self.__lane_repository = lane_repository

    @property
    def duck_repository(self):
        return self.__duck_repository

    @duck_repository.setter
    def duck_repository(self, value):
        self.__duck_repository = value

    @property
    def lane_repository(self):
        return self.__lane_repository

    @lane_repository.setter
    def lane_repository(self, value):
        self.__lane_repository = value

    @staticmethod
    def permutations(iterable, r=None):
        items = tuple(iterable)
        r = len(items) if r is None else r

        if r == 0:
            yield ()
            return

        for i, item in enumerate(items):
            rest = items[:i] + items[i + 1:]
            for perm in ReportsService.permutations(rest, r - 1):
                yield (item,) + perm



                #to simplify the writing in the module
    # def __get_all_ducks(self):
    #     return self.__duck_repository.find_all()
    #
    # def __get_all_lanes(self):
    #     return self.__lane_repository.find_all()



    def __get_all_ducks(self):
        return {duck.id: duck for duck in self.duck_repository.find_all()}

    def __get_all_lanes(self):
        return {lane.id: lane for lane in self.lane_repository.find_all()}



    # def valid_pairing(ducks, lanes, pairing):
    #     # Check if the pairing respects the resistance-lane length condition
    #     for i in range(len(pairing) - 1):
    #         duck1, lane1 = pairing[i]
    #         duck2, lane2 = pairing[i + 1]
    #
    #         if ducks[duck1][0] > ducks[duck2][0] and lanes[lane1] <= lanes[lane2]:
    #             return False  # Invalid pairing
    #     return True

    def __valid_pairing(self, pairing):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        for i in range(len(pairing) - 1):
            duck1, lane1 = pairing[i]
            duck2, lane2 = pairing[i + 1]

            if ducks[duck1].resistance > ducks[duck2].resistance and lanes[lane1].length <= lanes[lane2].length:
                return False
        return True

    # def find_valid_pairings(ducks, lanes):
    #     duck_ids = sorted(ducks.keys(), key=lambda d: ducks[d][0])  # Sort by resistance
    #     lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l])  # Sorted by length
    #
    #     all_permutations = permutations(duck_ids, len(lane_ids))  # Assign ducks to lanes
    #     valid_pairings = []
    #
    #     for perm in all_permutations:
    #         pairing = list(zip(perm, lane_ids))
    #         if valid_pairing(ducks, lanes, pairing):
    #             valid_pairings.append(pairing)
    #
    #     return valid_pairings

    def find_valid_pairings(self):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        # The lines below are for the first version
        # duck_ids = sorted(self.__get_all_duck_ids(), key=lambda d: ducks[d].resistance)
        # lane_ids = sorted(self.__get_all_lane_ids(), key=lambda d: lanes[d].length)
        duck_ids = sorted(ducks.keys(), key=lambda d: ducks[d].resistance)
        lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l].length)

        # all_permutations = ReportsService.permutations(duck_ids, len(lane_ids))
        all_permutations = combinations(duck_ids, len(lane_ids))
        valid_pairings = []

        for perm in all_permutations:
            pairing = list(zip(perm, lane_ids))
            if self.__valid_pairing(pairing):
                valid_pairings.append(pairing)

        return valid_pairings

    # def calculate_max_time(pairing, ducks, lanes):
    #     return max((2 * lanes[lane]) / ducks[duck][1] for duck, lane in pairing)


    def __calculate_max_time(self, pairing):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        return max((2 * lanes[lane].length) / ducks[duck].speed for duck, lane in pairing)

    # def find_best_pairing(valid_pairings, ducks, lanes):
    #     return min(valid_pairings, key=lambda pairing: calculate_max_time(pairing, ducks, lanes))

    def find_best_pairing(self, valid_pairings):
        if not valid_pairings:
            return None
        return min(valid_pairings, key=lambda pairing: self.__calculate_max_time(pairing))





    def find_best_time(self, pairing):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        minimum_time = float('inf')
        times = [(2 * lanes[lane].length) / ducks[duck].speed for duck, lane in pairing]
        max_time = max(times)
        minimum_time = min(max_time, minimum_time)
        print(f"Version 3 (My third method): {minimum_time:.6f}")




    # ducks = {1: (1, 4), 2: (8, 2), 3: (8, 8), 4: (15, 10)}  # duck_id: (resistance, speed)
    # lanes = {1: 6, 2: 8, 3: 9, 4: 10}  # lane_id: length
    #
    # pairings = find_valid_pairings(ducks, lanes)
    # best_pairing = find_best_pairing(pairings, ducks, lanes)
    # print("Best Pairing:", best_pairing)

    def minimum_time(self):
        ducks = self.duck_repository.find_all()
        lanes = self.lane_repository.find_all()

        ducks.sort(key=lambda x: (x.resistance, -x.speed))
        lanes.sort(key=lambda x: x.length)

        minimum_time = float('inf')
        n = len(ducks)
        m = len(lanes)

        for i in range(n - m + 1):
            selected_ducks = ducks[i:i + m]
            times = [(2 * lanes[j].length) / selected_ducks[j].speed for j in range(m)]
            maximum_time = max(times)
            minimum_time = min(minimum_time, maximum_time)

        print(f"Minimum time (My 1st version): {minimum_time:.6f}")


    # N = 5
    # M = 3
    # rate = [(3, 1), (2, 2), (5, 3), (4, 4), (6, 5)]  # (viteza, rezistenta)
    # distante = [10, 20, 30]  # distanțele balizelor
    #
    # rezultat = minim_durata_cursa(N, M, rate, distante)
    # print(f"Durata minimă a cursei: {rezultat:.6f}")



#non-modular form of the problem:

# from itertools import permutations
#
#
# def valid_pairing(ducks, lanes, pairing):
#     # Check if the pairing respects the resistance-lane length condition
#     for i in range(len(pairing) - 1):
#         duck1, lane1 = pairing[i]
#         duck2, lane2 = pairing[i + 1]
#
#         if ducks[duck1][0] > ducks[duck2][0] and lanes[lane1] <= lanes[lane2]:
#             return False  # Invalid pairing
#     return True
#
#
# def find_valid_pairings(ducks, lanes):
#     duck_ids = sorted(ducks.keys(), key=lambda d: ducks[d][0])  # Sort by resistance
#     lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l])  # Sorted by length
#
#     all_permutations = permutations(duck_ids, len(lane_ids))  # Assign ducks to lanes
#     valid_pairings = []
#
#     for perm in all_permutations:
#         pairing = list(zip(perm, lane_ids))
#         if valid_pairing(ducks, lanes, pairing):
#             valid_pairings.append(pairing)
#
#     return valid_pairings
#
#
# # # Testing
# # ducks = {1: (5, 10), 2: (2, 8), 3: (2, 7)}  # duck_id: (resistance, speed)
# # lanes = {1: 3, 2: 7}  # lane_id: length
# #
# # pairings = find_valid_pairings(ducks, lanes)
# # print(pairings)
#
# def calculate_max_time(pairing, ducks, lanes):
#     return max((2 * lanes[lane]) / ducks[duck][1] for duck, lane in pairing)
#
# def find_best_pairing(valid_pairings, ducks, lanes):
#     return min(valid_pairings, key=lambda pairing: calculate_max_time(pairing, ducks, lanes))
#
# ducks = {1: (1, 4), 2: (8, 2), 3: (8, 8), 4: (15, 10)}  # duck_id: (resistance, speed)
# lanes = {1: 6, 2: 8, 3: 9, 4: 10}  # lane_id: length
#
# pairings = find_valid_pairings(ducks, lanes)
# best_pairing = find_best_pairing(pairings, ducks, lanes)
# print("Best Pairing:", best_pairing)
# print(pairings)

    # def schema(self):
    #     ducks = self.__get_all_ducks()
    #     lanes = self.__get_all_lanes()
    #     # The lines below are for the first version
    #     # duck_ids = sorted(self.__get_all_duck_ids(), key=lambda d: ducks[d].resistance)
    #     # lane_ids = sorted(self.__get_all_lane_ids(), key=lambda d: lanes[d].length)
    #     duck_ids = sorted(ducks.keys(), key=lambda d: ducks[d].resistance)
    #     lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l].length)
    #     M = len(lane_ids)
    #     N = len(duck_ids)
    #     times = [0] * M
    #
    #     for j in range(N):
    #         if j < M:
    #             time = lanes[j].length / ducks[j].speed
    #             if j == 0 or times[j - 1] < time:
    #                 times[j] = time
    #             else:
    #                 times[j] = times[j - 1]
    #         upper, lower = j, 0
    #         if M < j:
    #             upper = M
    #         if N - M <= j:
    #             lower = j - N + M
    #         for i in reversed(range(lower, upper)):
    #             time = lanes[i].length / ducks[j].speed
    #             if i > 0 and times[i - 1] > time:
    #                 time = times[i - 1]
    #             if time < times[i]:
    #                 times[i] = time
    #
    #     print(times[M - 1] * 2)

    def schema(self):
        ducks = self.__get_all_ducks()  # Dictionary {duck_id: Duck}
        lanes = self.__get_all_lanes()  # Dictionary {lane_id: Lane}

        # Sort based on resistance and length
        duck_ids = sorted(ducks.keys(), key=lambda d: (ducks[d].resistance, ducks[d].speed))
        lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l].length)

        M = len(lane_ids)
        N = len(duck_ids)
        times = [0] * M

        # print(f"{N} {M}")
        # print(ducks)
        # print(lanes)
        # print(duck_ids)
        # print(lane_ids)

        for j in range(N):
            if j < M:
                duck_id = duck_ids[j]  # Get the actual key
                lane_id = lane_ids[j]  # Get the actual key
                time = lanes[lane_id].length / ducks[duck_id].speed  # Access using the correct keys

                if j == 0 or times[j - 1] < time:
                    times[j] = time
                else:
                    times[j] = times[j - 1]

            upper, lower = j, 0
            if M < j:
                upper = M
            if N - M <= j:
                lower = j - N + M

            for i in reversed(range(lower, upper)):
                duck_id = duck_ids[j]  # Correctly reference duck
                lane_id = lane_ids[i]  # Correctly reference lane
                time = lanes[lane_id].length / ducks[duck_id].speed  # Fix access

                if i > 0 and times[i - 1] > time:
                    time = times[i - 1]

                if time < times[i]:
                    times[i] = time

        print(f"Minimum time (Monti Version) is: {(times[M - 1]) * 2}")



