'''
target = 10
positions
[4, 1, 0, 7]

speeds
[2, 2, 1, 1]

positions
0 1 4 7
speeds
1 2 2 1
times
10 4.5 3 3

target = 10
positions
3 4 5 6 7 8
speeds
4 4 4 4 4 4
times
1.75 1.5 1.25 1 0.75 0.5

'''
class Solution:
    # Neetcode solution
    # re-organize the inputs by grouping the position and speeds together as array of tuples
    # sort by ascending starting position (nlogn assuming merge sort is used)
    # process the car fleet from right to left to ensure cars that could become a part of the
    # fleet get merged together (if it is done left to right, the issue is that we don't know if
    # car ahead of us got already merged with another car that's also ahead of it)
    # merge logic --> if time to reach destination for car A <= time to reach destination for car B
    # and car B's starting position is ahead of car A's starting position, merge car A into car B's fleet
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # tuple (starting position, speed, and time to destination)
        cars = []
        for i in range(len(position)):
            # measured in hours
            destinationTime = (target - position[i]) / speed[i]
            cars.append((position[i], speed[i], destinationTime))

        # In python, it will sort by the first entry in the tuple which is the starting position
        # of each car in ascending order (starting positions are unique)
        cars.sort()

        # right to left
        i = len(cars) - 1
        carStack = []
        while i >= 0:
            carStack.append(cars[i])
            
            if len(carStack) > 1:
                # remove the car we just placed on the stack that will reach the destination faster than the one that started ahead of it
                if carStack[-2][2] >= carStack[-1][2]:
                    carStack.pop()

            i -= 1

        carFleetCount = len(carStack)
        return carFleetCount