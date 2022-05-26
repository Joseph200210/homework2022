from math import floor


with open('input.txt', 'r') as INPUT:
    text = INPUT.readline()

floor = 0
steps = 0

for symb in text:
    if symb == '(':
        floor += 1

    elif symb == ")":
        floor -= 1

    else:
        print('error')
    
    steps += 1
    if floor == -1:
        break
   


print('Step: ', steps)

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(steps))
