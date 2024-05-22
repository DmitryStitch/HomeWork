x = 54
print('Найс')
if x < 0:
     print('меньше нуля')
print('Пока')

a, b = 4, 8
if a < b:
     print('a < b')
if a < b and a > 0:
     print('работает')
if (a > b) and (a > 0 or b < 15):
     print('работает')
if 5 < b and b < 10:
     print('работает')

if '64' > '456':
     print('победа')
if '135' > '13':
     print('победа')
if [2, 3] > [2, 2]:
     print('победа')

if '7' > 3:
    print('не работает')
if [3, 6, 9] > 3:
    print('не работает')

# но
if '7' != 3:
    print('работает')
