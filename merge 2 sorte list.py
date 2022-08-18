'''
Program to merge 2 sorted list
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        l = ListNode()
        l.next = None
        l.value = 0

        while (list1.next != 0):
            while (list2.next != 0):
                if list2.val <= list1.val:
                    l.val = list2.val
                    l = l.next

                else:
                    l.val = list1.val
                    list1 = list1.next
                list2 = list2.next
            list1.next


l1 = [1,2,4]
l2 = [1,3,4]
'''
n1 = int(input("Enter the no. of items you want in 1st list: "))
for i in range(0,n1):
    ele = int(input("Enter the {} element in the list".format(i)))
    l1.append(ele)
n2 = int(input("Enter the no. of items you want to add in 2nd list:"))
for j in range(0,n2):
    ele1 = int(input("Enter the {} element in the list".format(j)))
    l2.append(ele1)
print(l1,l2)
merged = merge_list(l1,l2)
print("merged list of 2 sorted list: {0}".format(merged))
'''


