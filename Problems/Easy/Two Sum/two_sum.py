class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i]+nums[j] == target):
                    return [i,j]
        else:
            return 0
        
