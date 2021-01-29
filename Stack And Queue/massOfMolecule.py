c = list(input())

dic = {'C':12,'H':1,'O':16}
s = []
t = 0
for i in range(len(c)):
    temp = 0 #value in parentheses
    if c[i] == "(":
        s.append(c[i])
    elif c[i].isalpha():
        s.append(dic[c[i]])
    elif c[i].isnumeric(): #if found a number
        s[len(s)-1] = s[len(s)-1] * int(c[i])
    elif c[i] == ")":
        #calculate value in parentheses
        j = len(s) - 1
        while s[j] != "(":
            temp += s.pop()
            j -= 1
        s.pop() # pop the "("
        s.append(temp)
print(sum(s))
