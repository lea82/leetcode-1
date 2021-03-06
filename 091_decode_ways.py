# -*- coding: utf-8 -*-
"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

http://www.cnblogs.com/zuoyuan/p/3783897.html

解题思路：解码有多少种方法。一般求“多少”我们考虑使用dp。

状态方程如下：

　　　　 当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，
        那么可以有两种编码方式（BA，U），
        所以dp[i]=dp[i-1]+dp[i-2]

　　　　 当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，
        所以dp[i]=dp[i-2]

　　　　 当s[i-2:i]不在以上两个范围时，
        如09这种，编码方式为0，
        而31这种，dp[i]=dp[i-1]。

　　　　 注意初始化时：dp[0]=1,dp[1]=1
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == '0':
            return 0

        dp = [1, 1]
        for i in range(2, len(s) + 1):
            # xxx12xxx
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            # xxx20xxx
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:
                dp.append(dp[i - 2])
            # xxx59xxx
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            # xx307xxx
            else:
                return 0
        return dp[len(s)]

    # https://www.cnblogs.com/grandyang/p/4313384.html
    def numDecodings(self, s):
        if s == '' or s[0] == 0:
            return 0
        dp = [1] * (len(s) + 1)
        for i in range(1, len(dp)):
            dp[i] = 0 if s[i-1] == '0' else dp[i-1]
            if (i > 1) and (s[i-2] == '1' or (s[i-2] == '2' and int(s[i-1]) <= 6)):
                dp[i] += dp[i-2]    # add one more if s[i-2] = 1 or 2.
        return dp[len(s)]


if __name__ == '__main__':
    print Solution().numDecodings('80')
    print Solution().numDecodings('509')
