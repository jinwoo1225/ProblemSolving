formula = input()

operators_hi = {'*', '/'}
operators_lo = {'+', '-'}
bracket = {'(', ')'}

operators = operators_hi | operators_lo | bracket

stack = []
answer = ""
for w in formula:
    if w not in operators:
        answer += w
    else:
        # can be + - * / ( )
        if w == '(':
            stack.append(w)
        elif w == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()  # (
        elif w in operators_lo:
            while stack and stack[-1] in operators_lo | operators_hi:
                answer += stack.pop()
            stack.append(w)
        elif w in operators_hi:
            while stack and stack[-1] in operators_hi:
                answer += stack.pop()
            stack.append(w)

print(answer + "".join(reversed(stack)))
