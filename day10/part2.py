with open('input.txt','r') as INPUT:
    line = INPUT.readline()

print('Труд - это хорошо, но и об отдыхе не нужно забывать!' +
      '\n Эльфы решили сыграть в игру, но ВЫ решили их впечатлить.' +
      '\n Давайте удивим их, как быстро мы можем находить решение' +
      '\n на несколько шагов вперёд.')

#HMSteps = int(input('Количество шагов вычислений: '))
#for counter in range(HMSteps):
for counter in range(50):
    array = [element for element in line]
    HMNumb = 1
    new_array = []
    try:
            for i in range(len(array)):
                if array[i] == array[i+1]:
                    HMNumb += 1
                else:
                    new_array.append(str(HMNumb))
                    new_array.append(array[i])
                    HMNumb = 1
    except IndexError:
            None
            if array[-1] == array[-2]:
                new_array[-1][0] += 1
                line = ''.join(new_array)
            else:
                new_array.append(str(1))
                new_array.append(array[-1])
                line = ''.join(new_array)

print('Ого, неплохо так насчитало...')
print('...')
print('{} цифр получилось!!!'.format(str(len(line))))

OUTPUT = open('output2.txt', 'w')
OUTPUT.write(str(len(line)))
OUTPUT.close()
            
input()
