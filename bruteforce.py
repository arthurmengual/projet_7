import matplotlib.pyplot as plt
import time
import itertools
import numpy as np

actions = {'action1': {'cout': 20, 'profit': 5}, 'action2': {'cout': 30, 'profit': 10}, 'action3': {'cout': 50, 'profit': 15}, 'action4': {'cout': 70, 'profit': 20},
           'action5': {'cout': 60, 'profit': 17}, 'action6': {'cout': 80, 'profit': 25}, 'action7': {'cout': 22, 'profit': 7}, 'action8': {'cout': 26, 'profit': 11},
           'action9': {'cout': 48, 'profit': 13}, 'action10': {'cout': 34, 'profit': 27}, 'action11': {'cout': 42, 'profit': 17}, 'action12': {'cout': 110, 'profit': 9},
           'action13': {'cout': 38, 'profit': 23}, 'action14': {'cout': 14, 'profit': 1}, 'action15': {'cout': 18, 'profit': 3}, 'action16': {'cout': 8, 'profit': 8},
           'action17': {'cout': 4, 'profit': 12}, 'action18': {'cout': 10, 'profit': 14}, 'action19': {'cout': 24, 'profit': 21}, 'action20': {'cout': 114, 'profit': 18}
           }


####This function takes in parameter a list of actions and the budget of the client.###
### It analyses all possible combinations and return the one with the higher profit,###
### within the client's budget###


def bruteforce(liste, budget):
    binaries = [format(i, '020b') for i in range(2**len(liste))]
    combos = {}
    # iterate through every combination
    k = 1
    for binary in binaries:
        combo = {'actions': '', 'cout': 0, 'profit': 0}
        # iterate through each cell and if equals to one, take in account the corresponding action
        for index, cell in enumerate(binary):
            if cell == '1':
                action = f'action{index+1}'
                cout = actions[f'action{index+1}']['cout']
                profit = float(actions[f'action{index+1}']['cout'] *
                               actions[f'action{index+1}']['profit'] / 100)
                # increment combo
                combo['actions'] += f'{action} '
                combo['cout'] += cout
                combo['profit'] += profit
        # append the combo to the list of combos
        if combo:
            combos[f'combo{k}'] = combo
            k += 1

    # sorting of combos and keep the one with the maximum profit
    i = 0
    result = ''
    for key, value in combos.items():
        if value['cout'] < budget:
            if i < int(value['profit']):
                result = key, value
                i = value['profit']

    return result


#print(bruteforce(actions, 500))

##ANALYSING BRUTEFORCE ALGORITHM COMPLEXITY##


points = []
for i in range(len(actions)):
    time1 = time.time()
    bruteforce(dict(itertools.islice(actions.items(), i)), 500)
    time2 = time.time()
    delay = time2 - time1
    points.append(delay)


###graph###
abscisse = [x for x in range(len(actions))]
ordonnées = points

plt.figure(figsize=(12, 8))
plt.title('Optimized \n Complexité: x')
plt.xlabel('nb of actions')
plt.ylabel('time of execution')
plt.scatter(abscisse, ordonnées)

z = np.polyfit(abscisse, ordonnées, 1)
p = np.poly1d(z)
plt.plot(abscisse, p(abscisse), "r--")

plt.legend()
plt.show()
# plt.savefig('bruteforce_graphe.png')


# cours sur la complexité
# noter à côté des courbes la complexité pour chaque alog (expo, loga, ...)
# diapositive
# rapport dexploration de compa résultats siena et les notres
# comparer result avec les diffts algo
###
