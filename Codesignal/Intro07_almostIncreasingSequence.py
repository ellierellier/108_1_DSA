sequence = [1, 3, 2, 1]
def almostIncreasingSequence(sequence):


def almostIncreasingSequence(sequence):
    dec_count = 0
    for num in range(0,len(sequence)-1):
        if sequence[num]>=sequence[num+1]:
            if dec_count == 0:
                dec_count+=1
            else:
                return False
    return True

def almostIncreasingSequence(sequence):
    dec_count = 0
    for num in range(1,len(sequence)-1):
        if sequence[num]<=sequence[num-1]: # 前比後大，代表有減的話
            dec_count+=1 # 減少的次數加一
            if dec_count > 1:  # 當減少的次數大於一
                return False # 直接回傳錯誤
            else: # 否則當減少的次數<=1時
                if sequence[num+1] >= sequence[num]: # 如果後面又彼此大的話 
                    return False # 回傳False
    return True
    
