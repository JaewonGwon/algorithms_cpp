def main():
    list = [0, 0, 1, 1]
    X = 14

    for i in range(4, X+1):
        list.append(list[i-1] + 1)
        if i%2 == 0:
            list[i] = min(list[i], list[i//2] + 1)
        if i%3 == 0:
            list[i] = min(list[i], list[i//3] + 1)

    print(list[X])


if __name__ == "__main__":
    main()

