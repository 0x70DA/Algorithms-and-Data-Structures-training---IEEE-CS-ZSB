# Memoization
class Solution:
    def climbStairs(self, n: int, table: dict = {}) -> int:
        if n <= 3:
            return n
        if n-1 not in table.keys():
            table[n-1] = self.climbStairs(n-1, table)
        if n-2 not in table.keys():
            table[n-2] = self.climbStairs(n-2, table)

        return table[n-1] + table[n-2]


# Iterative
class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [1, 2]
        for i in range(2, n):
            lst.append(lst[i-1] + lst[i-2])

        return lst[n-1]

