
'''
问题描述
　　给定一个年份y和一个整数d，问这一年的第d天是几月几日？
　　注意闰年的2月有29天。满足下面条件之一的是闰年：
　　1） 年份是4的整数倍，而且不是100的整数倍；
　　2） 年份是400的整数倍。
输入格式
　　输入的第一行包含一个整数y，表示年份，年份在1900到2015之间（包含1900和2015）。
　　输入的第二行包含一个整数d，d在1至365之间。
输出格式
　　输出两行，每行一个整数，分别表示答案的月份和日期。
样例输入
2015
80
样例输出
3
21
样例输入
2000
40
样例输出
2
9
'''

year = int(input())
dayNum = int(input())
# 月
monthNum = [31,28,31,30,31,30,31,31,30,31,30,31]
# 判断闰年
if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
    monthNum[1] = 29

month = 1
# 计算
for i in range(12):
    if dayNum > monthNum[i]:
        dayNum -= monthNum[i]
        month += 1
    else:
        day = dayNum
        break
# 打印
print(month)
print(day)