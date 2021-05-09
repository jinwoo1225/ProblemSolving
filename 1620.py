import sys
N, M = map(int, input().split())

name_dict = {}
numb_dict = {}

pokemons = []
for _ in range(N):
    pokemons.append(sys.stdin.readline().strip())

for index, pokemon in enumerate(pokemons):
    name_dict[pokemon] = index + 1
    numb_dict[index + 1] = pokemon


querys = []
for _ in range(M):
    querys.append(sys.stdin.readline().strip())

for query in querys:
    if query.isnumeric():
        print(numb_dict[int(query)])
    else:
        print(name_dict[query])
