class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_of_each_car = []

        for i in range(len(position)):
            time_i = (target-position[i])/speed[i]
            time_of_each_car.append((position[i], time_i))

        fleet = []
        time_of_each_car.sort(reverse=True)
        # curr = float("inf")
        for position, time in time_of_each_car:
            if not fleet or time > fleet[-1]:
                fleet.append(time)

        print(len(fleet))
        print(time_of_each_car)
        return len(fleet)