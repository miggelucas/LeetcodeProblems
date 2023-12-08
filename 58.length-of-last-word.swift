/*
 * @lc app=leetcode id=58 lang=swift
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    func lengthOfLastWord(_ s: String) -> Int {

        if s.isEmpty { return 0 }
        var result: Int = 0

        for i in 0 ..< s.count {
            let index = s.index(s.startIndex, offsetBy: s.count - 1 - i)
            if s[index] == " " {
                if result > 0 {
                    return result
                }
                
            } else { 
                result += 1
            }
        }
        
        return result
    }
}
// @lc code=end

