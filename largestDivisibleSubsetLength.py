 def largestDivisibleSubsetLength(self, nums: List[int]) -> int:
        if not nums:
           return []
         
        nums.sort()
        n = len(nums)
        
        dp = [1] * n          # dp[i] = size of subset ending at i
        max_len = 1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
         max_len = max(max_len, dp[i])

         return max_len

if __name__ == "__main__":
    sol = Solution()

    nums3 = [1,2,3]
    print("Output is : ", sol.largestDivisibleSubsetLength(nums3))
