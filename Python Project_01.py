# '''
# My first Snake, Water, Gun game Project.

# snake = 1
# water = -1
# gun = 0

# '''

# import random

# computer = random.choice([-1, 0, 1])

# yourstr = input("Enter you choice :")
# yourdict = {"s": 1, "w": -1, "g": 0}

# reversedict = {1 : "snake", -1 :"water", 0 : "gun"}
# you = yourdict[yourstr]

# print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

# if(computer == you):
#     print("The Match is draw, 'Play Again'")

# else:
#     if (computer == -1 and you == 1):
#         print("Congratulation, you win!")
        
#     elif(computer == -1 and you == 0):
#         print("Oops, you loose")
        
#     elif(computer == 1 and you == -1):
#         print("Oops, you loose")
        
#     elif(computer == 1 and you == 0):
#         print("Congratulation, you win!")

#     elif(computer == 0 and you == -1):
#         print("Congratulation, you win!")

#     elif(computer == 0 and you == 1):
#         print("Oops, you loose")

#     else:
#         print("Some went wrong,\n'Play Again'")