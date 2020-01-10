class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        contain_even_number_of_digits = 0
        
        for n in nums:
            if len(str(n)) % 2 ==0:
                contain_even_number_of_digits += 1
                
        return contain_even_number_of_digits