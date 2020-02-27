import assassins as asns

live_assassins = asns.live_assassin_list()
assassins = asns.assassin_list()

count = live_assassins.copy()

print('\nFull Leaderboard:')

dead_or_alive = ''

assassins.sort(key=asns.takeThird)

i = 1
while assassins:
    assassin = assassins.pop()
    if assassin[3] == 0:
        dead_or_alive = ' (immunities unused: ' + str(assassin[1]) + ') **DEAD**'
    else:
        dead_or_alive = ' (immunities remaining: ' + str(assassin[1]) + ')'
    print (str(i) + '. ' + assassin[0] + ' with ' + str(assassin[2]) + ' kills' + dead_or_alive)
    i += 1

#for i in range(0,49):
#    if assassins[i][3] == 0:
#        dead_or_alive = ' **DEAD** (immunities wasted: ' + str(asssassins[i][1]) + ')'
#    else:
#        dead_or_alive = ' (immunities remaining: ' + str(assassins[i][1]) + ')'
    #if assassins[i][2] == 0:
        #break
#    print (str(i+1) + '. ' + assassins[i][0] + ' with ' + str(assassins[i][2]) + ' kills' + dead_or_alive)

print('\nNumber Alive: ' + str(len(count)))
