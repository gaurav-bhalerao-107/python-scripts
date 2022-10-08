class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sumExp = N*(N+1) // 2
        sumAct = sum(nums)
        
        return sumExp - sumAct
            