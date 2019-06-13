def main():
    wine = []
    dp = []
    n = int(input())
    for i in range(n):
        wine.append(int(input()))
    if n == 1:
        print(wine[0])
        return
    elif n == 2:
        print(wine[1] + wine[0])
        return
    elif n == 3:
        print(max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2]))
        return
    else:
        dp.append(wine[0])
        dp.append(wine[0] + wine[1])
        dp.append(max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2]))
        for i in range(3, n):
            dp.append(max(dp[i-1], wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3]))
        print(dp[n-1])   

if __name__ == "__main__":
    main()
    