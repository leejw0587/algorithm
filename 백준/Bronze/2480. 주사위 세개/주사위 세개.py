a, b, c = map(int, input().split())
num = [a, b, c]

if(a==b==c):
    print(10000 + a * 1000)

elif(a==b or a==c or b==c):
    if(a==b):
        print(1000 + a * 100)
    elif(a==c):
        print(1000 + a * 100)
    else:
        print(1000 + c * 100)

else:
    print(max(num) * 100)
