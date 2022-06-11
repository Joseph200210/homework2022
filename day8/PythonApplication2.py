import itertools as perm

string = 'abcdefghijklmnopqrstuvwxyz0123456789'
array = list(perm.product(string, repeat=2))
for i in range(len(array)):
    array[i] = '\\x' + array[i][0] + array[i][1]

old_str = ''
new_str = ''

print('Помогаем Санте определить количество неучитываемых символов...\n')

with open('input.txt', 'r') as INPUT:
    for line in INPUT:
        line = line.strip()
        old_str += line
        if '\"' in line:
            line = line.replace('\"', '**')
        if '\\' in line:
            line = line.replace('\\', '**')
        line = '\"' + line + '\"'
        new_str += line
    value = len(new_str) - len(old_str)
    print('Разница между новой и старой строкой будет {} символов!'.format(value))

with open('output2.txt','w') as OUTPUT:
    OUTPUT.write(str(value))
