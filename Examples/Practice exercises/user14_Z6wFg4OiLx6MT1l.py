my_list = [0, 1]

x = 0
while x < 40:
    suma = my_list[len(my_list)-1] + my_list[len(my_list)-2]
    my_list.append(suma)
    x += 1

ultimo = my_list[-1]

print ultimo