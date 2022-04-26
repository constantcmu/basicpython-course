import random


while True:
    choice = ['rock','paper','scissors']
    n = random.randint(0,2)
    robot = choice[n]
    print("------------rock paper sissors-------------")
    print("chose: rock , paper , scissors ")
    player = input("You : ")
    print("Robot :  ",robot)


    if player == "rock":
        if robot == "rock":
            print(">>draw")
        elif robot == "paper":
            print(">>Robot win ")
        else:
            print(">>You win")
            break
    elif player == "paper":
        if robot == "rock":
            print(">>You win")
            break
        elif robot == "paper":
            print(">>draw")
        else:
            print(">>Robot win ")
    elif player == "scissors":
        if robot == "rock":
            print(">>Robot win ")
        elif robot == "paper":
            print(">>You win")
            break
        else:
            print(">>draw ")

