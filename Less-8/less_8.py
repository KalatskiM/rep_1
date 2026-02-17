#напишите программу. Есть две переменные salary и bonus. Salary - int, bonus - bool.
#Спросите у пользователя salary. А bonus пусть назначается рандомом.
#Если bonus - true, то к salary должен быть добавлен рандомный бонус
#Примеры результатов:
#10000, True - '$10255'
#25000, False - '$25000"
#600, True - '$3785'


import random

bonus = [True,  False]

def give_a_bonus(entered_salary = int(input('Введите зэпку '))):
        selected_bonus = random.choice(bonus)
        if selected_bonus is True:
            print(f'{entered_salary}, {selected_bonus} - ${(entered_salary) + random.random()*10}')
        elif selected_bonus is False:
            print(entered_salary)



give_a_bonus()
#приделать цикл до exit
