# continue and break
list_1 = [1, 2, 3]
list_2 = [10, 20, 30]
for i in list_1:
    print('START outer')
    for j in list_2:
        print('-> ', i, j)
        if i == 2 and j == 20:
            print('break inner for')
            break
    else:
        print('Finish inner for')
        continue
    print('break outer for')
    break
