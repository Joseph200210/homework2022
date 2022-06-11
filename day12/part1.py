print('Считаем кредиты, дебеты, 1+1, 2+2=5 для Санты!\n')

with open('input.txt','r') as INPUT:
    string = INPUT.readline()

for element in string:
    if element.isdigit() == False and element != '-':
        string = string.replace(element, '.')

array = []
new_array = []
array = string.split('.')
for element in array:
    if element != '':
        new_array.append(int(element))

print('Бухгалтерское универсальное число для Санты:', sum(new_array), sep = ' ')

with open('output1.txt','w') as O:
    O.write(str(sum(new_array)))
