import random
secret = "Я задумав число від 1 до 1000"
case = random.randint(1, 1000)
print(secret)
attempt = 0
_input = 0
while _input != case:
    attempt += 1
    print("Вгадай число: ", end="")
    _input = int(input())
    if _input < case:
        print("Мало")
    if _input > case:
        print("Багато")
    if _input == case:
        print("Вгадав!")
print(f"Вгадано за {attempt} спроб.")