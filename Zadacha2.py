#дан списко a = [4, 3, -10, 1, 7, 12], изменить его а=[4, -10, 12, 3, 1, 7]

my_list = [4, 3, -10, 1, 7, 12]
#my_list[1] = -10
#my_list[2] = 12
#my_list[3] = 3
#my_list[4] = 1
#my_list[5] = 7
my_list.sort(key=lambda x: x%2)
print(my_list)

