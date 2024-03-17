import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

element = [rock, paper, scissors]
user_choice =int (input("enter your choice \n 0 fore rock ,  1 for paper , 2 for scissors \n") ) 
print (element[user_choice])

computer_choice =random.randint(0,2)
print (f"computer chose {element[computer_choice]}")

if user_choice == 0 and computer_choice == 2 :
    print ("you win!")
elif computer_choice == 0 and user_choice == 2 :
    print ("you lose")
elif computer_choice > user_choice :
    print ("you lose")
elif user_choice > computer_choice :
    print ("you win!")
elif computer_choice == user_choice :
    print ("it's a draw")
else :
    print ("you typed an invalid number, you lose!")