def main():
    length = int(input())
    d = [int(i) for i in input().split(' ')]
    max = 0
    cnt = 0
    for i in range(1, len(d)):
        if d[i] > d[i-1] and d[i] > max:
            max = d[i]
            cnt = cnt + 1
    if cnt != 0:
        print(cnt+1)
        return
    print(cnt+1)

if __name__ == "__main__":
    main()