import assassins as asns

assassins = asns.live_assassin_list()
print()
print('immunities left:')

for assassin in assassins:
    print(assassin[0] + ': ' + str(assassin[1]))
print()
