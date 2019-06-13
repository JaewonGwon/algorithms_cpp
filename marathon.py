def solution():
    answer = 'failed'
    participant = ['leo', 'kiki', 'eden']
    completion = ['eden', 'kiki']
    participant.sort()
    completion.sort()
    for i in range(0,len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
        elif i == len(participant)-2 and participant[i] == completion[i]:
            print(i)
            return participant[i+1]
    return answer

print(solution())