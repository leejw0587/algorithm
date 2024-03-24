N = int(input())

list = list(map(int, input().split()))

M = max(list)
m = min(list)

print(f"{m} {M}")
