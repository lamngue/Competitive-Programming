a, b, c, d = map(int, input().split())
p, m, g = map(int, input().split())

#0,4,8,12,16,...;2,6,10,14,18,...
#0,6,12,18,24,...;3,9,15,21,27,...
period1 = a + b
period2 = c + d

def count_dog(time):
    cnt = 0

    if (time % period1 != 0 and time % period1 <= a):
        cnt += 1
    if (time % period2 != 0 and time % period2 <= c):
        cnt += 1
    if(cnt == 0):
        print("none")
    elif (cnt == 1):
        print("one")
    else:
        print("both")

count_dog(p)
count_dog(m)
count_dog(g)
