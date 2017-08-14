"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer.
However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow.
How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # find the max divisor
        # later decrease the divisor in the loop
        div = 1
        while x / div >= 10:
            div *= 10

        while x:
            left = x / div
            right = x % 10

            if left != right:
                return False

            # strip off left most and right most
            # print x, div
            x = (x % div) / 10
            # decrease by order of 2 divisor
            div /= 100

        return True


if __name__ == '__main__':
    print Solution().isPalindrome(-1234)
    print Solution().isPalindrome(123321)
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(3)
