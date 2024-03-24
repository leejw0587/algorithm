T=int(input())
for _ in range(T):
    marh=list(map(str, input().split()))
    R=float(marh[(-1)*len(marh)])

    for i in range(1, len(marh)):
        if marh[i]=='@':
                R*=3

        elif marh[i]=='%':
                R+=5

        elif marh[i]=='#':
                R-=7
                
    print('%0.2f'%R)