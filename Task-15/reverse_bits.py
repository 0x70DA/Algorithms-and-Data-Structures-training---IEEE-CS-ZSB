# Soulution using bit manipulation
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & (1 << i):
                res |= (1 << 31 - i)

        return res


# Regular solution
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         s = bin(n)[2:][::-1]
#         s += '0' * (32 - len(s))
#         return int(s, 2)
