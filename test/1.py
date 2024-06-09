import random
import time
print("Давай кинемо кубики!")
your_number = 0
my_number = 0

# Гральні кубики
for n in range(100):
    print(str(n + 1) + ". Раунд")
    print("Твій кидок: ", end="")
    shoot1 = random.randint(1, 6)
    time.sleep(0.5)
    print(shoot1)
    print("Мій кидок: ", end="")
    shoot2 = random.randint(1, 6)
    time.sleep(0.5)
    print(shoot2)
    if shoot1 > shoot2:
        your_number += 1
    if shoot1 < shoot2:
        my_number += 1
    print(str(your_number) + " і " + str(my_number))
    time.sleep(1)
    print()

if your_number > my_number:
    print("Ти виграв")
elif your_number < my_number:
    print("Я виграв")
else:
    print("Нічия")
