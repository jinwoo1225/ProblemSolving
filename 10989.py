
N = int(input())
list = [0] * 10001
comm = []
for i in range(N):
    comm.append(int(input()))


for i in comm:
    list[i] += 1


for index in range(1,10001):
    for j in range(list[index]):
        print(index)