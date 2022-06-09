def func(x):
    global area
    string = x
    size = string.split('x')
    l = int(size[0])
    w = int(size[1])
    h = int(size[2])

    area_list = [l*w, w*h, h*l]
    min_area = min(area_list)

    area += 2*(area_list[0]+area_list[1]+area_list[2]) + min_area
    return area
  
with open('input.txt', 'r') as I:
    area = 0
    for line in I:
        func(line)

output = open('output1.txt', 'w')
output.write(str(area))
output.close()
print('Площадь обёрточной бумаги, которую нужно заказать: '+ str(area) + ' футов^2')
