import random


def dice_roll(num_of_dices):
    dices = []
    for i in range(num_of_dices):
        dices.append(random.randint(1, 7))
    return dices


def dice_roll(num_of_dices):
    dices = []
    for i in range(num_of_dices):
        dices.append(random.randint(1, 7))
    return dices


def head_or_tail():
    coin_sides = ["head", "tail"]
    return random.choice(coin_sides)


def rock_paper_scissors():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)


choice_of_probability = input("Zar atmak icin 1, yazı-tura icin 2, tas-kagıt-makas icin 3 giriniz:")

if choice_of_probability == "1":
    num_of_dices = input("Kac zar atilsin?")
    print("Atilan", num_of_dices, "zar :", dice_roll(int(num_of_dices)))
elif choice_of_probability == "2":
    print("Yazı-tura sonucu:", head_or_tail())
elif choice_of_probability == "3":
    print("tas-kagıt-makas sonucu:", rock_paper_scissors())
else:
    print("Gecersiz bir ifade girdiniz!")
