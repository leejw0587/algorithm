h, m, s = map(int, input().split())
time_s = int(input())

res_s = s + time_s
res_m = m
res_h = h

while res_s >= 60:
    res_m = res_m + 1
    res_s = res_s - 60

    if res_m >= 60:
        res_h = res_h + 1
        res_m = res_m - 60

    if res_h >= 24:
        res_h = res_h - 24

print(res_h,res_m,res_s)