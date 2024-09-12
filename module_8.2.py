def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            return 'В numbers записан некорректный тип данных'

        sum_numbers, incorrect_data = personal_sum(numbers)

        if len(numbers) == incorrect_data:
            return 0

        average = sum_numbers / (len(numbers) - incorrect_data)
        return average

    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') 
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')