while True:
    s = input().rstrip(".")
    if s == "":
        break
    ans = True
    stack = []

    for i in range(len(s)):
        if '(' == s[i] or '[' == s[i]:
            stack.append(s[i])
        elif ')' == s[i]:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    ans = False
                    break
            else:
                ans = False
                break
        elif ']' == s[i]:
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    ans = False
                    break
            else:
                ans = False
                break

    if stack:
        ans = False

    print("yes" if ans else "no")
