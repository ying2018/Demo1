# for i in range(10):
#     print(i+1)
#
# for i in range(10,0,-1):
#     print(i)
#
# flag = 10
# while flag:
#     print(flag)
#     flag -= 1
#
# for i in range(5):
#     print('welcome')
#
# for i in range(10):
#     if i % 2:
#         continue
#     print(i)
#
# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(0,10,2):
#     print(i)
#
# for i in range(0,10):
#     if i & 1:
#         print(i)
#
# count = 0
# for i in range(0,1000,7):
#     print(i)
#     count += 1
#     if count >= 20:
#         break


# # 打印边长为n的正方形
# n = int(input('请输入正方形边长'))
# print('*'*n)
# for i in range(n-2):
#     print('*',' '*(n-2),'*')
# print('*'*n)

# n = int(input('请输入正方形边长'))
# e = -n//2
# for i in range(e, n+e):
#     if i == e or i == n+e-1:
#         print('*'*n)
#     else:
#         print('*' + ' '*(n-2) + '*')


# # 100以内奇数的和
# sum = 0
# for i in range(1,100,2):
#     sum += i
# print(sum)
#
#
# # 判断学生成绩
# score = int(input('请输入成绩'))
# if score >= 80:
#     if score >= 90:
#         print('A')
#     else:
#         print('B')
# elif score >= 60:
#     if score >= 70:
#         print('C')
#     else:
#         print('D')
# else:
#     print('E')


# # 求1-5阶乘之和
# s = 1
# for a in range(1,5):
#     s *= a
# print(s)


# 给一个数，判断是否是素数（质数）质数：被1和它本身整除的自然数
# b = int(input('输入一个数'))
# for i1 in range(2, b):
#     if b % i1 == 0:
#         print('%d 不是素数' % b)
#         break
# else:
#     print('%d is a prime number！' % b)


# # 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, '*', i, '=', j*i, '\t', end='')
#     print()


# # 打印菱形
n = int(input('输入菱形行数'))
for i in range(1, n):
    for j in range(1, n-i):
        print(' ', end='')
    for k in range(2*i-1):
        print('*', end='')
    print('')
# 菱形的下半部分
for i in range(1, n):
    for j in range(i):
        print(' ', end='')
    for k in range(1, 2*(n-i)-2):
        print('*', end='')
    print('')

# # 打印100以内的斐波那契数列
# n1 = 1
# n2 = 1
# count = 2
# print(n1, ',', n2, end=' , ')
# while count <= 100:
#     nth = n1 + n2
#     print(nth, end=' , ')
#     n1 = n2
#     n2 = nth
#     count += 1
#     if nth > 100:
#         break


# 斐波那契数列第101项
