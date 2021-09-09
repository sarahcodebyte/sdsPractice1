import random
random_number = random.randint(10, 99)
user_input = int(input('Enter a two-digit number: '))
random_numberdigit1 = random_number//10
random_numberdigit2 = random_number%10
user_inputdigit1 = user_input//10
user_inputdigit2 = user_input%10
if random_number == user_input:
    print('You have won $10,000')
elif random_numberdigit1 == user_inputdigit2 and random_numberdigit2 == user_inputdigit1:
    print('You have won $3000')
elif random_numberdigit1 == user_inputdigit1 or random_numberdigit2 == user_inputdigit2 or random_numberdigit1 == user_inputdigit2 or random_numberdigit2 == user_inputdigit1:
    print('You have won $1000')
else: print('Bad luck') 
       
        