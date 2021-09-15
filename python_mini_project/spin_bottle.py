import time

import random
import secrets


print('#### WELCOME TO SPIN THE BOTTLE GAME ####')
time.sleep(3)
for i in range(1, 5):
    print('\n')
d = int(input('         enter number of player   '))
player = []
for i in range(1, d+1):
    print('enter player number', i)
    p = input()
    print('\n')
    player.append(p)
print('players are', player)
print('### BOTTLE IS SPINNING ###\n')

time.sleep(3)
heads = secrets.choice(player)

tails = secrets.choice(player)
print('#### BOTTLES HEADS TOWARD  ###\n', heads)
if heads != tails:
    print('### BOTTLES TAILS TOWARDS  ###\n', tails)
else:
    print('###BOTTLES TAILS TOWARDS ###', tails)
