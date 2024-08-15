team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 7
print('В команде Мастера кода участников: %s' % team1_num)
team2_num = 8
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
score_1 = 44
print('Команда Мастера кода решила задач: {}'.format(score_1))
score_2 = 34
print('Команда Волшебники данных решила задач: {}'.format(score_2))
team1_time = 1552.512
team2_time = 2153.31451
print('Волшебники данных решили задачи за {} с.'.format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
challenge_result = 'Результат битвы: победа команды '
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
time_avg = float('{:.3f}'.format(time_avg))
result1 = team1_time / score_1
result2 = team2_time / score_2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
if (score_1 > score_2 and team1_time < team2_time or score_1 > score_2 and team1_time > team2_time and result1 < result2
    or score_1 == score_2 and team1_time < team2_time):
    print(challenge_result + team1_name)
elif (score_1 < score_2 and team1_time > team2_time or score_1 < score_2 and team1_time < team2_time and result1 > result2
    or score_1 == score_2 and team1_time > team2_time):
    print(challenge_result + team2_name)
else:
    print("Ничья")
