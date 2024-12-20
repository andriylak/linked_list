This repository contains simple data structure linked list and methods for this data structure:
  
  - LinkedList(list) - creates a LinkedList that initially holds the values in the given Python list
  - l.to_list() - return a Python list containing the values in this LinkedList
  - l.len() - return the number of nodes in a LinkedList
  - l.get(n) - return the value in the nth node, where nodes are numbered from 0. If n is higher than length of l, returns None
  - l.has(x) - true if the list includes the value x
  - l.delete(x) - delete the first occurrence (if any) of the value x
  - l.rotate() - move the last node in the list to the head of the list; does nothing if the list is empty
  - l.starts_with(m) - true if the elements of the LinkedList m appear at the beginning of l
  - l.contains(m) - true if the elements of the LinkedList m appear in succession anywhere in l
  - l.ends_with(m) - true if the elements of the LinkedList m appear in succession at the end of l
