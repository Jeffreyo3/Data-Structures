"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"N: {self.value}"
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f"Head: {self.head}\nTail: {self.tail}\nLength: {self.length}"
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create variable to hold the new node 
        # & assign its next to the current list head
        new_node = ListNode(value)
        new_node.next = self.head
        
        # if list is empty, make first added node the tail
        if self.head is None:
            self.tail = new_node
        # if list already has items in it, assign the new node
        # to be the previous of the current head
        else:
            self.head.prev = new_node
        
        # set the head of the list to the new node & increase length
        self.head = new_node
        self.length += 1
        return self

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if there is already no head, do nothing
        if self.head is None:
            return self
        # if the head and tail are the same, 'reset' list
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return self
        # set head to next item in list & reduce length
        else:
            self.head = self.head.next
            self.length -= 1
            return self
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

listything = DoublyLinkedList()
print(listything)
listything.add_to_head(1)
listything.add_to_head(2)
listything.add_to_head(3)
print(listything)
listything.add_to_head(4)
listything.add_to_head(5)
listything.add_to_head(6)
print(listything)


listything.remove_from_head()
print(listything)
listything.remove_from_head()
print(listything)
listything.remove_from_head()
print(listything)
listything.remove_from_head()
print(listything)
listything.remove_from_head()
print(listything)