'''
    TODO: 实现原地旋转
'''

inp = input().split()
r,c = int(inp[0]),int(inp[1])
img = []
# 输入
for i in range(r):
    inp = input().split()
    nums = [int(x) for x in inp]
    img.append(nums)
# 旋转
for j in range(c-1,-1,-1):
    for i in range(r):
        print(img[i][j], end=' ')
    print()