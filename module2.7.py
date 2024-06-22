def print_param(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_param(c = [1,2,3])

value_list = 7, 'hello Pycharm', False
value_dict = {'a':7, 'b': 'Hello Pycharm', 'c': False}

print_param(*value_list)
print_param(**value_dict)

value_dict_2 = 54.32, 'Строка'
print_param(*value_dict_2, 42)


