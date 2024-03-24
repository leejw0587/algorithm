t = int(input())
res = 0


i = 1
while i <= t:
    a, b = map(int, input().split())
    res = a + b
    print("Case #{}: {}".format(i, res))
    i = i+1

