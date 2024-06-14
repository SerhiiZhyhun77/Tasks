import random


def initGame():
    secret = "Я задумав число від 1 до 1000"
    print(secret)
    attempt = 0
    input = 0

def playGame():
    case = random.randint(1, 1000)
    while input != case:
        print("Вгадай число: ", end="")
        input = int(input())
        attempt += 1
        if input < case:
            print("Занадто маленьке!")
        if input > case:
            print("Занадто велике!")
        if input == case:
            print("Правильно!")

def endGame():
    print("Ти спробував " + str(attempt) + " разів.")


# main program
initGame()
playGame()
endGame()
