import random  # Для генерации случайного числа
# Объявляем переменные
low_digit = 10  # Нижняя граница случайного числа
high_digit = 50  # Верхняя граница случайного числа
what_is_digit = 0  # Загаданное компьютером число
count_input = 0  # Количество попыток угадать
win_Flag = False  # Угадал текущее число?
play_game_Flag = True  # Продолжается ли игра?
x = ''  # Число, которое вводит пользователь
start_score = 100  # Начальное количество очков
score = 0  # Текущее количество очков
max_score = 100  # Максимальное за сессию игры

what_is_digit = random.randint(low_digit, high_digit)
print('Компьютер загадал число, попробуйте отгадать!')
print(f'Загаданное число: {what_is_digit}')

while (not x.isdigit()):
    x = input('Введите число: ')
    if (not x.isdigit()):
        print('Введите, пожалуйста, чиcло.')
