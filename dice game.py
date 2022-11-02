
import time
import random

print('Lets play a fun dice game!!!')
var1 = input('Press enter to start...')
print("Numbers should be between 1 and 100")
time.sleep(3)
while True:

    lucky1 = int(input("Player 1's lucky number 1:"))
    if (0 < lucky1 < 100):
        lucky1_2 = int(input("Player 1's lucky number 2:"))
        if (0 < lucky1_2 < 100):
            pen1 = int(input("Player 1's penalty number 1:"))
            if (0 < pen1 < 100):
                pen1_2 = int(input("Player 1's penalty number 2:"))
                if (0 < pen1_2 < 100):
                    lucky2 = int(input("Player 2's lucky number 1:"))
                    if (0 < lucky2 < 100):
                        lucky2_2 = int(input("Player 2's lucky number 2:"))
                        if (0 < lucky2_2 < 100):
                            pen2 = int(input("Player 2's penalty number 1:"))
                            if (0 < pen2 < 100):
                                pen2_2 = int(input("Player 2's penalty number 2:"))
                                if (0 < pen2_2 < 100):
                                    break

player1 = 1
player2 = 1

time.sleep(1)

while player1 <100 and player2 < 100:
    bekleme = input("Player 1's turn (press enter)")
    dice1 = random.randint(1,6)
    time.sleep(1)
    print("Dice rolling...")
    player1 += dice1
    print("Player1 is now:")
    print(player1)
    if player1 == lucky1 or player1 == lucky1_2:
        print("Lucky number!!!")
        player1 += 10
        print("Your number after lucky number is::")
        print(player1)
    elif player1 == pen1 or player1 == pen1_2:
        print("Penalty lovely(!)")
        player1 -= 10
        if player1 < 1:
            player1 = 1 
        print("Your number after penalty number is:")
        print(player1)
    bekleme1 = input("Player 2's turn(press enter)")
    dice2 = random.randint(1,6)
    time.sleep(1)
    print("Dice rolling...")
    player2 += dice2
    print("Player 2:")
    print(player2)
    if player2 == lucky2 or player2 == lucky2_2:
        print("Lucky number!!!")
        player2 += 10
        print("Your number is now:")
        print(player2)
    elif player2 == pen2 or player2 == pen2_2:
        print("Penalty lovely(!)")
        player2 -= 10 
        print("Your number after penalty number is:")
        print(player2)
print("GAME OVER!!!")
time.sleep(1)
if player1 > player2:
    print("Winner is player 1")
elif player2 > player1:
    print("Winner is player 2")