/*
 * @lc app=leetcode id=217 lang=swift
 *
 * [217] Contains Duplicate
 */

// @lc code=start
class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var numberSet: Set<Int> = []

        for number in nums {
            if numberSet.contains(number) {
                return true
            } else { 
                numberSet.insert(number)
            }
        }

        return false
        
    }
}
// @lc code=end

