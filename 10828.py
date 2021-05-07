N = int(input())

stack = []
commands = []
for _ in range(N):
    commands.append(input().split())

for command in commands:
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else :
            print(-1)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)


