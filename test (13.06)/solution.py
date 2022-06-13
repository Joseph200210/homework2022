with open('input.txt') as inp:               #Чтение данных
    N = int(inp.readline())                       #Читаем количество городов
    array = []                                      
    for i in range(N*(N+1)//2):                     #Цикл дял создания массива из чисел
        array.append(int(inp.readline().strip())) 
    m = len(array.copy())                           #Количество строк              
                                                    
n = 2                                               #Преобразование массива
smth_array = []                                  
while n <= N+1:                                     #Цикл с предусловием 
    new_array = []                                  
    for i in range(1,n):                            #Цикл для уменьшения длины массива
        new_array.append(array[-1])                 
        array.pop(-1)                               #Удаление элемента старого массива
    new_array.reverse()                             #Разворот подмассива
    smth_array.append(new_array)                    #Добавляем подмассив в полный НОВЫЙ массив
    n += 1                                          #Инкремент
smth_array.reverse()                                #Разворот нового массива
array = smth_array                               
                                                    
def minCost(array, x):                              #Рекурсивная функция   
    if x[1] > len(array):                           
        print(x[1], len(array))                     #Checker
        print('WRONG!')                     
    elif x[1] == len(array):                        #Условие выхода из рекурсии
        return x[0]                                 
    else:                                           
        List = []                                   
        for i in range(len(array[x[1]])):           #Перебор элементов возможных путей
            List.append(x[0] + minCost(array, [array[x[1]][i],x[1]+1+i]))
        return min(List)                            #Поиск наименьшей стоимости поездки для переданного старт


counter = 0                         
List = []                                           
for element in array[0]:                            #Перебор точек старта
    counter += 1                                    #Счётчик переходов
    a = minCost(array, [element, counter])          #Рекурсивная функция
    List.append(a)                                  #Добавление в список коротких путей
minCost = min(List)                                 #Стоимость самого дешёвого пути
print('Наименьшая стоимость пути:', minCost)


                                                    
with open('output.txt', 'w') as out:             #Запись данных в файл
    out.write(str(minCost))                      


