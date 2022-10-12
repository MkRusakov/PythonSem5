# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def function (text):
    result = []
    list = text.split()
    for i in list:
        current = i.lower()
        if "абв" not in current:
            result.append(i)
    new = " ".join(result)
    print(new)
text = "Абван создаёт чудный соабвку"
function(text)
