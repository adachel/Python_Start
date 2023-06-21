# Однонаправленный список
class LinkedList:
    head = None # голова списка или первый элемент
    class Node: # класс узел
        element = None
        next_node = None
        def __init__(self, element, next_node = None):
            self.element = element # значение
            self.next_node = next_node

    def append(self, element): # функция добавление элемента в конец
        if not self.head:   # если 'head' в другом классе, то добираемся до него через 'self'
            self.head = self.Node(element) # если 'head' пустой, то присваеваем ему 'Node'
            return element
        node = self.head    # если 'head' есть, то начинаем раскручивать список
        while node.next_node:   # пока есть следующий узел
            node = node.next_node   # будем 'node' присваивать следующему узлу
        node.next_node = self.Node(element) # как только дошли до конца, то в конец вставляем новый узел

    def out(self): # функция вывода
        node = self.head
        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

Linked_List = LinkedList()
Linked_List.append(1)
Linked_List.append(2)
Linked_List.append(3)
Linked_List.append(4)
Linked_List.append(5)
Linked_List.append(6)

Linked_List.out()