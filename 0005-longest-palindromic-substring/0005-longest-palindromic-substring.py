class Solution:
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            for j in (i, i + 1):
                l, r = i, j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(ans):
                        ans = s[l:r + 1]
                    l -= 1
                    r += 1
        return ans        