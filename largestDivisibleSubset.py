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
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
                
        # Reconstruct the subset
        result = []

        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = parent[max_idx]

        return result[::-1]

if __name__ == "__main__":
    sol = Solution()


    nums = [1,2,3]
    print("Output is : ", sol.largestDivisibleSubset(nums))

    nums2 = [1,2,4,8]
    print("Output is : ", sol.largestDivisibleSubset(nums2))
