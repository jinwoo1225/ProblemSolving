import re

oper = input()
expression = re.split(r'(\D)', oper)
new_expression = ""
for x in expression:
    if x.isdecimal():
        new_expression += str(int(x))
    else:
        new_expression += x

minus_only = new_expression.split('-')

answer = eval(minus_only[0])

for x in minus_only[1:]:
    answer -= eval(x)

print(answer)




# 055-50+40