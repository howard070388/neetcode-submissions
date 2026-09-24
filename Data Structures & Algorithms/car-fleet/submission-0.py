class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            car.append((position[i], time))
        car.sort()
        fleet = [car[-1][1]]
        while len(car) >= 2:
            if car[-2][1] <= car[-1][1]:
                car.pop(-2)
            else:
                car.pop(-1)
                fleet.append(car[-1][1])
        return len(fleet)
