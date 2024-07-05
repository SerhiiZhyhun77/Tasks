name = input("Как тебя зовут? ")
while name != "":
    for x in range(100):
        print(name, end=' ')
    print()
    name = input("Введите еще имя или нажмите [Enter], чтобы выйти: ")
print('Спасибо за игру!')
