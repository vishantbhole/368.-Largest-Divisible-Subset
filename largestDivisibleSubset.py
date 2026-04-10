#368. Largest Divisible Subset
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
         
        dp = [1] * n          # dp[i] = size of subset ending at i
        parent = [-1] * n     # to reconstruct the subset
        
        max_len = 1
        max_idx = 0
