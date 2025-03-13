num = int(input())
for i in range(num) :
    li = list(input())
    temp = 0; score = 0
    for j in li :
        if j == 'O' : temp += 1; score += temp
        else : temp = 0
    print(score)