def almostIncreasingSequence(sequence):
    flag = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            flag += 1
                
    if flag <= 1: return True
    else: return False


