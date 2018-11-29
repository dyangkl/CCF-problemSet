'''
 遇到的坑：
    末尾斜杠的完全匹配；
    输出第一个匹配成功的规则；
    注意没有参数的情况；
    数字匹配去掉前导0；
    参数为空的情况；
'''
import re
ruleNum,dataNum = input().split()
ruleNum = int(ruleNum)
dataNum = int(dataNum)
rules = []
datas = []
for rule in range(ruleNum):
    rules.append(input().split())
    rules[rule][0] = rules[rule][0].replace('<int>', r'0*([\d]*)')
    rules[rule][0] = rules[rule][0].replace('<str>', r'([a-zA-Z0-9-_.]*)')
    rules[rule][0] = rules[rule][0].replace('<path>', r'([a-zA-Z0-9-_./]*)')
    rules[rule][0] = re.compile('^' + rules[rule][0] + '$')
for data in range(dataNum):
    datas.append(input())
for d in range(dataNum):
    data = datas[d]
    flag = 0
    for r in range(ruleNum):
        matchResult = rules[r][0].findall(data)
        if '' in matchResult:
            break
        if not len(matchResult) == 0:
            flag = 1
            print(rules[r][1],end=' ')
            for item in matchResult:
                if type(item) == tuple:
                    for it in item:
                        print(it,end=' ')

                else:

                    if not item == datas[d]:
                        print(item,end=' ')
            print()
            break
        if rules[r][0].match(data):
            flag = 1
            print(rules[r][1])
            break
    if not flag == 1:
        print('404')

