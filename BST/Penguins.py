n = int(input())
dic = {"Emperor Penguin": 0, "Little Penguin": 1, "Macaroni Penguin": 2}
dic_rev = {0: "Emperor Penguin", 1: "Little Penguin", 2: "Macaroni Penguin"}
count = [0 for i in range(3)]
for i in range(n):
    p = input()
    count[dic[p]] += 1

print(dic_rev[count.index(max(count))])
