C = int(input())

for i in range(C):
    num = list(map(int, input().split()))
    avr = sum(num[1:]) / num[0]
    count = 0
    for score in num[1:]:
        if score > avr:
            count += 1
    rate = count/num[0] * 100
    print(f"{rate:.3f}%")