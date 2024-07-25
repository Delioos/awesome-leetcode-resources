/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycleTURBOOPTI(head *ListNode) bool {
    if head == nil {
        return false
    }
    
    slow, fast := head, head
    
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        
        if slow == fast {
            return true
        }
    }
    
    return false
}


func hasCycleBasic(head *ListNode) bool {
	/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
    if head == nil {
        return false
    }

    visited := make(map[*ListNode]bool)
    node := head

    for node != nil {
        if visited[node] {
            return true
        }
        visited[node] = true
        node = node.Next
    }

    return false
}
