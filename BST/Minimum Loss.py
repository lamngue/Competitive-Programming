n = int(input())
prices = list(map(int, input().split()))
dic = {}
loss = max(prices)
for i in range(n):
    dic[prices[i]] = i
prices.sort()
for i in range(1, n):
    l = prices[i] - prices[i-1]
    if (l >= 0 and dic[prices[i]] < dic[prices[i-1]]):
        loss = min(loss, l)
print(loss)

