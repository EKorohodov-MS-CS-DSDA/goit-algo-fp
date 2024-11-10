import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        buffer = []
        current = self.head
        while current:
            buffer.append(current.data)
            current = current.next
        print(buffer)


    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def sort(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            if min_node != current:
                current.data, min_node.data = min_node.data, current.data
            current = current.next


    def merge(self, other_list):
        if self.head is None:
            self.head = other_list.head

        if self.head is None:
            return

        current1 = self.head
        current2 = other_list.head
        prev = None
        while current1 and current2:
            if current1.data <= current2.data:
                prev = current1
                current1 = current1.next
            else:
                if prev:
                    prev.next = current2
                else:
                    self.head = current2
                prev = current2
                current2 = current2.next
                prev.next = current1
        if current2:
            prev.next = current2
        else:
            prev.next = current1


def main():
    # TODO: create 2 LinkedLists of random numbers, sort them, then merge them
    list1 = LinkedList()
    list2 = LinkedList()
    for _ in range(5):
        list1.insert_at_end(random.randint(1, 100))
    for _ in range(7):
        list2.insert_at_end(random.randint(1, 100))

    print("List1:")
    list1.print_list()
    print("List2:")
    list2.print_list()

    print("Sorted List1:")
    list1.sort()
    list1.print_list()
    print("Sorted List2:")
    list2.sort()
    list2.print_list()

    print("Merged List:")
    list1.merge(list2)
    list1.print_list()


if __name__ == "__main__":
    main()
