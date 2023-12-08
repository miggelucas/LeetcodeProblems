/*
 * @lc app=leetcode id=28 lang=swift
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
class Solution {
    func strStr(_ haystack: String, _ needle: String) -> Int {
        var result: Int = 0

        for i in 0...haystack.count {
            if i > haystack.count - needle.count {
                break
            }
            
            let start = haystack.index(haystack.startIndex, offsetBy: i)
            let end = haystack.index(haystack.startIndex, offsetBy: i + needle.count)
            let range = start..<end
            if haystack[range] == needle {
                result = i
                return result
            }
        }

        result = -1
        return result
        
    }
}
// @lc code=end

