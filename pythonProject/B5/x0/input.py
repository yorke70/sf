# def input_char():
#     print("Введите номер поля от 1 до 9 чтобы поставить символ: ")
#     char = ""
#     while not char:
#         char = int(input())
#         if char in
# play_field = [[i for i in range(1, 6)] for j in range(1, 6)]
# field = play_field[0]
# def print_field(play_field):
#     print("|" + "|".join(map(lambda x: "|".join(map(str, x)) + "|" + "\n",
#                          play_field)))
play_field = [i for i in range(1, 10)]
print_field = ["-" for i in range(1, 10)]
def pr_f(field):
    count = 0
    a = ""
    for i in field:
        count += 1
        a += "|" + str(i)
        if count == 3:
            print(a + "|")
            a = ""
            count = 0
pr_f(play_field)
pr_f(print_field)

char = input("Введи цифру блядь: ")
if char.isdigit():
    print("Введена цифра")
    char = int(char)
if char in play_field:
    play_field[char - 1] = "x"
    print_field[char - 1] = "x"
    pr_f(print_field)
else:
    print(type(char))
    print(f'{char} не в списке')
print(play_field)



