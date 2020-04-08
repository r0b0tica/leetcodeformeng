from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)


if __name__ == "__main__":
    assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6