import itertools as perm

string = 'abcdefghijklmnopqrstuvwxyz0123456789'
array = list(perm.product(string, repeat=2))
for i in range(len(array)):
    array[i] = '\\x' + array[i][0] + array[i][1]

r_string = ''
c_string = ''

print('Помогаем Санте определить количество неучитываемых символов...\n')

with open('input.txt', 'r') as INPUT:
    for line in INPUT:
        line = line.strip()
        r_string += line
        line = line[1:-1]
        if '\\\\' in line:
            line = line.replace('\\\\','*')
        if '\\"' in line:
            line = line.replace('\\"','*')
        for element in array:
            if element in array:
                line = line.replace(element, '*')
        c_string += line
    value = len(r_string) - len(c_string)
    print('У Санты не будет учтено {} символа!'.format(value))

with open('output1.txt','w') as OUTPUT:
    OUTPUT.write(str(value))
