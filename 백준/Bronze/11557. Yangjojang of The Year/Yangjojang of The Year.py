T = int(input())

for i in range(T):
    N = int(input())

    univlist = []
    for j in range(N):
        univname, liter = input().split()
        liter = int(liter)

        univlist.append(tuple([univname, liter]))

    univlist.sort(key=lambda x:x[1], reverse=True)
    print(univlist[0][0])
