/*
 * @lc app=leetcode id=141 lang=swift
 *
 * [141] Linked List Cycle
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        if head == nil || head?.next == nil { return false }
        var slow = head
        var fast = head?.next
        while slow !== fast {
            if fast == nil || fast?.next == nil { return false }
            slow = slow?.next
            fast = fast?.next?.next

        }

        return true
    }
}
// @lc code=end

