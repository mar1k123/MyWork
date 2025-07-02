# a = int(input.txt())
# min = 1000
# for i in range(a):
#     n = int(input.txt())
#     if n < min:
#         min = n
# print(min)
# if min < -15:
#     print("yes")
# else:
#     print("NO")
from typing import List


# a = []
# while True:
#     n = int(input.txt())
#     if n == 0:
#         break
#     if n // 100 == 0 and n // 10 != 0:  ## if n >= 10 and n < 100 или if len(str(n)) == 2
#         a.append(n)
#
#
# if a:
#     s = 0
#     for n in a:
#         s += n
#     SR = s / len(a)
#     print(SR)
# else:
#     print("NO")



# концепт функции Filter() фильтрует все значения по нашему условию
# numbers = [1,3,9,12,24,2,14,12,13,27]
# result = list(filter(lambda x: x % 3 == 0, numbers))
# print(result)


# концепт функции reduce() позволила свести список к одному значению
# from functools import reduce
# items = [10, 20, 30, 40, 50]
# result = reduce(lambda x,y: x + y, items)
# print(result)

# n = 1
# for i in range(5):
#     n = n * i\
# print(n)
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


# def rotate(matrix: List[List[int]]) -> None:
#     new_matrix = []
#     for i in range(len(matrix[0])):
#         current_sublist = []
#         for sublist in matrix[::-1]:
#             current_sublist.append(sublist[i])
#         new_matrix.append(current_sublist)
#     return new_matrix
# print(rotate(matrix))


# max = 0
# b = False
# n = int(input.txt())
# for i in range(n):
#     a = int(input.txt())
#     if a > max:
#         max = a
#     if a < 30:
#         b = True
# print(max)
# print("YES" if b == True else "NO")

# cnt = 0
# a = int(input.txt())
# while a != 0:
#     if a % 4 == 0 and 99 < a < 1000:
#         cnt += 1
#     a = int(input.txt())
# print(cnt)


# min = 301
# b = False
# a = int(input.txt())
# for i in range(a):
#     n = int(input.txt())
#     if n < min:
#         min = n
#     if n > 80:
#         b = True
# print(min)
# print("YES" if b == True else "NO")
# summi = 0
# a = int(input.txt())
# while a != 0:
#     if a % 6 == 0 and a % 10 == 4:
#         summi += a
#     a = int(input.txt())
# print(summi)
# for x in range(1000, 0, -1):
#     if not(x < 9) and not(x % 2 != 0):
#         print(x)














