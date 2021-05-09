import sys
from collections import deque

input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    func = input().strip()
    size = int(input().strip())
    arr = deque()
    if size:
        arr = deque(map(int, input().lstrip('[').rstrip(']\n').split(',')))
    else:
        input()

    func = func.replace('RR', "")
    if func.count('D') > len(arr) or (func.count('D') > 0 and not arr):
        print('error')
        continue

    flag = 'normal'
    for cmd in func:
        if cmd == 'R':
            flag = 'reverse' if flag == 'normal' else 'normal'
        elif cmd == 'D':
            if flag == 'normal':
                arr.popleft()
            else:
                arr.pop()

    if flag == 'reverse':
        arr.reverse()

    print(str(list(arr)).replace(" ", ""))


"""    
4
RDD
4
[1,2,3,4]
DD
1
[42]
DDDD
0
[]
RRRR
0
[]
RRD
6
[1,1,2,3,5,8]



1
RRDDDDDRRRRRDRDDDRRRRRDRRDRRRR
18
[65,14,87,67,55,58,23,51,85,41,69,25,31,63,70,64,59,21]

1
DDDD
3
[1,2,3]

1
D
1
[1]
"""
