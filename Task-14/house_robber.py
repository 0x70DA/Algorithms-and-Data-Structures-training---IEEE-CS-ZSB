class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        n1, n2 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            n1, n2 = n2, max(nums[i]+n1, n2)

        return n2
