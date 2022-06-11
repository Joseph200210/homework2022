import hashlib as hl

print('Помогаем найти Санте заветное число... \n')

with open("input.txt", 'r') as INPUT:
    line = INPUT.readline()
    for i in range(10000000):
        byte_line = line + str(i)
        byte_line = byte_line.encode('utf-8')
        hash_object = hl.md5(byte_line)
        hash_MD5 = hash_object.hexdigest()
        if hash_MD5[0:6] == '000000':
            answer = i
            print('Ответ: ', i)
            print('Хэш:', hash_object.hexdigest())
            break
with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(answer))
