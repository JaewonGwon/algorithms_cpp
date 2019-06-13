def main():
    target = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    result = quicksort(target)
    print(result)

def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)
    return quicksort(less) + equal + quicksort(more)


if __name__ == "__main__":
    main()