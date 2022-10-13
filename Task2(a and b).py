# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random


sweets = 150
whose_move = random.randint(1, 2)

if whose_move == 1:
    print("Первый ход делает Игрок №1!")
else:
    print("Первый ход делает Бот!")
if whose_move == 1:
    while sweets > 28:
        print("Игрок №1, бери конфеты!")
        sweet_current = int(input())
        if sweet_current > 28:
            print("Жульничество! Вы пропускаете ход!")
        else:
            sweets -= sweet_current
            whose_move += 1
            print(f"Осталось {sweets} конфет")
        print("Бот, бери конфеты!")
        sweet_current = random.randint(1, 28)
        print(f"Бот взял {sweet_current} конфет")
        sweets -= sweet_current
        whose_move -= 1
        print(f"Осталось {sweets} конфет")
    while sweets > 0:
        if whose_move == 1:
            print("Игрок №1, бери конфеты!")
            sweet_current = int(input())
            if sweet_current > sweets:
                print("Жульничество! Вы пропускаете ход!")
            else:
                if sweet_current == sweets:
                    print("Игрок №1 победил!")
                    break
                else:
                    sweets -= sweet_current
                    whose_move += 1
                    print(f"Осталось {sweets} конфет")
            print("Бот, бери конфеты!")
            sweet_current = sweets
            print(f"Бот взял {sweet_current} конфет")
            print("Бот победил!")
            break
        else:
            print("Бот, бери конфеты!")
            sweet_current = sweets
            print(f"Бот взял {sweet_current} конфет")
            print("Бот победил!")
            break

else:
    while sweets > 28:
        print("Бот, бери конфеты!")
        sweet_current = random.randint(1, 28)
        print(f"Бот взял {sweet_current} конфет")
        sweets -= sweet_current
        whose_move -= 1
        print(f"Осталось {sweets} конфет")
        print("Игрок №1, бери конфеты!")
        sweet_current = int(input())
        if sweet_current > 28:
            print("Жульничество! Вы пропускаете ход!")
        else:
            sweets -= sweet_current
            whose_move += 1
            print(f"Осталось {sweets} конфет")
    while sweets > 0:
        if whose_move == 1:
            print("Игрок №1, бери конфеты!")
            sweet_current = int(input())
            if sweet_current > sweets:
                print("Жульничество! Вы пропускаете ход!")
            else:
                if sweet_current == sweets:
                    print("Игрок №1 победил!")
                    break
                else:
                    sweets -= sweet_current
                    whose_move += 1
                    print(f"Осталось {sweets} конфет")
            print("Бот, бери конфеты!")
            sweet_current = sweets
            print(f"Бот взял {sweet_current} конфет")
            print("Бот победил!")
            break
        else:
            print("Бот, бери конфеты!")
            sweet_current = sweets
            print(f"Бот взял {sweet_current} конфет")
            print("Бот победил!")
            break

                    