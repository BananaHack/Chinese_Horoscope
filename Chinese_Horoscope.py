from datetime import datetime
from time import sleep
from os import system, name

# проверка корректности пользовательского ввода
def is_valid(y):
    try:
        int(y)
        return True
    except ValueError:
        return False
		


# очистка экрана для нового запуска
def cls():
    system('cls' if name=='nt' else 'clear')
	
# функция определения года по китайскому календарю	
def Chinese_Horoscope(y):
        animals = ["Обезьяны", "Петуха", "Собаки", "Свиньи", "Крысы", "Быка", "Тигра", "Зайца", "Дракона", "Змеи", "Лошади", "Овцы"]
        x = y % 12
        if y == currentYear: print('Этот год является годом', animals[x])
        elif y < currentYear: print('Этот год был годом', animals[x])
        elif y > currentYear: print('Этот год будет годом', animals[x])

# варианты написания ответов на вопрос о продолжении или же завершении программы		
one_more_time = ['ещё', 'еще', 'to~','tot']
the_exit = ['выход','ds[jl']
print('Добро пожаловать в программу по определению года по китайскому календарю.\n')
sleep(2)

while True:
    year, currentYear  = input('Введите год по григорианскому календарю:  '), datetime.now().year
	
    if is_valid(year) == False:
        print('Пожалуйста, введите целое число...\n\n')
        sleep(2)
        continue
	
    else: Chinese_Horoscope(int(year))
	
    while True:
        repeat = input('\nВведите "Ещё", чтобы сыграть ещё раз или "Выход", чтобы закрыть игру:  ')
        if repeat.lower() in one_more_time:
            print()
            break

        elif repeat.lower() in the_exit:
            exit()
			
    cls()
    print('Определение года по китайскому календарю\n')
    continue