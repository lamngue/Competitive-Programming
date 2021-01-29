s = input()
name = list(s[:len(s)])

def museum(s):
    mask = "abcdefghijklmnopqrstuvwxyz"
    rotation = 0
    current = 'a'
    #['z','e','u','s']
    for i in range(len(s)):
        dist = abs(mask.find(current) - mask.find(s[i]))
        opt = min(26-dist, dist)
        rotation += opt
        current = s[i]
   
    return rotation
    
print(museum(name))
