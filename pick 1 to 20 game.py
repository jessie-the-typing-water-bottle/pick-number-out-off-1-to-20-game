#exoprogamer
#pick number from 1 to 20 game

import random
from colorama import Fore

print('Welcome to my game')
print('')


num = random.randint(1, 20)
userinput = None
num2 = random.randint(1, 20)

for i in range(21):
    print(i, end=" ")
print()

while userinput != num:
    userinput=input(Fore.WHITE + 'pick a number: ')
    userinput=int(userinput)

    if userinput != num2:
        userinput=int(userinput)
    elif userinput == num2:
        print(Fore.GREEN + 'YOU PICKED THE SECOND NUMBER YOU WIN!!!!')
        break
    else:
        print(Fore.RED + '*wrong number*')
        
    if userinput == num:
        print(Fore.GREEN + 'YOU WON!!!')
        break
    else:
        print(Fore.RED + '***wrong number***')
