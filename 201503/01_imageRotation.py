
'''
问题描述
　　旋转是图像处理的基本操作，在这个问题中，你需要将一个图像逆时针旋转90度。
　　计算机中的图像表示可以用一个矩阵来表示，为了旋转一个图像，只需要将对应的矩阵旋转即可。
输入格式
　　输入的第一行包含两个整数n, m，分别表示图像矩阵的行数和列数。
　　接下来n行每行包含m个整数，表示输入的图像。
输出格式
　　输出m行，每行包含n个整数，表示原始矩阵逆时针旋转90度后的矩阵。
样例输入
2 3
1 5 3
3 2 4
样例输出
3 4
5 2
1 3
评测用例规模与约定
　　1 ≤ n, m ≤ 1,000，矩阵中的数都是不超过1000的非负整数。
'''
'''
    TODO: 不是原地旋转
'''

inp = input().split()
r,c = int(inp[0]),int(inp[1])
img = []
newimg = []
# 输入
for i in range(r):
    inp = input().split()
    nums = [int(x) for x in inp]
    img.append(nums)
# 旋转
for j in range(c-1, -1, -1):
    tmp = []
    for i in range(r):
        tmp.append(img[i][j])
    newimg.append(tmp)
# 输出
for i in range(c):
    for j in range(r):
        print(newimg[i][j], end=' ')
    print()