
'''
CSS 选择器
测试用例：
11 5
html
..head
....title
..body
....h1
....p #subtitle
....div #main
......h2
......p #one
......div
........p #two
p
#subtitle
h3
div p
div div p
'''


# 读
n, m = [int(x) for x in input().split()]
# 存放HTML信息和CSS选择器信息
html = []
cssSelect = []
# 读HTML，并将HTML以 缩进量，HTML标签，ID 格式的元组保存
for i in range(n):
    r = input()
    level = r.count('.')
    if ' #' in r:
        label, id = r[level:].split()
    else:
        label = r[level:]
        id = ''
    html.append(((level+1)//2, label, id))

# 读CSS选择器，并直接打印选择结果
for i in range(m):
    # 读CSS选择
    cs = input().split()
    # 匹配的数量
    cnt = 0
    # 匹配的HTML行数
    lineNum = []
    # 当只有一层选择
    if len(cs) == 1:
        # 当根据 ID 选择
        if cs[0].startswith('#'):
            for i in range(len(html)):
                if html[i][2] == cs[0]:
                    cnt += 1
                    lineNum.append(i+1)
        # 当根据标签名选择
        else:
            for i in range(len(html)):
                if html[i][1] == cs[0]:
                    cnt += 1
                    lineNum.append(i+1)
    # 当有多层选择
    else:
        # 上一次是否匹配
        last = False
        # 当前html层级
        deep = -1
        # 选择器层级
        cDeep = 0
        # 遍历HTML
        for hi in range(len(html)):
            # 遍历每一层选择器
            for i in range(cDeep, len(cs)):
                # 当前层根据 ID 选择
                if cs[i].startswith('#'):
                    mi = 2
                # 根据标签名选择
                else:
                    mi = 1

                # 完全匹配
                if cs[i] == html[hi][mi] and i == len(cs) - 1:
                    cnt += 1
                    lineNum.append(hi + 1)
                    deep = -1
                    cDeep = 0
                    last = False
                    break
                # print('i ',i, '   hi  ', hi, ' c  ',cs[i], '  h  ', html[hi], '  m  ', mi, '  deep ', deep, '  cDeep  ', cDeep)

                # 匹配
                # 匹配成功
                if cs[i] == html[hi][mi]:
                    last = True
                    cDeep = i + 1
                    deep = html[hi][0]
                    break
                elif deep <= html[hi][0] and last:
                    cDeep = i
                    deep = html[hi][0]
                    break
                else:
                    cDeep = 0
                    deep = -1
                    last = False
                    break

    print(cnt, end=' ')
    print(' '.join([str(x) for x in lineNum]))