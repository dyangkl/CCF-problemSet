
'''
问题描述
　　消除类游戏是深受大众欢迎的一种游戏，游戏在一个包含有n行m列的游戏棋盘上进行，棋盘的每一行每一列的方格上放着一个有颜色的棋子，当一行或一列上有连续三个或更多的相同颜色的棋子时，这些棋子都被消除。当有多处可以被消除时，这些地方的棋子将同时被消除。
　　现在给你一个n行m列的棋盘，棋盘中的每一个方格上有一个棋子，请给出经过一次消除后的棋盘。
　　请注意：一个棋子可能在某一行和某一列同时被消除。
输入格式
　　输入的第一行包含两个整数n, m，用空格分隔，分别表示棋盘的行数和列数。
　　接下来n行，每行m个整数，用空格分隔，分别表示每一个方格中的棋子的颜色。颜色使用1至9编号。
输出格式
　　输出n行，每行m个整数，相邻的整数之间使用一个空格分隔，表示经过一次消除后的棋盘。如果一个方格中的棋子被消除，则对应的方格输出0，否则输出棋子的颜色编号。
样例输入
4 5
2 2 3 1 2
3 4 5 1 4
2 3 2 1 3
2 2 2 4 4
样例输出
2 2 3 0 2
3 4 5 0 4
2 3 2 0 3
0 0 0 4 4
样例说明
　　棋盘中第4列的1和第4行的2可以被消除，其他的方格中的棋子均保留。
样例输入
4 5
2 2 3 1 2
3 1 1 1 1
2 3 2 1 3
2 2 3 3 3
样例输出
2 2 3 0 2
3 0 0 0 0
2 3 2 0 3
2 2 0 0 0
样例说明
　　棋盘中所有的1以及最后一行的3可以被同时消除，其他的方格中的棋子均保留。
评测用例规模与约定
　　所有的评测用例满足：1 ≤ n, m ≤ 30。
'''

n,m = [int(x) for x in input().split()]
# 记录消除的位置
eliminate = []
panel = []
for i in range(n):
    read = input().split()
    panel.append(read)
# 遍历行
for i in range(n):
    rcnt = 0
    for j in range(1,m):
        if panel[i][j] == panel[i][j-1]:
            rcnt += 1
            if rcnt == 2:
                eliminate.append((i, j))
                eliminate.append((i, j-1))
                eliminate.append((i, j-2))
            if rcnt > 2:
                eliminate.append((i,j))
        else:
            rcnt = 0
# 遍历列
for i in range(m):
    ccnt = 0
    for j in range(1,n):
        if panel[j][i] == panel[j-1][i]:
            ccnt += 1
            if ccnt == 2:
                if (j, i) not in eliminate:
                    eliminate.append((j, i))
                if (j-1, i) not in eliminate:
                    eliminate.append((j-1, i))
                if (j-2, i) not in eliminate:
                    eliminate.append((j-2, i))
            if ccnt > 2:
                if (j, i) not in eliminate:
                    eliminate.append((j, i))
        else:
            ccnt = 0
# 置0
for e in eliminate:
    r = e[0]
    c = e[1]
    panel[r][c] = '0'
# 打印
for i in range(n):
    print(' '.join(panel[i]))