# Time : 11/14/22 07:35
# Author : Benjamin Hensley Jr.
# File : pinCracker.py

import time
x = True

while x:
    password = input(f"What is your 4 digit pin?: ")
    if len(password) != 6:
        print(f"That is not a valid 4 digit pin. Please try again: ")
    else:
        try:
            password = int(password)
            x = False
        except ValueError:
            print(f"That is not a valid pin. Please try again")

while True:
    startTime = time.time()
    for a in range(1, 1000000):
        a = str(a)
        if len(a) == 1:
            a = f'00000{a}'
        elif len(a) == 2:
            a = f'0000{a}'
        elif len(a) == 3:
            a = f'000{a}'
        elif len(a) == 4:
            a = f'00{a}'
        elif len(a) == 5:
            a = f'0{a}'
        print(a)
        if str(password) == a:
            print('Passphrase Cracked')
            print(f'{a}:{password}')
            print(f"It took {time.time() - startTime} seconds to crack this password")
            quit()