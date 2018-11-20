# 最小差值
n = eval(input())
li = list(map(int,input().split()))
# 列表排序
li.sort()

# 后一项减去前一项的差值
difference = list(map(lambda x , y : y - x , li[: -1] , li[ 1:]))

print(min(difference))