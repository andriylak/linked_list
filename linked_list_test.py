import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.sequence = LinkedList([2, 7, 4, 9, 18, 19, 22])
        self.empty_sequence = LinkedList([])
        self.single_element_sequence = LinkedList([12])

    def test_to_list(self):
        self.assertEqual(self.sequence.to_list(), [2, 7, 4, 9, 18, 19, 22])     #usual linked list
        self.assertEqual(self.empty_sequence.to_list(), [])                     #empty linked list
        self.assertEqual(self.single_element_sequence.to_list(), [12])          #one element linked list

    def test_len(self):
        self.assertEqual(self.sequence.len(), 7)                          #usual linked list
        self.assertEqual(self.single_element_sequence.len(), 1)           #one element linked list
        self.assertEqual(self.empty_sequence.len(), 0)                    #empty linked list


    def test_delete(self):
        test_cases = [
            (self.sequence, 2, [7, 4, 9, 18, 19, 22]), #deletion of the first element
            (self.sequence, 22, [7, 4, 9, 18, 19]),    #deletion of the last element
            (self.sequence, 9, [7, 4, 18, 19]),        #deletion of the middle element
            (self.sequence, 3, [7, 4, 18, 19]),        #no such element in sequence
            (self.single_element_sequence, 23, [12]),  #no such element in sequence with 1 element
            (self.single_element_sequence, 12, []),    #deletion of the 1 element in single element sequence
            (self.empty_sequence, 23, [])              #deletion in an empty array
        ]
        for linked_list, target, expected_result in test_cases:
            with self.subTest(sequence = linked_list.to_list(), target = target):
                linked_list.delete(target)
                self.assertEqual(linked_list.to_list(), expected_result)
    
    def test_has(self):
        self.assertTrue(self.sequence.has(4)) #element in linked list
        self.assertFalse(self.sequence.has(3)) #element not in linked list

    def test_get(self):
        self.assertEqual(self.sequence.get(4), 18) #index is less than length of linked list
        self.assertIsNone(self.sequence.get(7))    #index is more than length of linked list

    def test_rotate(self):
        test_cases = [
            (self.empty_sequence, []),                  #empty linked list
            (self.single_element_sequence, [12]),       #single element linked list
            (self.sequence, [22, 2, 7, 4, 9, 18, 19])   #usual linked list
        ] 
        for linked_list, result in test_cases:
            with self.subTest(array = linked_list.to_list()):
                linked_list.rotate()
                self.assertEqual(linked_list.to_list(), result)

    def test_starts_with(self): 
        self.assertFalse(self.empty_sequence.starts_with(LinkedList([1, 2, 3])))     #linked list is shorter than sequence
        self.assertTrue(self.sequence.starts_with(LinkedList([2, 7])))               #linked list is longer than sequence, starts
        self.assertFalse(self.sequence.starts_with(LinkedList([2, 8])))              #linked list is longer than sequence, doesn't start

    def test_contain(self): 
        self.assertFalse(self.empty_sequence.contains(LinkedList([1, 2, 3])))        #linked list is shorter than sequence
        self.assertTrue(self.sequence.contains(LinkedList([4, 9, 18])))              #linked list is longer than sequence, inside
        self.assertFalse(self.sequence.contains(LinkedList([4, 10, 18])))            #linked list is longer than sequence, not inside


    def test_ends_with(self): 
        self.assertFalse(self.empty_sequence.ends_with(LinkedList([1, 2, 3])))     #linked list is shorter than sequence
        self.assertTrue(self.sequence.ends_with(LinkedList([9, 18, 19, 22])))      #linked list is longer than sequence, ends
        self.assertFalse(self.sequence.ends_with(LinkedList([23])))                #linked list is longer than sequence, doesn't end

if __name__ == "__main__":
    unittest.main(verbosity=2)