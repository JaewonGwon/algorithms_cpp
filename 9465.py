n = int(input())

for k in range(n):
    w = int(input())
    t = []
    t.append(input().split(' '))
    t.append(input().split(' '))

    t[0] = [int(i) for i in t[0]]
    t[1] = [int(i) for i in t[1]]

    t[0][1] = t[1][0] + t[0][1]
    t[1][1] = t[0][0] + t[1][1]

    for j in range(2, w):
        t[0][j] = max(t[1][j-2] + t[0][j], t[1][j-1] + t[0][j])
        t[1][j] = max(t[0][j-2] + t[1][j], t[0][j-1] + t[1][j])

    print(max(t[0][w-1], t[1][w-1]))
    