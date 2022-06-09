def func(x):
    string = x
    size = string.split('x')

    l = int(size[0])
    w = int(size[1])
    h = int(size[2])

    sizes = sorted([l,w,h])

    length = l*w*h + 2*(sizes[0]+sizes[1])
    return length
  
with open('input.txt', 'r') as I:
    length = 0
    for line in I:
        length += func(line)

output = open('output2.txt', 'w')
output.write(str(length))
output.close()
print('Длина ленты, которую нужно заказать: '+ str(length) + ' футов^2')
