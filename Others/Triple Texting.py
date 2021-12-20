s = input()
n = len(s) // 3
first = 0
second = first + n
third = first + 2*n
out = ''
while first < n:
    if (s[first] == s[second] and s[second] == s[third]):
        out += s[first]
    elif (s[first] == s[second] and s[second] != s[third]):
        out += s[first]
    elif (s[first] != s[second] and s[second] == s[third]):
        out += s[second]
    elif (s[first] == s[third] and s[second] != s[third]):
        out += s[first]
    first += 1
    second += 1
    third += 1
print(out)
    
