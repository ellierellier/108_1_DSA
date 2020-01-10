# statues= [6, 2, 3, 8]
# def find_maxi(statues):
# 	# global maxi # global is envy
# 	maxi = statues[0]
# 	for i in range(len(statues)):
# 		if statues[i] > maxi:
# 			maxi = statues[i]
# 	return maxi
# 	# global maxi_num # global is envy
# 	# maxi_num = maxi
# # find_maxi(statues)


# def find_mini(statues):
# 	# global mini
# 	mini = statues[0]
# 	for a in range(len(statues)):
# 		if statues[a] < mini:
# 			mini = statues[a]
# 	return mini
# 	# global mini_num
# 	# mini_num = mini
# # find_mini(statues)


# def makeArrayConsecutive2(statues):
# 	maxi = find_maxi(statues)
# 	mini = find_mini(statues)
# 	for b in range(mini,maxi):
# 	# for b in range(mini_num, maxi_num):
# 		if mini+1 not in statues:
# 			statues = statues.append(mini+1)
# 			mini = mini + 1
# 		return statues
# print(makeArrayConsecutive2(statues))	

# #Hua Bao's way
# def makeArrayConsecutive2(statues):
#     min = statues[0]
#     max = statues[0]
#     for num in range(1,len(statues)):
#         if statues[num]<min:
#             min = statues[num]
#         elif statues[num]>max:
#             max = statues[num]
#     full_list_len = max - min +1 # list填滿後的長度
#     return full_list_len - len(statues)


statues= [6, 2, 3, 8]
#自己寫的樺寶法
def makeArrayConsecutive2(statues):
	maxi = max(statues)
	mini = min(statues)
	return (maxi-mini+1) - len(statues)
print(makeArrayConsecutive2(statues))




