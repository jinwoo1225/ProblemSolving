input()
from collections import Counter
cards = Counter(map(int, input().split()))
input()
for search in list(map(int, input().split())):
    print(cards[search], end=' ')
