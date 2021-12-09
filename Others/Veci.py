import sys
largest = 0
x = str(input())
arr = [str(i) for i in list(str(x))]
n = len(arr)
out = []

#Heap's Algorithm
def permute(arr, size):
    if size == 1:
        out.append(arr.copy())
        return
    else:
        permute(arr, size-1)
        for i in range(size-1):
            if size % 2 == 0:
                arr[i], arr[size-1] = arr[size-1], arr[i]
            else:
                arr[0], arr[size-1] = arr[size-1], arr[0]
            permute(arr, size-1)
minEl = sys.maxsize
permute(arr, n)
for i in out:
    sub = int(''.join(i)) - int(x)
    if sub < minEl and sub > 0:
        minEl = sub
        
if minEl < sys.maxsize:
    print(minEl + int(x))
else:
    print(0)
