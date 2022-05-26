with open('input.txt', 'r') as INPUT:
    text = INPUT.readline()

counter = 0

for symb in text:

    if symb == '(':
        counter += 1

    elif symb == ")":
        counter -= 1

    else:
        print(symb)
        print('error')

print('Floor: ', counter)

with open('output1.txt', 'w') as OUTPUT:
    OUTPUT.write(str(counter))
