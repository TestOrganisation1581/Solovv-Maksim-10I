def chet(n):
    ans = 0
    f = False
    for i in n:
        if len(str(i)) == 4:
            ans += 1
        if i % 5 == 0:
            f = True
    return ans == 2 and f and sum(n) > m
f = open("17_13088.txt")
lis = list(map(int, f.readlines()))
m = max(lis, key=lambda x: (x % 17 == 0, x))
ansn = 0
ansm = 0
for i in range(len(lis) - 2):
    if chet([lis[i], lis[i + 1], lis[i + 2]]):
        ansn += 1
        ansm = max(ansm, sum([lis[i], lis[i + 1], lis[i + 2]]))
print(ansn, ansm)