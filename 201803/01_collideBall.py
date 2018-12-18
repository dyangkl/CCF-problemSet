inputs = input().split()
n = int(inputs[0])
l = int(inputs[1])
t = int(inputs[2])
balls = input().split()
for b in range(n):
    balls[b] = int(balls[b])
places = [1]*n
for time in range(t):
    for p in range(n):
        # 到右端点
        if balls[p] == l:
            places[p] = (places[p] + 1) % 2
        # 到左端点
        if balls[p] == 0 and places[p] == 0:
            places[p] = (places[p]+ 1) % 2
        # 碰撞
        collide = [ i for i,v in enumerate(balls) if v == balls[p]]
        if not len(collide) == 1:
            places[collide[0]] = (places[collide[0]] + 1) % 2
            places[collide[1]] = (places[collide[1]] + 1) % 2
        if places[p] == 1:
            balls[p] += 1
        else:
            balls[p] -= 1

for i in balls:
    print(i, end=' ')