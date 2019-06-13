def main():
    rule = [int(i) for i in input().split(' ')]
    coinset = []
    for i in range(rule[0]):
        coinset.append(int(input()))
    target = rule[1]
    
    for i in range(len(coinset)):
        if coinset[i] >= target:
            coinset = coinset[0:i+1]
            break

    coinset.reverse()
    ans = {}
    for i in range(len(coinset)):
        ans[coinset[i]] = target//coinset[i]
        target = target%coinset[i]
    
    print(ans)

if __name__ == "__main__":
    main()