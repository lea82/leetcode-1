# 409. Longest Palindrome
#
# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctmap = {}
        for c in s:
            if c not in ctmap:
                ctmap[c] = 1
            else:
                ctmap[c] += 1
        ret = 0
        singleCharFound = 0
        for key in ctmap:
            if ctmap[key] %2 == 0:
                ret += ctmap[key]
            else:
                ret += ctmap[key] - 1
                singleCharFound = 1
        return ret + singleCharFound

s = Solution()
print(s.longestPalindrome("abccccdd"))
