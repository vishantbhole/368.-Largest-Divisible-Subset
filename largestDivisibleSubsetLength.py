 def largestDivisibleSubsetLength(self, nums: List[int]) -> int:
        if not nums:
           return []
         
        nums.sort()
        n = len(nums)
        
        dp = [1] * n          # dp[i] = size of subset ending at i
        max_len = 1
