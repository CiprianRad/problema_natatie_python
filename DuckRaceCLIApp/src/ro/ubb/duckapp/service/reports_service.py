from itertools import combinations, islice


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



    def __get_all_ducks(self):
        return {duck.id: duck for duck in self.duck_repository.find_all()}

    def __get_all_lanes(self):
        return {lane.id: lane for lane in self.lane_repository.find_all()}


    def __valid_pairing(self, pairing):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        for i in range(len(pairing) - 1):
            duck1, lane1 = pairing[i]
            duck2, lane2 = pairing[i + 1]

            if ducks[duck1].resistance > ducks[duck2].resistance and lanes[lane1].length <= lanes[lane2].length:
                return False
        return True



    def find_valid_pairings(self, limit=100):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        
        duck_ids = sorted(ducks.keys(), key=lambda d: ducks[d].resistance)
        lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l].length)

        combo_generator = combinations(duck_ids, len(lane_ids))

        # islice will stop the loop exactly when it hits the limit
        for combo in islice(combo_generator, limit):
            yield list(zip(combo, lane_ids))


    def __calculate_max_time(self, pairing):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        return max((2 * lanes[lane].length) / ducks[duck].speed for duck, lane in pairing)


def find_best_pairing(self):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()

        duck_ids = sorted(ducks.keys(), key=lambda d: ducks[d].resistance)
        lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l].length)

        N = len(duck_ids)
        M = len(lane_ids)

        if N < M:
            return None  # Impossible to pair if there are fewer ducks than lanes

        # dp[i][j] holds the minimum maximum-time using the first 'i' ducks for 'j' lanes.
        dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 0  # 0 lanes cost 0 time

        # Keep track of choices so we can reconstruct the actual pair later
        choice = [[False] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                duck = ducks[duck_ids[i - 1]]
                lane = lanes[lane_ids[j - 1]]

                # Calculate time for this specific duck on this specific lane
                current_time = (2 * lane.length) / duck.speed

                # Option 1: Don't use this duck, carry over best time from previous ducks
                skip_time = dp[i - 1][j]

                # Option 2: Use this duck. The new max time is the highest between 
                # the current run and the maximum of the previous lanes.
                use_time = max(dp[i - 1][j - 1], current_time)

                if use_time < skip_time:
                    dp[i][j] = use_time
                    choice[i][j] = True
                else:
                    dp[i][j] = skip_time
                    choice[i][j] = False

        # Backtrack to build the final list of (duck_id, lane_id) pairs
        best_pairing = []
        curr_i, curr_j = N, M
        
        while curr_j > 0 and curr_i > 0:
            if choice[curr_i][curr_j]:
                best_pairing.append((duck_ids[curr_i - 1], lane_ids[curr_j - 1]))
                curr_j -= 1
                curr_i -= 1
            else:
                curr_i -= 1

        best_pairing.reverse()
        return best_pairing





    def find_best_time(self, pairing):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()
        minimum_time = float('inf')
        times = [(2 * lanes[lane].length) / ducks[duck].speed for duck, lane in pairing]
        max_time = max(times)
        minimum_time = min(max_time, minimum_time)
        print(f"Best time is: : {minimum_time:.6f}")


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

        print(f"Minimum time : {minimum_time:.6f}")


#non-modular form of the problem:

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


    def schema(self):
        ducks = self.__get_all_ducks()
        lanes = self.__get_all_lanes()

        duck_ids = sorted(ducks.keys(), key=lambda d: (ducks[d].resistance, ducks[d].speed))
        lane_ids = sorted(lanes.keys(), key=lambda l: lanes[l].length)

        M = len(lane_ids)
        N = len(duck_ids)
        times = [0] * M


        for j in range(N):
            if j < M:
                duck_id = duck_ids[j]
                lane_id = lane_ids[j]
                time = lanes[lane_id].length / ducks[duck_id].speed

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
                duck_id = duck_ids[j]
                lane_id = lane_ids[i]
                time = lanes[lane_id].length / ducks[duck_id].speed

                if i > 0 and times[i - 1] > time:
                    time = times[i - 1]

                if time < times[i]:
                    times[i] = time

        print(f"Minimum time (Monti Version) is: {(times[M - 1]) * 2}")



