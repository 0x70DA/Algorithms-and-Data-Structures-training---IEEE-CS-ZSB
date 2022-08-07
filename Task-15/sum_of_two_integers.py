class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        
        while b:
            carry = a & b
            a = (a ^ b) & mask   # find sum and store in a
            b = (carry << 1) & mask  # carry to be used for next pair of digits
        
        return a if a <= MAX else ~(a ^ mask)


# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         def add(a, b):
#             if not a or not b:
#                 return a or b
#             return add(a ^ b, (a & b) << 1)

#         if a * b < 0:  # assume a < 0, b > 0
#             if a > 0:
#                 return self.getSum(b, a)
#             if add(~a, 1) == b:  # -a == b
#                 return 0
#             if add(~a, 1) < b:  # -a < b
#                 return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

#         return add(a, b)  # a*b >= 0 or (-a) > b > 0