# coding=gbk

'''
Title: ����A+B
��������������25λ�Ļ���������A��B������A+B����Ҫע����ǣ��ڻ����ϣ��������ǵ�һ���Ƶģ���nλ�Ľ��ƾ��ǵ�n�����������磺�����ϵ�10������2���ڻ����ϼ�Ϊ��1,0������Ϊ���Ǹ�λ����2���Ƶģ������ϵ�10������38���ڻ����ϼ�Ϊ��1,1,1,0������Ϊ���Ǹ�λ����2���Ƶģ�ʮλ����3���Ƶģ���λ����5���Ƶģ�ǧλ����7���Ƶġ��� 
Input
��������������ɲ���������ÿ����������ռһ�У�������������������A��B������������������λ���ö��ŷָ���A��B֮����һ���ո�������A��BΪ0ʱ�����������Ӧ�Ľ����Ҫ����� 
Output
��ÿ�������������1�У������Ǳ�ʾ����A+B��ֵ�� 
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
