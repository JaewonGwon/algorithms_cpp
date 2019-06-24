def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append([0 for l in range(n)])
    cnt = 1
    curX = 0
    curY = 0

    arr[curX][curY] = cnt
    
    while cnt < n * n:
        if curY + 1 < n:
            curY = curY + 1
        else:
            curX = curX + 1
        cnt = cnt + 1
        arr[curX][curY] = cnt

        while curY - 1 > -1 and curX + 1 < n:
            curY = curY - 1
            curX = curX + 1
            cnt = cnt + 1
            arr[curX][curY] = cnt
        
        if curX + 1 < n:
            curX = curX + 1
        else:
            curY = curY + 1
        
        cnt = cnt + 1
        arr[curX][curY] = cnt

        while curX - 1 > -1 and curY + 1 < n:
            curY = curY + 1
            curX = curX - 1
            cnt = cnt + 1
            arr[curX][curY] = cnt

main()