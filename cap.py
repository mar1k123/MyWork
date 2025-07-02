from sys import prefix
from typing import List
# def Dev(x: int) -> set:
#     l = []
#     for i in range(1, int((x+1)**0.5 + 1)):
#         if x % i == 0:
#             l.append(i)
#             l.append(x // i)
#     a = set(l)
#     l = list(a)
#     l.sort()
#     return l
#
# for i in range(100, 200):
#     if len(Dev(i)) == 4:
#         print(Dev(i)[1:3])

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         empty = []
#         sort_list = ['.'.join(sorted(strs)) for strs in list]
#         print(sort_list)
# a = b.sort()
# print(a)
# class Solution:
#     def groupAnagrams(self,strs: List[str]) -> List[List[str]]:
#         empty = []
#         sort_list = strs.sort()
#         for element in sort_list:
#             if element[0] == element + 1:
#                 empty += element
#             else:
#                 empty += element
#         return empty
# strs = [''.join(sorted(i)) for i in strs]
# print(strs)
# strs = ["eat","tea","tan","ate","nat","bat"]

# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     empty = [0] * 26
#     strs = [''.join(sorted(i)) for i in strs]
#     for i in range(len(strs)):
#         for j in range(i + 1, len(strs)):
#             if strs[i] == strs[j]:
#                 empty += [i, j]
#             else:
#                 empty += [i, j]
#     return empty
#
#
# print(groupAnagrams(strs))

#

# a = a.replace(" ","")
# a = a.lower()
# a = a.replace("?", "")
# b = [a]
# b = b.reverse()
# print(a)
# print(b)
# a = [a]
# print(a)

# nums = [1,2,3,7,1,12,4]
# cnt = 0
#
# last = nums[-1]
# penultimate = nums[-2]
# while True:
#     if last - penultimate == 1:
#         cnt += 1
#     else:
#         penultimate - 1 and last - 1
# class Solution:
#     def custom_isalnum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or
#                 ord('a') <= ord(c) <= ord('z') or
#                 ord('0') <= ord(c) <= ord('9'))
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             if not self.custom_isalnum(s[left]):
#                 left += 1
#                 continue
#             if not self.custom_isalnum(s[right]):
#                 right -= 1
#                 continue
#             if s[left].lower == s[right].lower:
#                 left += 1
#                 right -= 1
#             else:
#                 return False
#         return True
#
# s = "Was it a car or a cat I saw?"
# print(Solution().isPalindrome(s))
from re import search
from typing import List
import random
# a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [100, -1, -100]
# f = [1]
# def merge_iterative(a: List[int], b: List[int]) -> List[int]:
#     c = [0] * (len(a) + len(b))
#     cnt = 0
#     cnt_a = 0
#     cnt_b = 0
#     while cnt_a < len(a) and cnt_b < len(b):
#         if a[cnt_a] <= b[cnt_b]:
#             c[cnt] = a[cnt_a]
#             cnt_a += 1
#         else:
#             c[cnt] = b[cnt_b]
#             cnt_b += 1
#         cnt += 1
#     while cnt_a < len(a):
#         c[cnt] = a[cnt_a]
#         cnt += 1
#         cnt_a += 1
#     while cnt_b < len(b):
#         c[cnt] = a[cnt_b]
#         cnt += 1
#         cnt_b += 1
#     return c



# print(sorted(a+b))


# def quicksort(a: List[int]) -> List[int]:
#     if len(a) <= 1:
#         return a
#     pivot = a[len(a) // 2]
#     left = []
#     right = []
#     middle = []
#     for elem in a:
#         if elem < pivot:
#             left.append(elem)
#         elif elem > pivot:
#             right.append(elem)
#         else:
#             middle.append(elem)
#     return quicksort(left) + middle + quicksort(right)
#
# Ultimate_number = random.sample(range(1,10000001), 1000)
# f_list = random.sample(range(1,100),10//2)
# s_list = [y + random.randint(1, 10) for y in f_list] #a<y<b
# c = f_list + s_list
# print(c)
# print(quicksort(c))
# nums = {2,20,4,10,3,4,5}
# print(nums)






# nums = [1,1,1,2,2,3]
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         k = []
#         cnt = 1
#         for i in range(len(nums)):
#             for j in range(i + 1,len(nums)):
#                 if nums[i] == nums[j]:
#                     cnt += i,j
#                 else:
#                     cnt = k
#                 cnt = 0
#         return k
# print(ord("."))
# def find_dev(n):
#     div = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             div.append(i)
#     return div
#
# print(find_dev(28))


'''Обмен рекордов'''
# if we use import
# def main():
#
'''my solution but doest work totally   '''
#     from itertools import accumulate
#     n = int(input.txt())
#     a = list(map(int, input.txt().split()))
#     record = 0
#     is_good_massive = []
#     for i in range(1, len(a)):
#         if len(a[:i-1]) != 0  and a[i] > max(a[:i-1]):
#             record = a[i]
#             break
#     options = [a.copy()]
#     point = a.index(record)
#     while point > 0 and a[point - 1] < record:
#         a[point], a[point - 1] = a[point - 1], a[point]
#         options.append(a.copy())
#         point -= 1
#     is_good_massive = options
#     pref = ([list(accumulate(sub_arr)) for sub_arr in is_good_massive])
#     pref_sum = [sum(pref_ix) for pref_ix in pref]
#     print(sum(pref_sum) % (10 ** 9 + 7))



'''the best but complex'''
# def main(file):
#     n = int(file.readline())
#     a = list(map(int, file.readline().split()))
#     is_record = [0] * n
#     record = 0
#     for i in range(1, n):
#         if a[i] > record:
#             is_record[i] = 1
#         record = max(a[i], record)
#
#     dp = [n - i for i in range(n)]
#     prev = [1] * (n + 1)
#     for pointer in range(n):
#         if is_record[pointer]:
#             next = pointer + 1
#         else:
#             next = 1
#         prev[pointer + 1] = prev[pointer] * next
#
#     sum_ = 0
#     for i in range(n - 1, -1, -1):
#         current = dp[i]
#         if is_record[i]:
#             for j in range(i):
#                 current += dp[j]
#         sum_ += current * prev[i] * a[i]
#         if is_record[i]:
#             dp_new = [0] * n
#             for j in range(i):
#                 dp_new[j] += dp[j] * (i - j)
#                 dp_new[j] += dp[j + 1] * (j + 1)
#             dp = dp_new
#     print(sum_)
#
# if __name__ == '__main__':
#     print(main())








# def my_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return s
# LOG = 19
#
# class ListNode:
#     def __init__(self, u = 0):
#         self.u = u
#         self.parent = None
#         self.height = 0
#         self.up = [None] * LOG
#
# def main(file):
#     list_nodes = []
#     list_nodes.append(ListNode(1))
#     current_tree_size = 1
#     q, m = list(map(int, file.readline().split()))
#     ans = 0
#     ops = [list(map(my_int,
#                     file.readline().split())) for _ in range(q)]
#
#     for operation in ops:
#         if operation[0] == "+":
#             u = operation[1]
#             listnode = ListNode(u)
#             listnode.parent = list_nodes[u]
#
#         elif operation[0] == "?"
#
#
#
#
#
#
#
#  if __name__ == '__main__':
#     with open('input.txt.txt', 'r') as file:
#         t = int(file.readline())
#     for _ in range(t):
# print(main(file))


# def main(file):
#     n = int(file.readline())
#     a = list(map(int, file.readline().split()))
#
#     pointer = 0
#     while pointer < n:
#         a_i = a[pointer]
#         if a_i % 2 == 0:
#             break
#         elif pointer > 0:
#             print('x', end='')  #file=open('name file.txt', 'a+' / '...+')
#         pointer += 1
#
#     if pointer > 0:
#         print('+', end='')
#     pointer += 1
#
#     while pointer < n:
#         a_i = a[pointer]
#         if a_i % 2 == 0:
#             print('x', end='')
#         else:
#             break
#         pointer += 1
#     if pointer < n:
#         print('+', end='')
#     while pointer + 1 < n:
#         print('x', end='')
#         pointer += 1
#
#
# if __name__ == '__main__':
#     with open('input.txt', 'r') as file:
#         a = int(file.readline())
#         for _ in range(a):
#             main(file)
#             print()





# def main(file):
#     n = int(file.readline())
#     k = int(file.readline())
#     p = sorted(list(map(int, file.readline().split())))
#
#     max_pos = 0
#     min_pos = 0
#     for i in range(n - 1):
#         p_i = p[i]
#         if max_pos + 1 <= p_i:
#             max_pos += 1
#     max_pos = min(k - 1, max_pos) + 1
#
#     for i in range(k - 1):
#         p_i = p[min_pos]
#         if i + 1 > p_i:
#             min_pos += 1
#     min_pos = k - min_pos
#
#     return min_pos, max_pos
#
#
# if __name__ == '__main__':
#     with open('input.txt', 'r') as file:
#         a = int(file.readline())
#         for _ in range(a):
#             print(main(file))






# import random
# import sys
#
# random.seed(13111)
#
# MN = 300010
# #декартово дерево по неявному ключу (Treap)
#
# class Node:
#     def __init__(self, v_, h_):
#         self.v = v_
#         self.h = h_
#         self.y = random.randint(0, 10 ** 18)
#         self.l = None
#         self.r = None
#         self.p = None
#         self.m = h_
#         self.k = 1
#         self.f = 0
#         self.mn = h_
#
#     def push(self):
#         if self.f:
#             if self.l:
#                 self.l.f += self.f
#                 self.l.h += self.f
#                 self.l.m += self.f
#                 self.l.mn += self.f
#             if self.r:
#                 self.r.f += self.f
#                 self.r.h += self.f
#                 self.r.m += self.f
#                 self.r.mn += self.f
#             self.f = 0
#
#     def upd(self):
#         self.m = self.h
#         self.k = 1
#         self.mn = self.h
#         if self.l:
#             self.mn = min(self.mn, self.l.mn)
#             if self.l.m > self.m:
#                 self.m = self.l.m
#                 self.k = self.l.k
#             elif self.l.m == self.m:
#                 self.k += self.l.k
#         if self.r:
#             self.mn = min(self.mn, self.r.mn)
#             if self.r.m > self.m:
#                 self.m = self.r.m
#                 self.k = self.r.k
#             elif self.r.m == self.m:
#                 self.k += self.r.k
#
#
# def upd_p(v, p):
#     if v:
#         if p:
#             p.push()
#         v.p = p
#         if p:
#             p.upd()
#
#
# def merge2(a, b):
#     if a is None:
#         if b:
#             b.push()
#             b.upd()
#         return b
#     if b is None:
#         a.push()
#         a.upd()
#         return a
#     a.push()
#     b.push()
#     a.upd()
#     b.upd()
#     if a.y < b.y:
#         t = merge2(a, b.l)
#         b.l = t
#         upd_p(t, b)
#         b.upd()
#         return b
#     else:
#         t = merge2(a.r, b)
#         a.r = t
#         upd_p(t, a)
#         a.upd()
#         return a
#
#
# def push_up(v):
#     if v:
#         if v.p:
#             push_up(v.p)
#         v.push()
#         v.upd()
#
#
# def merge(a, b):
#     p = merge2(a, b)
#     push_up(p)
#     return p
#
#
# def split_l(a, b):
#     if a.p is None:
#         return (b, a)
#     a.push()
#     a.upd()
#     if a.p.l == a:
#         return split_l(a.p, b)
#     else:
#         t = a.p
#         a.p = None
#         t.r = b
#         upd_p(b, t)
#         t.upd()
#         return split_r(t, a)
#
#
# def split_r(a, b):
#     if a.p is None:
#         return (a, b)
#     a.push()
#     a.upd()
#     if a.p.r == a:
#         return split_r(a.p, b)
#     else:
#         t = a.p
#         a.p = None
#         t.l = b
#         upd_p(b, t)
#         t.upd()
#         return split_l(t, a)
#
#
# def split_l_node(a):
#     push_up(a)
#     a.push()
#     a.upd()
#     t = a.l
#     if t:
#         t.push()
#         t.upd()
#     a.l = None
#     upd_p(t, None)
#     a.upd()
#     p = split_l(a, t)
#     push_up(p[0])
#     push_up(p[1])
#     return p
#
#
# def split_r_node(a):
#     push_up(a)
#     a.push()
#     a.upd()
#     t = a.r
#     if t:
#         t.push()
#         t.upd()
#     a.r = None
#     upd_p(t, None)
#     a.upd()
#     p = split_r(a, t)
#     push_up(p[0])
#     push_up(p[1])
#     return p
#
#
# def getm(v):
#     return v.m if v else 0
#
#
# def getk(v):
#     return v.k if v else 0
#
#
# def getmn(v):
#     return v.mn if v else MN
#
#
# def get_ROOT(v):
#     push_up(v)
#     if v.h == 0:
#         return v.v
#     while v.mn > 1:
#         v = v.p
#     while v.h != 1:
#         v.push()
#         if getmn(v.l) <= 1:
#             v = v.l
#             v.push()
#             while getmn(v.r) <= 1:
#                 v = v.r
#                 v.push()
#         elif getmn(v.r) <= 1:
#             v = v.r
#             v.push()
#             while getmn(v.l) <= 1:
#                 v = v.l
#                 v.push()
#         else:
#             break
#     return v.v
#
#
# def add(v, val):
#     v.f += val
#     v.m += val
#     v.mn += val
#     v.h += val
#
#
# def main():
#     input = sys.stdin.read().split()
#     ptr = 0
#     q = int(input[ptr])
#     ptr += 1
#     m = int(input[ptr])
#     ptr += 1
#     sz = 1
#     la = 0
#     tin = [(Node(0, 0), Node(0, 0))]
#     root = merge(tin[0][0], tin[0][1])
#     g = [[]]
#     ROOT = 0
#     for _ in range(q):
#         c = input[ptr]
#         ptr += 1
#         x = int(input[ptr])
#         ptr += 1
#         x = (la * m + x - 1) % sz
#         if c == '+':
#             push_up(tin[x][0])
#             h = tin[x][0].h
#             tin.append((Node(sz, h + 1), Node(sz, h + 1)))
#             g[x].append(sz)
#             g.append([x])
#             NR = get_ROOT(tin[x][0])
#             h2 = root.m
#             p1 = split_l_node(tin[x][0])
#             p2 = split_l_node(tin[x][1])
#             root = merge(p1[0], merge(merge(p2[0], merge(tin[sz][0], tin[sz][1])), p2[1]))
#             if h == h2:
#                 p1 = split_l_node(tin[NR][0])
#                 p2 = split_r_node(tin[NR][1])
#                 if h + 1 - max(getm(p1[0]), getm(p2[1])) >= 2:
#                     add(p2[0], -1)
#                     p3 = split_l_node(tin[NR][1])
#                     t = merge(p1[0], p2[1])
#                     add(t, 1)
#                     t = merge(p3[0], t)
#                     root = merge(t, p3[1])
#                     ROOT = NR
#                 else:
#                     t = merge(p1[0], p2[0])
#                     root = merge(t, p2[1])
#             sz += 1
#         else:
#             push_up(tin[x][0])
#             h = tin[x][0].h
#             if x == ROOT:
#                 print(f"{root.m} {root.k // 2}")
#                 la = root.m + root.k // 2
#                 continue
#             NR = get_ROOT(tin[x][0])
#             p1 = split_l_node(tin[NR][0])
#             p2 = split_r_node(tin[NR][1])
#             m1 = getm(p1[0])
#             k1 = getk(p1[0])
#             m2 = getm(p2[1])
#             k2 = getk(p2[1])
#             if m1 == m2:
#                 k1 += k2
#             if m1 < m2:
#                 k1, k2 = k2, k1
#                 m1, m2 = m2, m1
#             k1 //= 2
#             print(f"{h + m1} {k1}")
#             la = h + m1 + k1
#             root = merge(merge(p1[0], p2[0]), p2[1])
#
#
# if __name__ == "__main__":
#     main()














# def main(file):
#     n = int(file.readline())
#     a = list(map(int, file.readline().split()))
#     a.sort()
#     dp = [[0] * n for _ in range(n)]
#     for i in range(n - 1, -1, -1):
#         dp[i][i] = 1
#         j = i
#         for k in range(i, n):
#             while j >= 0 and a[i] - a[j] <= a[k] - a[i]:
#                 j -= 1
#             if j < 0:
#                 break
#             dp[j][i] = max(dp[j][i], dp[i][k] + 1)   # кол - во зданий на которые можно перепрыгнуть, если прыжок был слева на право
#         for j in range(i - 1, -1, -1):
#             dp[j][i] = max(dp[j][i], dp[j + 1][i])
#
#     return max(dp[0])
#
#
#
# if __name__ == '__main__':
#     with open('input.txt', 'r') as file:
#         t = int(file.readline())
#         for _ in range(t):
#             print(main(file))








def my_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def main(file):
    q, n = list(map(int, file.readline().split()))

    ops = [list(map(my_int,
                    file.readline().split())) for _ in range(q)]
    cnt_action = 0
    deck = []
    for i in ops:
        if i[0] == "add":
            deck.append(i[1])



if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        t = int(file.readline())
        for _ in range(t):
            print(main(file))


















