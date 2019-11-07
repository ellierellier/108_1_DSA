# 原創程式碼

nums = [1, 4, 2, 3.6]
class Solution(object):
    def divide(self, nums):    
        if len(nums)<2:
            return nums
        else:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            left = self.divide(left)
            right = self.divide(right)
            merge = self.merge(left,right)
        return merge
            
    def merge(self, left, right):
        sorted_result = []
        while left and right:
            if left[0] < right[0]:
                sorted_result.append(left.pop(0))
            else:
                sorted_result.append(right.pop(0))

        if left:
            sorted_result += left
        else:
            sorted_result += right
        return sorted_result
    
    def merge_sort(self, nums):
        ans = self.divide(nums)
        print(ans)
        
A = Solution()
A.merge_sort(nums)
