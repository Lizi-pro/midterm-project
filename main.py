# თამაში - გამოიცანი რიცხვი

# import random
# number = random.randint(1, 100)
# print('გამარჯობა, ეს არის თამაში გამოიცანი რიცხვი,''\n'
#       'უნდა გამოიცნოთ რიცხვი 1-იდან 100-ის ჩათვლით,''\n'
#       'რიცხვის გამოსაცნობად გაქვთ 6 ცდა')
# number_of_attempts = 1
# while number_of_attempts <= 6:
#     user_number = int(input(f'ცდა {number_of_attempts}, შეიყვანეთ რიცხვი: '))
#     if number > user_number:
#         print('თქვენი შეყვანილი რიცხვი ნაკლებია გამოსაცნობ რიცხვზე')
#         number_of_attempts += 1
#     elif number < user_number:
#         print('თქვენი შეყვანილი რიცხვი მეტია გამოსაცნობ რიცხვზე')
#         number_of_attempts += 1
#     else:
#         break

# if number == user_number and number_of_attempts <= 6:
#     print(f'გილოცავთ, თქვენ გამოიცანით რიცხვი {number}, თქვენ დაგჭირდათ {number_of_attempts} მცდელობა')
# else:
#     print('სამწუხაროდ თქვენ ამოგეწურად მცდელობების რაოდენობა და ვერ გამოიცანით რიცხვი')