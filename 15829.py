input()

sentence = input()
N = 31
M = 1234567891
answer = 0
for index, word in enumerate(sentence):
    answer += ((ord(word) - ord('a') + 1) * pow(31, index, M)) % M

print(answer)
