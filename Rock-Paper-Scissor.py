import random

list=('rock', 'paper', 'scissor')

print(list)

print("\n\nScore 5 to win.\n\n")

print("Enter between 1-3 to choose rock, paper, scissor respectively.\n")

i=0 #me

j=0 #cp

while True:

  try:

    

    

    while True:

     me=list[int(input('Enter your choice: '))-1]

     cp=random.choice(list)

     print("You choosed" ,me)

     print("Computer choosed", cp, '\n')

   

     if me==cp:

       print("It's a draw.")

       i=i

       j=j

       print(f"Your total point is {i} \nComputer's total point is {j}.\n")

    

     if me=='rock' and cp=='paper':

       print('Computer scored.')

       j=j+1

       print(f"Your total point is {i}\nComputer's total point is {j}.\n")

    

     if me=='rock' and cp=='scissor':

       print('You scored.')

       i+=1

       print(f"Your total point is {i} \nComputer's total point is {j}.\n")

    

     if me=='paper' and cp=='scissor':

       print('Computer scored.')

       j=j+1

       print(f"Your total point is {i} \nComputer's total point is {j}.\n")

    

     if me=='paper' and cp=='rock':

       print('You scored.')

       i=i+1

       print(f"Your total point is {i} \nComputer's total point is {j}.\n")

     if me=='scissor' and cp=='rock':

       print('Computer scored.')

       j=j+1

       print(f"Your total point is {i} \nComputer's total point is {j}.\n")

  

     if me=='scissor' and cp=='paper':

       print('You scored.')

       i=i+1

       print(f"Your total point is {i} \nComputer's total point is {j}.\n")

     if j==5:

       print("******You loss the game******")

       break

     if i==5:

       print("*****Congratulations! You win the game.*****")

       break

        

      

  except Exception as e:

    print("Run the code again and enter between 1 to 3.")

    print(e)

    print('\n')

  if i==5 or j==5:

   break