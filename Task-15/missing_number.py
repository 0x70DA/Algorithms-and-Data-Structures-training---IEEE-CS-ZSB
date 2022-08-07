class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The sum of numbers 0..n is n*(n+1)//2
        s = (len(nums) * (len(nums) + 1)) // 2
        return s - sum(nums)


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         n1, n2 = 0, 0
#         for i in range(n+1):
#             n1 ^= i

#         for i in nums:
#             n2 ^= i

#         return n1 ^ n2
