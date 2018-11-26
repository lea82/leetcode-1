# 313. Super Ugly Number

# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
#
# Example:
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
#              super ugly numbers given primes = [2,7,13,19] of size 4.
#
# Note:
#
#     1 is a super ugly number for any given primes.
#     The given numbers in primes are in ascending order.
#     0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
#     The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
#

class Solution:
    # https://leetcode.com/problems/super-ugly-number/discuss/76291/Java-three-methods-23ms-36-ms-58ms(with-heap)-performance-explained
    # Basic idea is same as ugly number II, new ugly number is generated by multiplying a prime
    # with previous generated ugly number. One catch is need to remove duplicate
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import sys

        ugly = [0] * n
        idx = [0] * len(primes)

        ugly[0] = 1
        for i in range(1, n):
            # find next
            # ugly[i] = sys.maxint # py2
            ugly[i] = sys.maxsize
            for j in range(0, len(primes)):
                ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])

            # slip duplicate
            for j in range(0, len(primes)):
                while primes[j] * ugly[idx[j]] <= ugly[i]:
                    idx[j] += 1

        return ugly[n - 1]

sol = Solution()
print(sol.nthSuperUglyNumber(12, [2,7,13,19]))

