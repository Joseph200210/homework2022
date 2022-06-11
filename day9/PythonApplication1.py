from itertools import permutations

print('В этом году мы должны справиться с доставкой подарков как можно быстрее!\n' +
      'Давайте узнаем, как наиболее быстро нам пролететь все пункты.\n')

with open('input.txt', 'r') as INPUT:
    lines = INPUT.readlines()

#Инициализация списка мест
array = []
for line in lines:
    line = line.replace(' to ', ',')
    line = line.replace(' = ', ',')
    line = line.strip()
    array.append(line.split(','))

#Определяем,сколько городо всего
array_city = []
for i in range(len(array)):
    if array[i][0] not in array_city:
        array_city.append(array[i][0])
    if array[i][1] not in array_city:
        array_city.append(array[i][1])

#Создаём все возможные пути (можно оптимизировать, уверен)
perm = list(permutations(array_city))
dist_array = []
for element in perm:
    dist = 0

    for i in range(len(array_city)-1):
        for j in range(len(array)):
            if (element[i] == array[j][0] or element[i] == array[j][1]) and (element[i+1] == array[j][0] or element[i+1] == array[j][1]):
                dist += int(array[j][2])
    dist_array.append(dist)

#Самый короткий путь (из-за него немного дольше ищет)
    if dist <= min(dist_array):
        min_way = element
    

with open('output1.txt', 'w') as OUTPUT:
    OUTPUT.write(str(min(dist_array)))

string = ' <-> '.join(min_way)
print('Отлично, нам нужно преодолеть %s миль. В дорогу!\n' % (str(min(dist_array))))
print('Самый короткий путь:')
print(string)
