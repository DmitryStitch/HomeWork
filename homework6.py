my_dict = {'Dima': 1992, 'Luda': 1993,}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Mama'))
my_dict.update({'Papa': 1966, 'Zhenya' : 1993})
a = my_dict.pop('Papa')
print(a)
print(my_dict)


my_set = {1, 2, 'бананы', 2, 3.14, 1, 'бананы',3.14}
print(my_set)
my_set = {1, 2, 'бананы', 2, 3.14, 1, 'бананы',3.14, 6, 7, 'яблоки'}
print(my_set.discard('бананы'))
print(my_set)
