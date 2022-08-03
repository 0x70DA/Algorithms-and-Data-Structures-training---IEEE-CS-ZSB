class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lst = [0]
        for i in range(1, amount + 1):
            min_coins = -1
            for coin in coins:
                if i - coin >= 0 and lst[i-coin] != -1:
                    if min_coins == -1:
                        min_coins = lst[i-coin] + 1
                    else:
                        min_coins = min(min_coins, lst[i-coin] + 1)
            lst.append(min_coins)

        return lst[amount]
