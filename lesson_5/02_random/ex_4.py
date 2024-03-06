import random

d = {
    1: 'Орел',
    2: 'Решка',
}

count_O = 0
count_P = 0
sequence = []

while count_O < 3 and count_P < 3:
    trial = random.randint(1, 2)
    if trial == 1:
        count_O += 1
        count_P = 0
    else:
        count_O = 0
        count_P += 1
    sequence.append(d[trial])

print(f'Послідовність: {sequence}')
if count_O == 3:
    print('Випало 3 орли поспіль')
else:
    print('Випало 3 решки поспіль')
print(f'К-сть спроб: {len(sequence)}')