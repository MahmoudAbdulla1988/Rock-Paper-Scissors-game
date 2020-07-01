import random
file = open('rating.txt', 'r')  #  Reading the file named (rating.txt)
#  for converting the lines in the file to list (the name of the list is "full_list")
list_on_file = file.readlines()
full_list = []
for i in list_on_file:
    i.rstrip()
    a = i.split()
    for x in a:
        full_list.append(x)
name = str(input('Enter your name:'))  #  entering the name of the user.
print('Hello,', name)
#  calculate the rating for users.
if name in full_list:
    rating = int(full_list[full_list.index(name) + 1])
else:
    rating = 0
additional_inputs = input().split(',')  #  this list of the words which allowable for the user to select from.
if len(additional_inputs) == 1 and additional_inputs[0] == '':
    print("Okay, let's start")
    while True:
        allowable_inputs = ['rock', 'scissors', 'paper']  #  The main list of words which allowable for the user to select from.
        user_input = input()  #  entering the user selection.
        computer_input = random.choice(allowable_inputs)  #  computer random selection.

        if user_input in allowable_inputs or user_input == '!exit' or user_input == '!rating':
            if user_input == '!rating':
                print('Your rating:', rating)
                
            if user_input in allowable_inputs or user_input == '!exit':
                game_dict_winning = {'paper': 'rock', 'scissors': 'paper', 'rock': 'scissors'}
                if game_dict_winning[computer_input] == user_input:
                    print("Sorry, but computer chose {0}".format(computer_input))
                elif computer_input == user_input:
                    rating += 50  #  in case of draw the rating of user increase (50)
                    print("There is a draw ({0})".format(user_input))
                elif user_input == '!exit':
                    print('Bye!')
                    break
                else: 
                    rating += 100  #  in case of win the rating of user increase (100)
                    print("Well done. Computer chose {0} and failed".format(computer_input))
        else:
            print('Invalid input')
else:
    print("Okay, let's start")
    while True:
        user_input = input()  #  entering the user selection.
        computer_input = random.choice(additional_inputs)  #  computer random selection.
        if user_input in additional_inputs or user_input == '!exit' or user_input == '!rating':
            if user_input == '!rating':
                print('Your rating:', rating)
            elif user_input in additional_inputs:
                elemnts_after_user_selection = additional_inputs[int(additional_inputs.index(user_input) + 1):int(len(additional_inputs))]
                elemnts_before_user_selection = additional_inputs[0:int(additional_inputs.index(user_input))]
                elemnts_after_user_selection.extend(elemnts_before_user_selection)
                computer_wins_list = elemnts_after_user_selection[0:int(len(elemnts_after_user_selection) / 2)]
                if computer_input in computer_wins_list:
                    print("Sorry, but computer chose {0}".format(computer_input))
                elif computer_input == user_input:
                    rating += 50  #  in case of draw the rating of user increase (50)
                    print("There is a draw ({0})".format(user_input))
                else:
                    rating += 100  #  in case of win the rating of user increase (100)
                    print("Well done. Computer chose {0} and failed".format(computer_input))
            elif user_input == '!exit':
                print('Bye!')
                break
        else:
            print('Invalid input')