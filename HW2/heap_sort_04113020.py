# 原創程式碼
# nums = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0] 這是原本自己測試用的
result = []
size = len(nums)

class Solution(object):
    
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]
    
    def heapify(self, nums, index):
        left = 2*index + 1
        right = 2*index +2
        size = len(nums)
        
        if size<2:
            return nums
        
        if left <= size-1 and nums[left] > nums[index]:
            self.swap(nums, index, left)
            self.heapify(nums, left)
        if right <= size-1 and nums[right] > nums[index]:
            self.swap(nums, index, right)
            self.heapify(nums, right)
    
    #[4,3.6,2,1] -> [1,3.6,2,4]
    def heapify_down(self, nums):
        for rounds in range(size-1, -1, -1):
            self.swap(nums, 0, rounds)
            result.append(nums.pop())
            self.heapify(nums, 0)
        return result
        
    def heap_sort(self,nums):
        for element in range(size-1, -1, -1):
            self.heapify(nums, element)
        
        ans = self.heapify_down(nums)
        ans = ans[::-1]
        return ans

# test = Solution() ####原本自己測試的
# test.heap_sort(nums)
List[int] = Solution().heap_sort(nums)
