print('Помогаем Санте найти, сколько строчек хороших, а сколько непослушных...')

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
                for i in range(len(line)-2):
                    if line[i] == line[i+2]:
                        #2
                        for j in range(len(line)-1):
                            # Если совпадений больше 2, то очевидно,
                            # что даже если есть перекрытие, то
                            # условие выполняется
                            if line.count(line[j]+line[j+1]) > 2:
                                raise FinalRaise()
                            # Но если совпадения всего два, то
                            # нас устроит или 4 элемента подряд,
                            # или несовпадение 1го и 3го элемента
                            # (За IndexError не переживаем, т.к.
                            # будет анализироваться всегда первое
                            # появление повтора)
                            elif line.count(line[j]+line[j+1]) == 2:
                                if 4*line[j] in line:
                                    raise FinalRaise()
                                elif line[j] != line[j+2]:
                                    raise FinalRaise()
                                
                        raise SomeError()
                                        
                            
                raise SomeError()
        except SomeError:
            bad_strings += 1
            if bad_strings + nice_strings == Score:
                break
        except FinalRaise:
            nice_strings += 1
            if bad_strings + nice_strings == Score:
                break
print('Плохих строк:', bad_strings)
print('Хороших строк:', nice_strings)
print('Всего строк:', Score)

with open('output2.txt', 'w') as OUTPUT:
    OUTPUT.write(str(nice_strings))
