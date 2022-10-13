# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
result = ""
count = 1
for i in range(0, len(text)-1, +1):
    if text[i] == text[i+1]:
        count += 1
    else:
        result += str(count) + text[i]
        count = 1
print(result) 
print()
result_new = ""
current = ""
for i in range(len(result)):
        if not result[i].isalpha():
            current += result[i]
        else:
            result_new += result[i] * int(current)
            current = ""
print(result_new)