X = int(input())
N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append(a * b)

if sum(arr) == X:
    print("Yes")
else:
    print("No")
