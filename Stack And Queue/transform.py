n = int(input())

for i in range(n):
    a = list(input())
    rpn = ""
    s = []
    for j in range(len(a)):
        if (a[j].isalpha()):
            rpn += a[j]
        elif (a[j].isalpha() == False and a[j] != '(' and a[j] != ')'):
            s.append(a[j])
        elif (a[j] == ')'):
            rpn += s.pop()
    print(rpn)

