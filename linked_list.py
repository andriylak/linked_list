
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, array):
        self.head = None
        for value in reversed(array):
            self.head = Node(value, self.head)
        self.length = len(array)

    def to_list(self):
        result = []
        element = self.head
        while element != None:
            result.append(element.value)
            element = element.next
        return result

    def len(self):
        return self.length

    def get(self, n):
        if n >= self.length:
            return None
        else:
            element = self.head
            while (element != None) and (n > 0):
                element = element.next
                n -= 1
            return element.value

    def has(self, target):
        element = self.head
        while element != None:
            if element.value == target:
                return True
            element = element.next
        return False

    def delete(self, target):
        element = self.head
        if element == None:
            pass
        elif self.head.value == target:
            self.head = element.next
            self.length -= 1
        else:
            Delete = True
            while (Delete) and (element.next != None):
                if element.next.value == target:
                    element.next = element.next.next
                    Delete = False
                    self.length -= 1
                element = element.next

    def rotate(self):
        if self.length > 1:
            element = self.head
            while element.next.next != None:
                element = element.next
            self.head = Node(element.next.value, self.head)
            element.next = None

    def starts_with(self, target_seq):
        return starts(self.head, target_seq.head)

    def contains(self, target_seq):
        element = self.head
        while element != None:
            if starts(element, target_seq.head):
                return True
            element = element.next
        return False

    def ends_with(self, target_seq):
        if target_seq.length > self.length:
            return False
        element = self.head
        for i in range(self.length - target_seq.length):
            element = element.next
        return starts(element, target_seq.head)


# helper function that that takes two Node pointers, and returns True if the linked list sequence1 starts with the values in sequence2
def starts(sequence1, sequence2):
    while sequence2 != None:
        if (sequence1 == None) or (sequence1.value != sequence2.value):
            return False
        sequence1 = sequence1.next
        sequence2 = sequence2.next
    return True
