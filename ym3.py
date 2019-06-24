def main():
    solution(5, 4, 4)
    return 0

def solution(n, c, r):
    idx = c - 1
    r = r + idx
    if r <= n:
        target = 0
        for i in range(1, r + 1):
            target = target + i 
        if r % 2 == 0:
            print(target)
            print(target - idx)
            return
        else:
            print(target)
            print(target - (r-c))
            return
    else:
        target = n*n
        r = 2*n - r
        for i in range(1, r + 1):
            target = target - i
        if r % 2 == 0:
            print(target)
            print(target - idx)
            return
        else:
            print(target)
            print(target - (r-c))
            return
        
main()