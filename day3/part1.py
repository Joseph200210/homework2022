array = []
with open('input.txt', 'r') as INPUT:
    line = INPUT.readlines()
    line = str(line)[2:-2]
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
array1 = array.copy()
for j in array1:
    if array.count(j) > 1:
        for k in range(array.count(j) - 1):
            array.remove(j)
print('Санта посетил ' + str(len(array)) + ' дома за ночь!')

with open('output1.txt','w') as output:
    output.write(str(len(array)))
