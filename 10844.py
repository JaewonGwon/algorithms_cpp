def solution():
    x = int(input())
    list = [0, 9, 17]
    if x == 1 or x == 2:
        print(list[x])
    else:
        for i in range(3, x+1):
            list.append(list[i-1]*2 - 2)
        
        print(list[x]%1000000000)

solution()