def main():
    X = int(input())
    list = [1, 2]
    for i in range(2, X):
        list.append(list[i-2] + list[i-1])
    
    print(list[X-1]%10007)
if __name__ == "__main__":
    main()