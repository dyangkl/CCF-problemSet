flag = True
last = 0
score = 0
numbers = input().split()
for number in numbers:
    number = int(number)
    if number == 1:
        last = 0
    if number == 2:
        number += last
        last = number
    score += number
    if number == 0:
        break
print(score)
