# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Input
[0, 1, 2, 3, 4, 5, 6]

Output
[0, 6, 1, 5, 2, 4, 3]

Output
[0, n-1, 1, n-2, 2, n-3, ...]

3, n-4, 4, n-5 and so on....

-- Always know that the first node in the list never changes position
-- last element moves to be the 2nd element in the list
-- middle element gets moved to the last position of linked list
-- 2nd element of list gets shifted over to come right after the last node in the list


[2,4,6,8,10]

2 -> 10 -> 4 -> 8 -> 6

Even
--> shift the middle elements to the right of the last element and connect 
first element to last element

Odd
--> connect first element to last element
--> connect last element to 2nd element
--> connect 2nd element to 2nd to last element
--> connect 2nd to last element to 3rd element
--> connect 3rd element to 4th to last element


Might need 2 pointers
1. points to the 1st half of the linked list
2. points to the 2nd half of the linked list

I'm getting stuck on the fact that you can only move forward in a singly linked list
and by picking the last element as the 2nd pointer, you lose access for the 2nd to last and 3rd to last elements

 a.  
[2 4 6 8 10]

[1, 2, 3, 4, 5]

[1, 2]

[5, 4, 3]

[1, 5, 2, 4, 3]


list of size 9
first half size = 9 // 2 = 4
second half size = 9 % 2 = 5

- store in an array and occur an O(N) space complexity
- do this by looping through each element in linked list and appending item at the end

- manipulate the list by swapping 2nd item with last item
- do this for. 2nd item til the 2nd to last item for evens case
- do this for 2nd item til the 3rd to last item for odds case

-- evens you do the swap until 2nd to last item
2 4 6 8
2 8 6 4
2 8 4 6

-- odds 
2 4 6 8 10
2 10 6 8 4
2 10 4 8 6


1 2 3 4 5 6 7

1 7 3 4 5 6 2

1 7 2 4 5 6 3

1 7 2 3 5 6 4

1 7 2 3 4 6 5

1 2 3
7 6 5 4

1 7 2 6 3 5 4


'''


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        halfIndex = len(arr) // 2
        firstHalf = arr[:halfIndex] if halfIndex > 0 else arr
        secondHalfReversed = arr[len(arr)-1:halfIndex-1:-1]
        
        arr2 = []
        k, t = 0, 0
        while k < len(firstHalf) and t < len(secondHalfReversed):
            if k <= t:
                arr2.append(firstHalf[k])
                k += 1
            else:
                arr2.append(secondHalfReversed[t])
                t += 1

        while k < len(firstHalf):
            arr2.append(firstHalf[k])
            k += 1

        while t < len(secondHalfReversed):
            arr2.append(secondHalfReversed[t])
            t += 1

        curr = head
        j = 0
        while curr:
            curr.val = arr2[j]
            curr = curr.next
            j += 1
        