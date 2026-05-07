class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # If we had an array [-1], 0 would be returned as maximum product, so it is not an ideal default case

        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1 # Resetting, or 0 * X will keep coming as 0
                continue
            temp = n * curMax # We are re-computing curMax in the next step, and we want to retain the value before we re-compute it when we compute curMin. Hence, we are assigning it to a temporary variable
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(curMax, res)
        return res
