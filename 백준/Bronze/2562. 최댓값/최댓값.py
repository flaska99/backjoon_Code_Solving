li = [input() for _ in range(9)]
num_list = list((map(int, li)))
temp = 0
for i in num_list :
    if i > temp : temp = i
print(temp); print(num_list.index(temp)+1)   