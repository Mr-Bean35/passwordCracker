# Programmer: Benjamin Hensley Jr.
# Program Name: Passwords.py
# Date: 9/26/22

import time
passphrase = input(f"Please input your password: ")
add = 0
t = 0
test1 = 0
count = 1
startTime = time.time()
for i in range(32, 127):
    print(chr(i))
    if chr(i) == passphrase:
        print('Passphrase Cracked')
        print(f'{chr(i)}:{passphrase}')
        print(f"It took {time.time() - startTime} seconds to crack this password")
        quit()
used = [32]
index = 0
while True:
    if t == 1:
        used[1] = 32
    t = 0
    count = 0
    add = 0
    ind = True
    sub = 0
    repeat = 0
    base = ''
    for a in used:
        if repeat == 0:
            a = chr(a)
            base = f'{a}'
        else:
            base = f'{base}{chr(a)}'
        repeat = 1
    for i in range(32, 127):
        check = f'{base}{chr(i)}'
        print(check)
        if check == passphrase:
            print('Passphrase Cracked')
            print(f'{check}:{passphrase}')
            print(f"It took {time.time() - startTime} seconds to crack this password")
            quit()
        if i >= 126:
            if used[index] >= 126:
                if len(used) == 1:
                    used[index] = 32
                    used.append(32)
                    add += 1
                    index += 1
                else:
                    while ind:
                        if used[index - sub] >= 126:
                            if (index - sub) == 0:
                                used[index - sub] = 32 + count
                                used.append(32)
                                add += 1
                                index += 1
                                while index != count:
                                    used[count] = 32
                                    count += 1
                                    t = 1
                            else:
                                used[index - sub] = 32
                                sub += 1
                                add += 1
                        else:
                            used[index - sub] += 1
                            ind = False
            else:
                used[index] += 1