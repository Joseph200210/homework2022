####функция####
def smth(line):
    array = []
    array.append([0,0])
    y=0
    x=0
    for i in line:

        if i == '>':
            x += 1
        elif i == '<':
            x += -1
        elif i == '^':
            y += 1
        elif i == 'v':
            y += -1
        else:
            print('Something is wrong.')
            
        array.append([x,y])
    array = sort(array)
    return array
#####################

###Функция_2###
def sort(array):
    print
    array1 = array.copy()
    for j in array1:
        if array.count(j) > 1:
            for k in range(array.count(j) - 1):
                array.remove(j)
    return array
#####################

with open('input.txt', 'r') as INPUT:
    line = INPUT.readlines()
    line_Santa = str(line)[2:-2:2]
    line_RoboSanta = str(line)[3:-2:2]

Homes_Santa = smth(line_Santa)
Homes_RoboSanta = smth(line_RoboSanta)
HMHomes_list = Homes_Santa + Homes_RoboSanta

HMHomes_list = sort(HMHomes_list)

print('Санта и Робо-Санта смогли посетить ' + str(len(HMHomes_list)) + ' дом!')

output = open('output2.txt', 'w')
output.write(str(len(HMHomes_list)))
output.close()
