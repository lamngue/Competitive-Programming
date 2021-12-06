t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    s = set(l)
    if len(s) > x:
        print("Average")
    elif len(s) == x:
        print("Good")
    else:
        print("Bad")
