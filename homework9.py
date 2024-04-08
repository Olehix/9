def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()

print_params(3)

print_params(b = 25)

print_params(c = [1, 2, 3])




values_list = [145, 'OK', False]

print_params(*values_list)

values_dict = {'a': 20, 'b': 'строчка', 'c': True}

print_params(**values_dict)



values_list2 = [789, True]

print_params(*values_list2, 42)
