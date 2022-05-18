play_field = [i for i in range(1, 10)]
print_field = ["-" for i in range(1, 10)]
# for i in range(0, 9, 3):
#     field = ""
#     for y in range(1, 4):
#         field += "|" + str(y + i)
#         play_field.append(y + i)
#     field += "|"
#     print(field)


def input_char():
    field_print(play_field)
    print(f'Куда поставим "{gm_char}"')
    char = ""
    while not char:
        char = input()
        if char.isdigit():
            char = int(char)
        else:
            char = ""
            print("Нужно ввести цифру")
        if char in play_field:
            play_field[char - 1] = gm_char
            print_field[char - 1] = gm_char
            print(f'Ты поставил {gm_char} в поле {char}')
            field_print(print_field)
            print("===========")
        else:
            char = ""
            print("Нужно выбрать незанятое число от 1 до 9: ")


def field_print(field):
    count = 0
    a = ""
    for i in field:
        count += 1
        a += "|" + str(i)
        if count == 3:
            print(a + "|")
            a = ""
            count = 0


field_print(play_field)
gm_char = ""
print("Это наше игровое поле", "===========", sep="\n")

while not gm_char:
    gm_char = input("Введите символ 'х' или '0' которым будем играть: ")
    if gm_char == "x" or gm_char == "0":
        if gm_char == "x":
            print("===========", "Ты выбрал крестики", "===========", sep="\n")
        else:
            print("===========", "Ты выбрал нолики", "===========", sep="\n")
        break
    else:
        gm_char = ""
        print("Нужно ввести только 'x' или '0', попробуй снова")
