from collections import deque
from typing import Tuple

N = int(input())
# 2 <= N <= 20

maps_temp = []

DY = [-1, 0, 1, 0]
DX = [0, -1, 0, 1]


class Nemo:
    def __init__(self, y: int, x: int, maps: list, N: int):
        self.x: int = x
        self.y: int = y
        self.size: int = 2
        self.maps: list = maps
        self.N: int = N
        self.eaten = 0

        self.maps[y][x] = 0

    def checkPrey(self)-> list:
        visited = [[False for _ in range(self.N)] for _ in range(self.N)]
        queue = deque([[0, self.y, self.x]])
        preys = []
        # BFS
        while queue:
            _d, _y, _x = queue.popleft()

            if 0 < self.maps[_y][_x] < self.size:
                preys.append([_d, _y, _x])

            if not visited[_y][_x]:
                visited[_y][_x] = True
                for t in range(4):
                    if 0 <= _y + DY[t] < self.N and 0 <= _x + DX[t] < self.N \
                            and self.maps[_y + DY[t]][_x + DX[t]] <= self.size:
                        queue.append([_d + 1, _y + DY[t], _x + DX[t]])

        if preys:
            preys.sort(key=lambda x: (x[0], x[1], x[2]))
            return preys[0]
        else:
            # if nothing to return, return (-1,-1,-1) to stop
            return [-1, -1, -1]

    # eat prey
    def eatPrey(self, y: int, x: int)->None:

        # update nemo y,x
        self.y = y
        self.x = x
        # eaten prey is 0
        self.maps[y][x] = 0
        # eaten += 1
        self.eaten += 1
        # if eaten is same as size, update size
        if self.eaten == self.size:
            self.size += 1
            self.eaten = 0


for _ in range(N):
    maps_temp.append(list(map(int, input().split())))

nemo: Nemo

# finding nemo
for NY in range(N):
    for NX in range(N):
        if maps_temp[NY][NX] == 9:
            nemo = Nemo(NY, NX, maps_temp, N)

time = 0
while True:
    distance, _y, _x = nemo.checkPrey()
    if _y == -1:
        break

    time += distance
    nemo.eatPrey(_y, _x)
    # print("=" * 20, nemo.size, nemo.eaten, nemo.y, nemo.x, time)
    # for part in nemo.maps:
    #     print(part)

print(time)
