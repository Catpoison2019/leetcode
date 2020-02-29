#两数和#
#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#暴力求解 通过遍历整数数组来得到与目标值相等的两个整数
#时间复杂度o(n^2)
from typing import List
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        i=1
        for x in nums:
            j=0
            for y in nums[i:]:
                if x+y==target:
                    return [i-1,i+j]
                j=j+1
            i=i+1
            if i>=n:
               break



