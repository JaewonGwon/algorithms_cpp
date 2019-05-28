from sys import setrecursionlimit


def main():
    x = int(input())
    ans = sol(x)%10007
    print(ans)


def sol(x):
    a, b = 1, 3
    for i in range(x):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    main()
