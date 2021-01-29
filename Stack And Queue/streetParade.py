while True:
    n = int(input())
    if n == 0:
        break;
    a = list(map(int,input().split()))
    sort = list(a)
    sort.sort()
    flag = True
    count = 1
    s = []
    for j in range(len(a)):
        if (a[j] == count):
            count += 1
        else:
            if len(s) == 0 or s[-1] > a[j]:
                s.append(a[j])
            elif(s[-1] < a[j]):
                flag = False
        while (len(s) > 0 and s[-1] == count):
            s.pop()
            count += 1
    if (flag):
        print("yes")
    else:
        print("no")
    
