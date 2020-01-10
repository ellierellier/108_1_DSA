def checkPalindrome(inputString):
	inverse_string = inputString[::-1]
	if inputString == inverse_string:
		return True
	else:
		return False

# 可直接返回處理過的值 by adjeko
# def checkPalindrome(inputString):
    # return inputString == inputString[::-1]
