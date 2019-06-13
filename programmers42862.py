def solution(n, lost, reserve):
    answer = 0
    lost = [i for i in lost if i not in reserve]
    reserve = [i for i in reserve if i not in lost]
    lost.sort()
    reserve.sort()
    
    try:
        for i in range(30):
            if reserve[len(reserve)-1]+1 in lost:
                lost.remove(reserve[len(reserve)-1]+1)
                reserve.remove(reserve[len(reserve)-1])
            elif reserve[len(reserve)-1]-1 in lost:
                lost.remove(reserve[len(reserve)-1]-1)
                reserve.remove(reserve[len(reserve)-1])            
    except:
        pass
    
    answer = n - len(lost)
    return answer