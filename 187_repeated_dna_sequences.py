# 187. Repeated DNA Sequences
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#
# this Problem can be solve with O(n) time and O(n) space with hashing
# http://blog.csdn.net/hyperbolechi/article/details/44302991


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict = {}
        for i in range(len(s) - 9):
            if s[i:i + 10] not in dict:
                dict[s[i:i + 10]] = 1
            else:
                dict[s[i:i + 10]] += 1
        res = []
        for elem in dict:
            if dict[elem] > 1:
                res.append(elem)
        return res


if __name__ == '__main__':
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
