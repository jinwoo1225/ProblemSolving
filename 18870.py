from sys import stdin

N = int(stdin.readline().strip())

coords = list(map(int, stdin.readline().split()))
coords_dict = {}
for index, key in enumerate(sorted(list(set(coords)))):
    coords_dict[key] = index


for coord in coords:
    print(coords_dict[coord], end=' ')