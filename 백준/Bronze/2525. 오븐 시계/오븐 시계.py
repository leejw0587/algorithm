h, m = map(int, input().split())
time = int(input())

resm = m + time
resh = h
while resm >= 60:
    resh = resh + 1
    resm = resm - 60
    
    if resh >= 24:
        resh = resh - 24


print(resh,resm)