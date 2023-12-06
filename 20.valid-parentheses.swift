/*
 * @lc app=leetcode id=20 lang=swift
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    func isValid(_ s: String) -> Bool {
      
        var openChars = ["(", "[", "{"]
        var stack: [String] = []
        for char  in s {
            if openChars.contains(String(char)) {
                stack.append(String(char))
            } else {
                if stack.isEmpty { return false }
                var last = stack.removeLast()
                if char == ")" && last != "(" { return false }
                if char == "]" && last != "[" { return false }
                if char == "}" && last != "{" { return false }

            }
        }

    
        if !stack.isEmpty { return false } else { return true }
 
            
    }
}
// @lc code=end

