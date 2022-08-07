class Solution:
    def reverse(self, x: int) -> int:
        y = str(x) if x >=0 else str(x)[1:]
        y = y[::-1]
        y = int(y) if x >= 0 else -int(y)
        return y if (-(2 ** 31)) <= y <= ((2 ** 31) - 1) else 0