#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                print(map[target - num], i)
                return [map[target - num], i]
            map[num] = i
# @lc code=end

