s = input()
s1 = list(s[:len(s)])
t = input()
t1 = list(t[:len(t)])

def findSmallerString(s, t):
    mask = "abcdefghijklmnopqrstuvwxyz"
    h = list(s)
    g = list(t)
    final = []
    totalS = 0
    totalT = 0
    for i in range(len(s)):
        totalS += mask.find(s[i])
        totalT += mask.find(t[i])
    if (totalT - totalS == 1 and abs(mask.find(h[len(h)-1]) - mask.find(g[len(g)-1])) == 1):
        return "No such string"
    else:
        if (chr(ord(h[len(h)-1]) + 1).isalpha()):
            h[len(h) - 1] = chr(ord(h[len(h)-1]) + 1)
            final = h
        else:
            g[len(g) - 1] = chr(ord(g[len(g)-1]) - 1)
            final = g
    return "".join(final)
            

print(findSmallerString(s1,t1))
