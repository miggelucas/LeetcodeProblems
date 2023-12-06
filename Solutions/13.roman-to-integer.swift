/*
 * @lc app=leetcode id=13 lang=swift
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
    func romanToInt(_ s: String) -> Int {
        var result: Int = 0

        for (index, char) in s.enumerated() {
            let nextIndex = s.index(s.startIndex, offsetBy: index + 1)
            let next: Character? = index < s.count - 1 ? s[nextIndex] : nil

            switch char {
              case "I":
                result += (next == "V" || next == "X") ? -1 : 1
              case "V":
                result += 5
              case "X":
                result += (next == "L" || next == "C") ? -10 : 10
              case "L":
                result += 50
              case "C":
                result += (next == "D" || next == "M") ? -100 : 100
              case "D":
                result += 500
              case "M":
                result += 1000
             default:
                break
            }
        
        }
        
        return result
    }
}
// @lc code=end

