import random
the_number = random.randint(1, 10)
guess = int(input("Угадайте число от 1 до 10: "))
while guess != the_number:
    if guess > the_number:
        print(guess, "Слишком велико. Попробуйте снова.")
    if guess < the_number:
        print(guess, "Слишком мало. Попробуйте снова.")
    guess = int(input("Еще одна попытка: "))
print(guess, "Правильное число! Вы победили!")