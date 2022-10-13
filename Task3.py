# Создайте программу для игры в ""Крестики-нолики"".

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

win = True

a = "x"
b = "o"

print(f"{list[0]}  {list[1]}  {list[2]}")
print(f"{list[3]}  {list[4]}  {list[5]}")
print(f"{list[6]}  {list[7]}  {list[8]}")

whose_move = random.randint(1, 2)

if whose_move == 1:
    print("Ходят крестики x")
else:
    print("Ходят нолики o")
while win == True:
    if whose_move == 1:
            print("Куда поставить крестик?")
            choice = int(input())
            for i in range(0, len(list), +1):
                if list[i] == choice:
                    list[i] = "x"
                    print(f"{list[0]}  {list[1]}  {list[2]}")
                    print(f"{list[3]}  {list[4]}  {list[5]}")
                    print(f"{list[6]}  {list[7]}  {list[8]}")
            if a == list[0] and a == list[1] and a == list[2] or a == list[3] and a == list[4] and a == list[5] or a == list[6] and a == list[7] and a == list[8] or a == list[0] and a == list[3] and a == list[6] or a == list[1] and a == list[4] and a == list[7] or a == list[2] and a == list[5] and a == list[8] or a == list[6] and a == list[4] and a == list[2] or a == list[0] and a == list[4] and a == list[8]:
                print("Крестики выйграли!")
                win = False
                break
            whose_move += 1
    if whose_move == 2:
            print("Куда поставить нолик?")
            choice = int(input())
            for i in range(0, len(list),+1):
                if list[i] == choice:
                    list[i] = "o"
                    print(f"{list[0]}  {list[1]}  {list[2]}")
                    print(f"{list[3]}  {list[4]}  {list[5]}")
                    print(f"{list[6]}  {list[7]}  {list[8]}")
            if b == list[0] and b == list[1] and b == list[2] or b == list[3] and b == list[4] and b == list[5] or b == list[6] and b == list[7] and b == list[8] or b == list[0] and b == list[3] and b == list[6] or b == list[1] and b == list[4] and b == list[7] or b == list[2] and b == list[5] and b == list[8] or b == list[6] and b == list[4] and b == list[2] or b == list[0] and b == list[4] and b == list[8]:
                print("Нолики выйграли!")
                win = False
                break
            whose_move -= 1
