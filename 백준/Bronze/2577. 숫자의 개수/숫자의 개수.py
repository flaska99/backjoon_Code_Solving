import sys
temp = 1 # 초기화
num_list = [int(sys.stdin.readline().strip()) for _ in range(3)] 
# num_list [150, 266, 427]
for i in num_list: temp *= i 
# temp = 150 * 266 * 427 = 17037300
num_list_times = [num for num in str(temp)] 
# num_list_times = ['1', '7', '0', '3', '7', '3', '0', '0']

for i in range(10) :
    count = 0
    for j in num_list_times :
        if i == int(j) :
            count += 1
    print(count)
