# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        result = ListNode() #初始结点
        head = result #保存head
        while list1 != None and list2 != None: #如果list1和list2的当前结点都不为空时
            if list1.val <= list2.val:
                result.next = list1 #直接指向结点
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
        
            result = result.next #链表前进一个结点

        if list1 == None:   #处理单个list为空的情况
            result.next = list2
        else:
            result.next = list1
        
        return head.next #头结点为空，需返回head.next