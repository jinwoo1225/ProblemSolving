N = int(input())

pic = []

for _ in range(N):
    pic.append(input())




def DFS(y: int, x: int, color: str) -> None:
    global N
    if visited[y][x]:
        return

    stack = [[y, x]]

    while stack:
        new_y, new_x = stack.pop()
        if new_y >= N or new_y < 0 or new_x >= N or new_x < 0:
            continue
        if visited[new_y][new_x]:
            continue
        if not pic[new_y][new_x] == color:
            continue
        visited[new_y][new_x] = True
        stack.append([new_y + 1, new_x])
        stack.append([new_y, new_x + 1])
        stack.append([new_y - 1, new_x])
        stack.append([new_y, new_x - 1])


RGB = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            DFS(y,x , 'R')
            DFS(y,x , 'G')
            DFS(y,x , 'B')
            RGB += 1

for y in range(N):
    pic[y] = pic[y].replace('G', 'R')


RB = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            DFS(y,x,'R')
            DFS(y,x,'B')
            RB += 1

print(RGB, RB)
