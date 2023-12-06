/*
 * @lc app=leetcode id=14 lang=swift
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard strs.count > 0 else { return "" }
        var prefix = strs[0]
        for i in 1..<strs.count {
            while !strs[i].hasPrefix(prefix) {
                prefix.removeLast()
                if prefix.isEmpty { return "" }
            }
        }

        return prefix
    }
}
// @lc code=end

