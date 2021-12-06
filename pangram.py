n = int(input())

s = input()
dic = {}
for i in range(n):
    k = s[i].lower()
    if (k in dic):
        dic[k] += 1
    else:
        dic[k] = 1
if (len(dic) >= 26):
    print("YES")
else:
    print("NO")
