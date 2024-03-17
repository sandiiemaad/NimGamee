#File:CS112_A1_T2_2_20230170.py
#purpose:Each player takes turns picking a number from 1 to 9. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game.
#if all the numbers are used and no player gets exactly 15, the game is a draw.
#Author:Sandy Emad William
#ID:20230170

def number_scrabble():
       # welcome message and display status
       print("welcome to number scrabble")
       numbers = [1,2,3,4,5,6,7,8,9]
       player1_numbers = []
       player2_numbers = []
       sum1 = 0
       sum2 = 0

       while numbers :
             # player1's turn
             print(numbers)
             # show the player the numbers he picked before
             if len(player1_numbers) != 0 :
                 print("player1's numbers", player1_numbers)
             while True :
               player1_num = (input("player1, pick a number"))
               if player1_num.isdigit() and int(player1_num) in numbers :
                     player1_num = int(player1_num)
                     player1_numbers.append(player1_num)
                     numbers.remove(player1_num)
                     break
               else :
                     print("please enter an available valid number")

             #check if player1 wins
             for i in range(len(player1_numbers)):
                for j in range(i + 1, len(player1_numbers)):
                    for k in range(j + 1, len(player1_numbers)):
                        if player1_numbers[i] + player1_numbers[j] + player1_numbers[k] == 15:
                             print("player1 is the winner")
                             sum1 = 15
             if sum1 == 15 :
                 break

             #check if all the numbers are picked
             if len(numbers) == 0:
                   print("the game is draw")
                   break


             # player2's turn
             print(numbers)
             # show the player the numbers he picked before
             if len(player2_numbers) != 0:
                 print("player2 numbers", player2_numbers)
             while True :
                   player2_num = input("player2, pick a number")
                   if player2_num.isdigit() and int(player2_num) in numbers :
                         player2_num = int(player2_num)
                         player2_numbers.append(player2_num)
                         numbers.remove(player2_num)
                         break
                   else :
                         print("please enter an available valid number")

             #check if player2 wins
             for l in range(len(player2_numbers)):
                 for m in range(l + 1, len(player2_numbers)):
                     for n in range(m + 1, len(player2_numbers)):
                         if player2_numbers[l] + player2_numbers[m] + player2_numbers[n] == 15:
                             print("player2 is the winner")
                             sum2 = 15
             if sum2 == 15 :
                 break

             #check if all the numbers are picked
             if len(numbers) == 0 :
                   print("the game is draw")
                   break

def menu():
    print("[A]Start the game\n[B]Exit the game")

while True :
    menu()
    choice = input("Please enter your choice(A/B)").upper()
    while choice != "B":
        if choice == "A":
            number_scrabble()
            break
        else:
            print("Please enter valid choice")
            choice = input("Enter your choice(A/B)").upper()
    if choice == "B" :
        print("End game")
        break



