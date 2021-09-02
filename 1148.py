from collections import Counter
from functools import reduce
from sys import stdin

input = stdin.readline

words = []
puzzles = []
while True:
    word: str = input().strip()
    if word == '-':
        break
    words.append(word)

while True:
    puzzle = input().strip()
    if puzzle == '#':
        break
    puzzles.append(list(puzzle))

for puzzle in puzzles:
    puzzle_count = Counter(puzzle)


    def subtract(x: str) -> Counter:
        p = puzzle_count.copy()
        p.subtract(Counter(list(x)))
        return p


    matching_words = list(filter(lambda x: all(map(lambda y: y >= 0, subtract(x).values())), words))


    def count_word(x: str) -> dict:
        count = 0
        for y in matching_words:
            if x in y:
                count += 1
        return {x: count}


    def update(x, y) -> Counter:
        x.update(y)
        return x


    counted: Counter = reduce(update, map(count_word, puzzle_count.keys()), Counter())

    max_count = max(counted.values())
    min_count = min(counted.values())

    max_char = "".join(sorted(map(lambda x: x[0], filter(lambda x: x[1] == max_count, counted.items()))))
    min_char = "".join(sorted(map(lambda x: x[0], filter(lambda x: x[1] == min_count, counted.items()))))

    print(f"{min_char} {min_count} {max_char} {max_count}")
