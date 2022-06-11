print('Помогаем Санте найти, сколько строчек хороших, а сколько непослушных...')

vowels = ('a','e','i','o','u')
HMVowels = 0
Score = 0

bad_strings = 0
nice_strings = 0

class SomeError(BaseException):
    None

class FinalRaise(BaseException):
    None

with open('input.txt', 'r') as INPUT:
 
    for line in INPUT:
        Score += 1

with open('input.txt', 'r') as INPUT:    
    while True:
        try:
            for line in INPUT:
                #1
                if 'ab' in line:
                    raise SomeError()
                elif 'cd' in line:
                    raise SomeError()
                elif 'xy' in line:
                    raise SomeError()
                elif 'pq' in line:
                    raise SomeError()
                else:
                    for i in range(len(line)):
                        #2
                        if 2*line[i] in line:
                            #3
                            for j in vowels:
                                HMVowels += line.count(j)     
                                if HMVowels >= 3:
                                    HMVowels = 0
                                    raise FinalRaise()
                                elif j == vowels[-1] and HMVowels < 3:
                                    HMVowels = 0
                                    raise SomeError()
                                    

                        elif i == (len(line) - 1):
                            raise SomeError()
        except SomeError:
            bad_strings += 1
            if  bad_strings + nice_strings == Score:
                break
        except FinalRaise:
            string = line
            nice_strings += 1
            if  bad_strings + nice_strings == Score:
                break
print('Плохих строк:', bad_strings)
print('Хороших строк:', nice_strings)
print('Всего строк:', Score)

with open('output1.txt', 'w') as OUTPUT:
    OUTPUT.write(str(nice_strings))
