class Solution(object):
    def removeDuplicates(self, nums):
    
        length = 1
        if (len(nums) == 0):
            return 0
        for entry in range (1, len(nums)):
            if nums[entry] != nums[entry - 1]:
                nums[length] = nums[entry]
                length +=1
        
        return length
    
