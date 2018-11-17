
'''
问题描述
　　请实现一个铁路购票系统的简单座位分配算法，来处理一节车厢的座位分配。
　　假设一节车厢有20排、每一排5个座位。为方便起见，我们用1到100来给所有的座位编号，第一排是1到5号，第二排是6到10号，依次类推，第20排是96到100号。
　　购票时，一个人可能购一张或多张票，最多不超过5张。如果这几张票可以安排在同一排编号相邻的座位，则应该安排在编号最小的相邻座位。否则应该安排在编号最小的几个空座位中（不考虑是否相邻）。
　　假设初始时车票全部未被购买，现在给了一些购票指令，请你处理这些指令。
输入格式
　　输入的第一行包含一个整数n，表示购票指令的数量。
　　第二行包含n个整数，每个整数p在1到5之间，表示要购入的票数，相邻的两个数之间使用一个空格分隔。
输出格式
　　输出n行，每行对应一条指令的处理结果。
　　对于购票指令p，输出p张车票的编号，按从小到大排序。
样例输入
4
2 5 4 2
样例输出
1 2
6 7 8 9 10
11 12 13 14
3 4
样例说明
　　1) 购2张票，得到座位1、2。
　　2) 购5张票，得到座位6至10。
　　3) 购4张票，得到座位11至14。
　　4) 购2张票，得到座位3、4。
评测用例规模与约定
　　对于所有评测用例，1 ≤ n ≤ 100，所有购票数量之和不超过100。
'''

# 购票信息
n = int(input())
buyTicketsInfo = [int(x) for x in input().split()]
# 存该排剩余位置个数
seatsInfo = [5] * 20
result = []

for buyInfoIndex in range(n):
    result.append([])
    for lineIndex in range(20):
        if seatsInfo[lineIndex] >= buyTicketsInfo[buyInfoIndex]:
            # 开始和结束的座位下标
            start = lineIndex * 5 + 5 - seatsInfo[lineIndex]
            end = start + buyTicketsInfo[buyInfoIndex] - 1
            seatsInfo[lineIndex] -= buyTicketsInfo[buyInfoIndex]
            for index in range(start, end + 1):
                result[buyInfoIndex].append(index)
            break
    else:
        for lineIndex in range(20):
            if seatsInfo[lineIndex] >= 0:
                # 开始和结束的座位下标
                start = lineIndex * 5 + 5 - seatsInfo[lineIndex]
                end = start + buyTicketsInfo[buyInfoIndex] - 1
                if end >= 5:
                    end = lineIndex * 5 + 4
                    buyTicketsInfo[buyInfoIndex] -= end - start + 1
                    seatsInfo[lineIndex] = 0
                else:
                    buyTicketsInfo[buyInfoIndex] = 0
                for index in range(start, end + 1):
                    result[buyInfoIndex].append(index)
                if buyTicketsInfo[buyInfoIndex] == 0:
                    break

for i in range(n):
    outInfo = [str(x + 1) for x in result[i]]
    print(' '.join(outInfo))