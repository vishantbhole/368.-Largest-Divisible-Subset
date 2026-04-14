 def largestDivisibleSubsetLength(self, nums: List[int]) -> int:
        if not nums:
           return []
         
        nums.sort()
        n = len(nums)
