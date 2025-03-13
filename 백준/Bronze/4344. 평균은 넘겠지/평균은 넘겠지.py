num = int(input())
for i in range(num) :
    score = 0
    count = 0
    num_list = list(map(int,(input().split())))
    for j in range(1, num_list[0] + 1, 1):
        score += num_list[j]
    average = score/num_list[0]
    for j in range(1, num_list[0] + 1, 1):
        if num_list[j] > average : count += 1
    
    answer = format(count/num_list[0] * 100 , ".3f")
    print(answer + '%')
