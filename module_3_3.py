def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ['мир', False, 25]
values_dict = {'a': 45, 'b': 56, 'c': 23}
values_list_2 = ['сложно', 28]
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)