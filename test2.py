
rows = int(input('输入列数'))
i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# 打印直角等腰三角形
for i in range(0, rows):
    for k in range(0, rows-i):
        print('*', end=' ')
        k += 1
    i += 1
    print()
# 打印等边三角形
for i in range(0, rows + 1):
    for j in range(0, rows-i):
        print(' ',end='')
        j += 1
    for k in range(0, 2*i-1):
        if k == 0 or k == 2*i-2 or i == rows:
            if i == rows:
                if k % 2 == 0:  # 从0开始，偶数打印* 奇数打印空格
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                print('*', end='')
        else:
            print(' ',end='')
        k += 1
    print()
    i += 1
# 打印菱形
for i in range(rows):
    for j in range(rows-i):
        print(' ', end='')
        j += 1
    for k in range(2*i-1):
        if k == 0 or k == 2*i-2:
            print('*', end='')
        else:
            print(' ', end='')
        k += 1
    print('')
    i += 1
# 菱形的下半部分
for i in range(rows):
    for j in range(i):
        print(' ', end=''),
        j += 1
    for k in range(2*(rows-i)-1):
        if k == 0 or k == 2*(rows-i)-2:
            print('*', end=''),
        else:
            print(' ', end='')
        k += 1
    print('')
    i += 1
