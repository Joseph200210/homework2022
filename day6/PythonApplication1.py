print('Санта прекрасно осветил улицу, но стоит высчитать, сколько всего фонарей горит...')

array = []
for y in range(1000):
    for x in range(1000):
        array.append([x,y,0])

with open('input.txt','r') as INPUT:
    for line in INPUT:

        text = line
        if '\n' in text:
            text = text[0:-1]
        text = text.split(' ')
        
        if text[0] == 'turn':
            if text[1] == 'on':
                start_coord = str(text[2]).split(',')
                end_coord = str(text[4]).split(',')
                for y in range(int(start_coord[1]), int(end_coord[1])+1):
                    for x in range(int(start_coord[0]), int(end_coord[0])+1):
                        array[1000*y+x][2] = 1
            elif text[1] == 'off':
                start_coord = str(text[2]).split(',')
                end_coord = str(text[4]).split(',')
                for y in range(int(start_coord[1]), int(end_coord[1])+1):
                    for x in range(int(start_coord[0]), int(end_coord[0])+1):
                        array[1000*y+x][2] = 0

            else:
                print('smth is wrong! (on/off)')

        elif text[0] == 'toggle':
            start_coord = str(text[1]).split(',')
            end_coord = str(text[3]).split(',')
            for y in range(int(start_coord[1]), int(end_coord[1])+1):
                for x in range(int(start_coord[0]), int(end_coord[0])+1):
                    if array[1000*y+x][2] == 1:
                        array[1000*y+x][2] = 0
                    elif array[1000*y+x][2] == 0:
                        array[1000*y+x][2] = 1
                    else:
                        print('smth is wrong! (toggle 1/0)')
        else:
            print('smth is wrong! (turn/toogle)')
HMLights = 0
for element in array:
    if element[2] == 1:
        HMLights += 1

row = []

with open('output1.txt','w') as OUTPUT:
    OUTPUT.write(str(HMLights))
with open('map_of_lights.txt', 'w') as map:
    for y in range(1000):
        map.write('\n' + ''.join(row))
        row = []
        for x in range(1000):
            row.append(str(array[1000*y+x][2]))
            
print('Санта зажёг {} фонарей!'.format(HMLights))
