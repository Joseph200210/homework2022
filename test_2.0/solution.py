"""Программа для поиска пути от мухи к слону.
Реализует поиск решений для игры "Метаграмма".
По заданному набору слов, начальному и конечному слову,
находит самый короткий способ превратить одно слово в другое.
Например, сделать из мухи слона можно так:
муха -> мура -> тура -> тара -> кара -> каре -> кафе -> кафр ->
каюр -> каюк -> крюк -> урюк -> урок -> срок -> сток -> стон -> слон.
"""

from sys import stdin


def neighbours(a, b):
    """Проверяет являются ли слова a и b соседями.
    На вход ожидаются два слова одинаковой длины.
    :param string a: Одно слово.
    :param string b: Другое слово.
    :return: True если слова являются соседями, иначе False.
    :rtype: bool
    """

    # флаг указывающий на то, встречались ли нам различные буквы
    # на одной и той же позиции в словах a и b
    diff = False

    # перебираем буквы в словах
    for i in range(len(a)):
        # если буквы на позиции i совпадают, переходим к следующей позиции
        if a[i] == b[i]:
            continue

        # если несовпадение уже случалось на одной из предыдущих позиций,
        # значит слова отличаются более чем одной буквой, и мы можем вернуть
        # результат указывающий на то что слова не являются соседями
        if diff:
            return False

        # запоминаем что нам встретилось первое различие в словах
        diff = True

    # мы перебрали все буквы и встретили не более одного различия,
    # возвращаем результат указывающий на то что слова являются соседями
    return True


def metagram(words, start, end):
    """Находит цепочку слов из списка "words", начинающуюся со "start"
    и заканчивающуюся в "end".
    Используем алгоритм поиска в ширину (BFS):
    https://en.wikipedia.org/wiki/Breadth-first_search.
    Вершинами графа будем считать слова из списка, соседние вершины - это
    слова отличающиеся на одну букву.
    :param list[string] words: Набор слов в котором ищем цепочку.
    :param string start: Начальное слово.
    :param string end: Конечное слово.
    :return: Путь от начального слова до конечного слова.
    :rtype: list[string]
    """

    # словарь содержащий посещенные вершины, ключ в этом словаре - это
    # очередная вершина, а значение - предыдущая вершина из которой мы пришли
    visited = {start: None}

    # FIFO (https://ru.wikipedia.org/wiki/FIFO) очередь обнаруженных вершин
    queue = [start]

    # цикл выполняется до тех пор, пока в очереди есть доступные для посещения
    # вершины, то есть до тех пор, пока она не станет пустой
    while queue:
        # достаем очередную вершину из начала очереди
        curr = queue.pop(0)

        # если текущая вершина является конечной, восстанавливаем
        # путь от начальной до конечной вершины и завершаем функцию
        if curr == end:
            path = []
            while curr is not None:
                path.append(curr)
                curr = visited[curr]
            # так как мы строили путь начиная с конца,
            # полученный список нужно развернуть
            path.reverse()
            # возвращаем результат
            return path

        for word in words:
            # проверяем какие из входных слов являются соседями
            # текущего слова и еще не посещались
            if neighbours(curr, word) and word not in visited:
                # запоминаем путь из следующего слова к текущему
                # и помечаем слово как просмотренное
                visited[word] = curr
                # добавляем соседа в очередь обнаруженных вершин
                queue.append(word)

    # мы посетили все вершины, но не добрались до конечного слова
    # так что возвращаем пустой список
    return []


def main():
    # объявляем пустой список в котором будем хранить слова из входного файла
    words = []

    with open('input.txt', 'r') as INPUT:
        # читаем количество строк во входном файле
        word_count = int(INPUT.readline())

        # добавляем слова из входного файла в список
        for _ in range(word_count):
            words.append(INPUT.readline().strip())

    # запускаем алгоритм поиска цепочки слов
    path = metagram(words, words[0], words[1])

    with open('output.txt', 'w') as OUTPUT:
        # печатаем количество слов в полученной цепочке
        OUTPUT.write(str(len(path)) + "\n")

        # печатаем каждое слово в цепочке
        for word in path:
            OUTPUT.write(word + "\n")


# запускаем решение только если скрипт вызван напрямую
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
    main()
