import assassins as asns
from random import shuffle
from random import randint

live_assassins = asns.live_assassin_list()
targets = []

print()

shuffle(live_assassins)
live_assassins.sort(key=asns.takeThird, reverse=True)

tier1 = live_assassins[:len(live_assassins)//2 + 1]
tier2 = live_assassins[len(live_assassins)//2 + 1:]

for i in range(0, randint(1, 100)):
    shuffle(tier1)

for i in range(0, randint(1, 100)):
    shuffle(tier2)

shuffle_list = []

count = live_assassins.copy()

while tier1:
    shuffle_list.append(tier1.pop())
    if tier2:
        shuffle_list.append(tier2.pop())

while shuffle_list:
    curr_assassin = shuffle_list.pop(0)
    curr_target = [curr_assassin[0], '']
    if targets:
        targets[-1][1] = curr_target[0]
    targets.append(curr_target)

targets[-1][1] = targets[0][0]

for pair in targets:
    print(pair[0] + ' has ' + pair[1])
print()
