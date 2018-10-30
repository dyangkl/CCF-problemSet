cnt = int(input())

chesss = []
chess = []
for c in range(cnt*3):
    steps = input().split()
    chess.append(steps)
    if len(chess) == 3:
        chesss.append(chess)
        chess=[]

#
def minmax(chess):


for chess in chesss:
    score = 0
    for item in range(3):
        score += chess[item].count('0')
    flagx = 1
    flagy = 1
    for a in range(3):
        for b in range(3):
            flagx *= int(chess[a][b])
            flagy *= int(chess[b][a])

        if flagy == 1 or flagx == 1:
            print(1+score)
            break
        elif flagx == 8 or flagy == 8:
            print(-1-score)
            break
        flagy = 1
        flagx = 1
    if chess[0][0] == chess[1][1] == chess[2][2] == '1':
        print(1+score)
    elif chess[0][0] == chess[1][1] == chess[2][2] == '2':
        print(-1-score)
    else:





