# coding=gbk

'''
Title: 火星A+B
读入两个不超过25位的火星正整数A和B，计算A+B。需要注意的是：在火星上，整数不是单一进制的，第n位的进制就是第n个素数。例如：地球上的10进制数2，在火星上记为“1,0”，因为火星个位数是2进制的；地球上的10进制数38，在火星上记为“1,1,1,0”，因为火星个位数是2进制的，十位数是3进制的，百位数是5进制的，千位数是7进制的…… 
Input
测试输入包含若干测试用例，每个测试用例占一行，包含两个火星正整数A和B，火星整数的相邻两位数用逗号分隔，A和B之间有一个空格间隔。当A或B为0时输入结束，相应的结果不要输出。 
Output
对每个测试用例输出1行，即火星表示法的A+B的值。 
Sample Input
1,0 2,1
4,2,0 1,2,0
1 10,6,4,2,1
0 0
Sample Output
1,0,1
1,1,1,0
1,0,0,0,0,0
'''
susu = [2,3]
num = 4
while True:
    for n in susu:
        if num % n == 0:
            break
        elif susu.index(n) == len(susu) - 1:
            susu.append(num)
    num += 1
    if len(susu) == 26:
        break

while True:
    inp = input()
    nums = inp.split()
    num1 = nums[0].split(',')
    num2 = nums[1].split(',')
    num1 = list(map(int, num1))
    num2 = list(map(int, num2))
    if num1[0] == 0 and num2[0] == 0 and len(num1) == 1 and len(num2) == 1:
        break
    result = []
    up = 0
    indexup = 0
    while True:
        tmp = num1[-1] + num2[-1] + up
        up = 0
        num1.pop()
        num2.pop()
        if tmp >= susu[indexup]:
            up = 1
            tmp = tmp - susu[indexup]
        
        result.append(tmp)
        indexup += 1
        if len(num1) == 0 and not len(num2) == 0:
            if num2[-1]+up >= susu[indexup]:
                for i in range(len(num2)-1, -1, -1):
                    num2[i] += up
                    if num2[i] >= susu[indexup]:
                        num2[i] -= susu[indexup]
                        up = 1
                        indexup += 1
                        if i == 0 and up == 1:
                            num2.insert(0,1)
                        
                    else:
                        up = 0
                        break                
            num2.reverse()
            result += num2
            break
        elif len(num2) == 0 and not len(num1) == 0:
            if num1[-1]+up >= susu[indexup]:
                for i in range(len(num1)-1, -1, -1):
                    num1[i] += up
                    if num1[i] >= susu[indexup]:
                        num1[i] -= susu[indexup]
                        up = 1
                        indexup += 1
                        if i == 0 and up == 1:
                            num1.insert(0,1)
                    else:
                        up = 0
                        break                
            num1.reverse()
            result += num1
            break
        elif len(num1) == 0 and len(num2) == 0:
            if up == 1:
                result.append(1)
            break
    result.reverse()
    print(result)
