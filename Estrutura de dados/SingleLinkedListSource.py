# Singly LinkedList
"""
      head            second              third
         |                 |                  |
         |                 |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |   -------->| 2  |   -------->|  3 | null |
    +----+------+     +----+------+     +----+------+
"""


# Node class of a linked list
class SingleNode:

    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class SingleLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        if index < 0 or index >= self.length():
            print("Error: Index out of range")
            return None

        current_node = self.head
        for _ in range(1, index):
            current_node = current_node.next

        return current_node.data

    def append(self, data):

        new_node = SingleNode(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        return

    def length(self):
        if self.head is None:
            return 0
        current_node = self.head
        total = 0

        while current_node:
            total += 1
            current_node = current_node.next

        return total

    def display(self):
        contents = self.head
        print('')
        if contents is None:
            print("List has no element")

        display_str = 10 * "_"
        while contents:
            display_str += "\n|" + f"{contents.data}".center(8, "_") + "|"
            contents = contents.next

        print(display_str + '\n')

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next

        return node_data

    def reverse_linkedlist(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
        return

    def search_item(self, item):

        index = 0
        current_node = self.head

        print(f'Searching for item: {item}')

        while current_node:
            if current_node.data == item:
                print(f"Item found at index {index}")
            index += 1
            current_node = current_node.next
        else:
            print("Item not found")

    def remove_at_start(self):
        if self.head is None:
            print("Error: Empty list")
            return

        self.head = self.head.next

    def remove_at_end(self):
        current_node = self.head

        if self.head is None:
            print(f'Error: Empty list')
            return
        elif self.head.next is None:
            self.head.data = None
            return

        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None


    def insert_at_start(self, data):
        new_node = SingleNode(data)
        new_node.next = self.head
        self.head = new_node


    def remove_element_by_value(self, data):
        current_node = self.head

        if current_node.data == data:
            self.head = current_node.next
            print(f'The item {data} is excluded from the list')
            return

        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                print(f'The item {data} is excluded from the list')
                return

            current_node = current_node.next

        print(f'{data} was not found')
        return


    def insert_at_index(self, index, data):
        new_node = SingleNode(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        elif index < 0:
            print('Error: Index out of range!')
            return

        current_node = self.head
        for _ in range(index-1):
            if current_node.next is None:
                print('Error: Index out of range!')
                return

            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
        return
