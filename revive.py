import assassins as asns
from random import shuffle
from random import randint
import time

assassins = asns.assassin_list()

print()

dead_assassins = []

for assassin in assassins:
    if assassin[3] == 0:
        dead_assassins.append((assassin, asns.revival_chance(assassin)))

weighted_random_list = []
total_entries = 0;

for assassin in dead_assassins:
    total_entries += assassin[1]

dead_assassins.sort(key=asns.takeSecond, reverse=True)

for assassin in dead_assassins:
    for i in range(assassin[1]):
        weighted_random_list.append(assassin[0][0])
    print(assassin[0][0] + ' has been added ' + str(assassin[1]) + ' times (' + str(round((100*assassin[1]/total_entries), 2)) + '% revival chance)')

print('\nThere are ' + str(total_entries) + ' total entries')
time.sleep(2)

print('\nDRUMROLL PLEASE...')
time.sleep(1)

for i in range(3):
    print('.')
    time.sleep(1)


for i in range(randint(1, 10)):
    shuffle(weighted_random_list)

print(weighted_random_list.pop() + ' has been given another chance!')
