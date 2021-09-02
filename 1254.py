word = input()

# abcdd     5
# abcdd deba 5 + 4
for i in range(len(word)):
    if word[i:] == word[i:][::-1]:
        # 길이 + i
        print(len(word) + i)
        break
