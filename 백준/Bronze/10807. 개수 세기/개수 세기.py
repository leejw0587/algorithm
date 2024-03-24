N = int(input())
numList = list(map(int, input().split()))
targetNum = int(input())

count = 0

for i in range(N):
    if numList[i] == targetNum:
        count += 1
        
print(count)