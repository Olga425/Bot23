# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#             return False
#     middle = (right + left) // 2
#     if element == array[middle]:
#         if array[middle - 1] < element and element <= array[middle]:  # если элемент в середине,
#             return middle
#         elif element < array[middle]:  # если элемент меньше элемента в середине
#             # рекурсивно ищем в левой половине
#             return binary_search(array, element, left, middle - 1)
#     elif element == array[middle - 1]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#             return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#             return binary_search(array, element, middle + 1, right)
# array = list(map(int, input("Введите целые числа в любом порядке, через пробел: ").split()))
# element = int(input("Введите любое положительное целое число из полученного списка: "))
# array = sorted(array)
# print(array)
# left = int(array[0])
# right = int(array[-1])
# if element < left or element > right:
#     print('Числа нет в диапазоне')
# else:
#     print(binary_search(array, element, 0, len(array) - 1))
#

# def is_empty(): # очередь пуста?
# #     # да, если указатели совпадают и в них содержится ноль
# #     return head == tail and queue[head] == 0


# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head

# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max

# def show(): # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))

# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель

# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#         D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
#     U[min_k] = True # просмотренную вершину помечаем

Сейчас мы попробуем создать класс LinkedList, реализующий список.
Элементы списка будут представлять собой экземпляры класса Node.
#
#
# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
# #
# #         pointer = self.first  # берем первый указатель
# #         while pointer is not None:  # пока указатель не станет None
# #             R += str(pointer.value)  # добавляем значение в строку
# #             pointer = pointer.next  # идем дальше по указателю
# #             if pointer is not None:  # если он существует добавляем пробел
# #                 R += ' '
# #         return R
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)


# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 98))