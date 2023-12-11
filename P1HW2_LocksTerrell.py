# P1HW2 - Calculating travel expenses
# October 3, 2023
# CTI-110 P1HW2 - Travel Expense
# Terrell Locks
#

#user inputs their destination, and numbers for budget, destination, gas, accommodation, and food

print('This program calculates and displays travel expenses: ')

user_budg = int(input('\nEnter budget: '))

user_dest = (input('\nEnter your travel destination: '))

user_gas = int(input('\nHow much do you think you will spend on gas? '))

user_accm = int(input('\nApproximately, how much will you need for accommodation/hotel? '))

user_food = int(input('\nLast, how much do you need for food? '))

#expenses are calculated

print('------------Travel Expenses------------')
print('Location: ', user_dest)
print('Initial budget: ', user_budg)
print('\nFuel: ', user_gas)
print('Accomodation: ', user_accm)
print('Food: ', user_food)
print('\nRemaining Balance: ', user_budg - user_gas - user_accm - user_food)

#Remaining balance: 1200 - 250 - 600 - 300 = 50
