arr = [3, 1, 2]
def main():
    print(solution(arr))

def solution(A):
    target_list=[]
    idx = 1
    for i in A:
        if (idx == 1) or (len(target_list) == 1) or (len(target_list) == 0) or (target_list[-1] <= i) :
            while idx <= i:
                target_list.append(idx)
                idx += 1
            target_list.pop()

    if len(target_list) != 0:
        return False
    else:
        return True

main()
