/*
 * @lc app=leetcode id=9 lang=swift
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        let str = String(x)
        let reversedStr = String(str.reversed())
        return str == reversedStr
    }
}
// @lc code=end

