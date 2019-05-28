def main():
    for j in range(int(input())):
        a, b, c = 1, 2, 4
        x = int(input())
        if x == 1:
            print(a)
        elif x == 2:
            print(b)
        else:
            for i in range(4, x+1):
                a, b, c = b, c, (a + b + c)
            print(c)


if __name__ == "__main__":
    main()
