inputArray = [3, 6, -2, -5, 7, 3]
# product_list= []
# def adjacentElementsProduct(inputArray):
# 	for a in range(len(inputArray)):
# 		adjacent_product = inputArray[a]*inputArray[a+1]
# 		product_list.append(adjacent_product)
# 	print(max(product_list))
	#演算法不能用套件（如max），要依照自己的思路去解決問題才有真的練習到演算法

def adjacentElementsProduct(inputArray):
	max = inputArray[0]*inputArray[1]
	for a in range(1,len(inputArray)-1):
		if inputArray[a]*inputArray[a+1] > max:
			max = inputArray[a]*inputArray[a+1]
	return max

adjacentElementsProduct(inputArray)



