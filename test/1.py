import random

attempt = 0
_input = 0


def init_game():
    global attempt, _input
    secret = "Я задумав число від 1 до 1000"
    print(secret)


def play_game():
    global attempt, _input
    case = random.randint(1, 1000)
    while _input != case:
        print("Вгадай число: ", end="")
        _input = int(input())
        attempt += 1
        if _input < case:
            print("Занадто маленьке!")
        if _input > case:
            print("Занадто велике!")
        if _input == case:
            print("Правильно!")


def end_game():
    print("Ти спробував " + str(attempt) + " разів.")


# main program
init_game()
play_game()
end_game()
