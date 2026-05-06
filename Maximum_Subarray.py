class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] # By default, we should start with the first element
        curSum = 0 # Initialising since we are going to add numbers from n, one-by-one

        for n in nums:
            if curSum < 0:
                curSum = 0 # Re-initializing curSum, since negatives won't add up to maximum
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
