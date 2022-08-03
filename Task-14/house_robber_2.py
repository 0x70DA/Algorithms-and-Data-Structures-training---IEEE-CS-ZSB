class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_houses(nums[:len(nums)-1]), self.rob_houses(nums[1:len(nums)]))

    def rob_houses(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for i in range(len(nums)):
            n1, n2 = n2, max(nums[i] + n1, n2)

        return n2
