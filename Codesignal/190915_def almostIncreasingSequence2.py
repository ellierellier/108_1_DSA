sequence = [1,3,2,1]
def almostIncreasingSequence(sequence):
    remove_list = 0
    for i in range(len(sequence)):
        if sequence[i+1] <= sequence[i]:
            remove_list = remove_list +1
            if remove_list >2:
                return False
        else:
            return True
print(almostIncreasingSequence(sequence))