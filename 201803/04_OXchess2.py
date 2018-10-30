from copy import deepcopy


# 判断是否结束：行、列、对角相等；A 获胜返回 1，B 获胜返回 2；未结束返回 0
def end(now):
    # 行相等
    for i in range(3):
        if now[i][0] == now[i][1] == now[i][2] == 1:
            return 1
        elif now[i][0] == now[i][1] == now[i][2] == 2:
            return 2
    # 列相等
    for j in range(3):
        if now[0][j] == now[1][j] == now[2][j] == 1:
            return 1
        elif now[0][j] == now[1][j] == now[2][j] == 2:
            return 2
    # 对角相等
    if now[0][0] == now[1][1] == now[2][2] == 1 or now[0][2] == now[1][1] == now[2][0] == 1:
        return 1
    if now[0][2] == now[1][1] == now[2][0] == 2 or now[0][0] == now[1][1] == now[2][2] == 2:
        return 2
    # 未获胜，返回 0
    return 0


def get_next(cur_node, player, point):
    i = int(point / 3)
    j = point % 3
    node = deepcopy(cur_node)
    node[i][j] = player
    return node


def res(end, node):
    if end == 1:  # win
        res = 1
        for i in range(3):
            for j in range(3):
                if not node[i][j]:
                    res += 1
    elif end == 2:  # lose
        res = -1
        for i in range(3):
            for j in range(3):
                if not node[i][j]:
                    res -= 1
    return res


def maxmin(player, cur_node, alph, bet):
    # 将判断是否结束的返回值赋值给变量 en
    en = end(cur_node)
    # 如果结束，返回分数，正负
    if en:
        return res(en, cur_node)

    # 存棋盘元素为 0 的元素位置
    node_list = []  # 0-8
    # 遍历当前棋盘
    for i in range(3):
        for j in range(3):
            # 如果是 0
            if not cur_node[i][j]:
                # 将位置添加到 node_list 数组中，位置 = 行 * 3 + 列
                node_list.append(i * 3 + j)
    # 为 0 的元素个数
    blank = len(node_list)

    # 如果为 0 个数为 0，返回 0
    if not blank:  # ping
        return 0
    print(cur_node[0],'\n',cur_node[1],'\n',cur_node[2])
    print()

    # 变量 alph,bet
    alpha = alph
    beta = bet
    if player == 1:
        # best = 0-blank
        alpha = -10
        for i in node_list:
            new_node = get_next(cur_node, player, i)

            val = maxmin(2, new_node, alpha, beta)
            if val >= beta:
                return val
            if val >= alpha:
                alpha = val
        print('alpha',alpha)
        return alpha
    else:  # 2
        # best = blank
        beta = 10
        for i in node_list:
            new_node = get_next(cur_node, player, i)
            val = maxmin(1, new_node, alpha, beta)  # 1
            if val <= alpha:
                return val
            if val <= beta:
                beta = val
        print('beta',beta)
        return beta


n = int(input())
inp = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
for i in range(n):
    for j in range(3):
        a = input().split()
        inp[j][0] = int(a[0])
        inp[j][1] = int(a[1])
        inp[j][2] = int(a[2])

    result = maxmin(1, inp, -10, 10)
    print(result)

