class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        max_sub = ''
        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(max_sub):
                    max_sub = s[l:r+1]
                l -= 1
                r += 1

            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(max_sub):
                    max_sub = s[l:r+1]
                l -= 1
                r += 1

        return max_sub
