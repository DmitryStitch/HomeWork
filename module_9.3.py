first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(name_1) - len(name_2) for name_1, name_2 in zip(first, second) if len(name_1) != len(name_2))
print(list(first_result))

second_result = (len(first[i]) > len(second[i]) for i in range(min(len(first), len(second))))
print(list(second_result))