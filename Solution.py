class Solution:
    def subsequenceSumAfterCapping(self, nums, k):
        nums.sort()
        dp = [False] * (k + 1)
        dp[0] = True

        result = [False] * len(nums)
        index = -1

        for i in range(len(nums)):
            while index != len(nums) - 1 and nums[index + 1] <= i + 1:
                self.update(dp, nums[index + 1])
                index += 1

            result[i] = any(
                k - j * (i + 1) >= 0 and dp[k - j * (i + 1)]
                for j in range(0, len(nums) - index)
            )

        return result

    def update(self, dp, value):
        for i in range(len(dp) - 1, value - 1, -1):
            dp[i] = dp[i] or dp[i - value]
