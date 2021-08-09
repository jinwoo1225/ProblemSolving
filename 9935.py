answer: str = input()
target: str = input()

stack: list = []
target_size: int = len(target)

for c in answer:
    stack.append(c)
    if target[-1] == c and "".join(stack[-target_size:]) == target:
        del stack[-target_size]

print("".join(stack) if stack else "FRULA")
