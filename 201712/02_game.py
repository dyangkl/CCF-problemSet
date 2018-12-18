'''
    TODO:有n个小朋友围成一圈玩游戏，小朋友从1至n编号，2号小朋友坐在1号小朋友的顺时针方向，3号小朋友坐在2号小朋友的顺时针方向，……，1号小朋友坐在n号小朋友的顺时针方向。
　　TODO:游戏开始，从1号小朋友开始顺时针报数，接下来每个小朋友的报数是上一个小朋友报的数加1。若一个小朋友报的数为k的倍数或其末位数（即数的个位）为k，则该小朋友被淘汰出局，不再参加以后的报数。当游戏中只剩下一个小朋友时，该小朋友获胜。
'''
nums = input().split()
n = int(nums[0])
k = int(nums[1])

number = 0
index = -1
littleFirend = list(range(1,n+1))
while True:
    number += 1
    index = (index + 1) % len(littleFirend)
    if number % k == 0 or number % 10 == k:
        littleFirend.pop(index)
        index -= 1
    if len(littleFirend) == 1:
        break
print(littleFirend[0])