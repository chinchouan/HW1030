index_of_star = int(input("請輸入星星數量："))
half_index = int(index_of_star / 2)
# 上半三角形
for i in range(0, index_of_star - 1, 2):
    for j in range(half_index, int(i / 2), -1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()
# 中間
for i in range(index_of_star):
    print('*', end='')
print()
# 下半三角形
for i in range(index_of_star, 0, -2):
    for j in range(index_of_star, i - 1, -2):
        print(' ', end='')
    for j in range(i - (index_of_star % 2 + 1)):
        print('*', end='')
    print()
