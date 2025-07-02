# №704
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             return nums[0]
# Time complexity O(n)



# №74
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         matrix = sum(matrix, [])
#         if target in matrix:
#             return True
#         else:
#             return False
# Time complexity O(n)
# Memory complexity O(nlogn)



# №153
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         return nums[0]
# time complexity O(n)
# Time comlexity O(nlogn)
from math import ceil
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         right = len(nums) - 1
#         left = 0
#         while right > left:
#             middle = (left + right) >> 1
#             if nums[middle] > nums[right]:
#                 left = middle + 1
#             else:
#                 right = middle
#         return nums[left]
# Time complexity O(n)
# Memory complexity O(n)




# №206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         prev = None
#         while current:
#             empty = current.next
#             current.next = prev
#             prev = current
#             current = empty
#         return prev
# Time complexity O(n)
# Memory comlexity O(1)



# №793
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         ans = []
#         for i in range(len(temperatures)):
#             ans.append(0) # == ans += [0]
#         for index, temperature in enumerate(temperatures):
#             while stack and stack[-1][0] < temperature:
#                 popped_temp, popped_index = stack.pop()
#                 ans[popped_index] = index - popped_index
#             stack.append((temperature, index))
#         return ans
# Time complexxity O(n)
# Memory complexity (n)


#№33
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # ans = []
#         # first = nums[0]
#         # ans = first >> target
#         # return ans
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1
# Time complexity O(n)


#№234
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         stack = []
#         current = head
#         while current:
#             stack.append(current.val)
#             current = current.next
#         current = head
#         while current:
#             if current.val != stack.pop():
#                 break
#             current = current.next
#         return not(current)
# Time O(n)
# MemoryO(n)




#№78
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         ans  = [[]]
#         for elem in nums:
#             ans += [subset + [elem] for subset in ans]
#         return ans
# Time complexity O(n * 2^n)
# Memory compexity O(n)

#№55
# class Solution:
#     def canJump(self, nums: List[int]) -> bool
        # first solution doest work if last num = 0
        # if 0 in nums:
        #     return False
        # else:
        #     return True

        # second solution(bad for Memory complexity)
        # nums = sorted(nums)
        # for i in nums:
        #     if nums[0] != 0:
        #         return True
        #     else:
        #         return False

        # third solution(best)
        # max_num = 0
        # for i, num in enumerate(nums):
        #     if i > max_num:
        #         return False
        #     max_num = max(max_num, i + num)
        # return True




#№3168
# class Solution:
#     def minimumChairs(self, s: str) -> int:
#         ans = 0
#         chairs = 0
#         for i in s:
#             if i == "E":
#                 chairs += 1
#             else:
#                 chairs -= 1
#             ans = max(ans, chairs)
#         return ans



#57
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         intervals.append(newInterval)
#         ans = []
#         for sublist in sorted(intervals, key=lambda x: x[0]):
#             if ans and ans[-1][1] >= sublist[0]:
#                 ans[-1][1] = max(ans[-1][1], sublist[1])
#             else:
#                 ans.append(sublist)
#         return ans
# Time complexity: O(n*logn)
# Memory complexity: O(n)










