import random

low_digit = 10
high_digit = 50
digit = 0
count_input = 0
win = False
play_game = True
x = 0
start_score = 100
score = 0
max_score = 100

digit = random.randint(low_digit, high_digit)
print('Компьютер загадал число, попробуйте отгадать!')
print(f'Загаданное число: {digit}')