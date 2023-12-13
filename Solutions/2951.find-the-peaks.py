#
# @lc app=leetcode id=2951 lang=python3
#
# [2951] Find the Peaks
#

# @lc code=start
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result: [int] = []

        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                result.append(i)

        return result        
# @lc code=end

