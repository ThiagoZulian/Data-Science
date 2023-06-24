from SingleLinkedList import SingleLinkedList


if __name__ == '__main__':

    list1 = SingleLinkedList()

    for x in range(1, 10):
        list1.append(x)

    list1.insert_at_index(5, 77)

    list1.display()
