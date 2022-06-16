//https://leetcode.com/problems/merge-two-sorted-lists/submissions/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    // Check if either of the lists is null 
    if (!l1) {
        return l2;
    }
    if (!l2) {
        return l1;
    }
    // Head of the new linked list - this is the head of the resultant list
    let head = null;
    // Reference of head which is null at this point
    let temp = head;
    // Choose head which is smaller of the two lists
    if (l1.val < l2.val) {
        temp = head = new ListNode(l1.val);
        l1 = l1.next;
    } else {
        temp = head = new ListNode(l2.val);
        l2 = l2.next;
    }
    // Loop until any of the list becomes null
    while (l1 && l2) {
        if (l1.val < l2.val) {
            temp.next = new ListNode(l1.val);
            l1 = l1.next;
            temp = temp.next;
        } else {
            temp.next = new ListNode(l2.val);
            l2 = l2.next;
            temp = temp.next;
        }
    }
    // Add all the nodes in l1, if remaining
    while (l1) {
        temp.next = new ListNode(l1.val);
        l1 = l1.next;
        temp = temp.next;
    }
    // Add all the nodes in l2, if remaining
    while (l2) {
        temp.next = new ListNode(l2.val);
        l2 = l2.next;
        temp = temp.next;
    }
    return head;
};

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}