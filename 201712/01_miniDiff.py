
'''
    TODO:求给定数的最小差
    输入都是字符串
'''

n = int(input())
nums = input().split()
for i in range(n):
    nums[i] = int(nums[i])

nums.sort()
dif = 10001
for j in range(n-1):
    tmpDif = nums[j] - nums[j+1] if nums[j] - nums[j+1] > 0 else nums[j+1] - nums[j]
    if tmpDif < dif:
        dif = tmpDif
print(dif)



