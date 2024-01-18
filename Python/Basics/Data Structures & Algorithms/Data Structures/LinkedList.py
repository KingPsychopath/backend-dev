class Node:
    def __init__(self, data):
        """
        a node in a singly linked list.
        """
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """
        a singly linked list.
        """
        self.head = None

    # Adds a node to the end of the linked list
    def append(self, data):
        """
        append a node to the end of the linked list.
        """
        # Create Node with Data passed through append method
        new_node = Node(data)

        # Check if head(start of linkedlist) is None; if so, set head to new_node
        if self.head is None:
            self.head = new_node
            return
        
        # Create a variable to keep track of the current node
        current_node = self.head

        # Iterate through the linked list until we reach the end
        while current_node.next:
            current_node = current_node.next

        # Set the current node's next pointer to the new node
        current_node.next = new_node

    # Adds a node to the beginning of the linked list
    def prepend(self, data):
        """
        prepend a node to the beginning of the linked list.
        """
        # Create Node with Data passed through prepend method
        new_node = Node(data)

        # Set new_node's next pointer to the current head
        new_node.next = self.head

        # Set head to new_node
        self.head = new_node

    def delete(self, data):
        """
        delete a node from the linked list.
        """

        # If the head node is the one we want to delete, set the head to the next node
        if self.head.data == data:
            self.head = self.head.next
            return
        # Typically where you'd do garbage collection in other languages i.e. C++

        # Create a variable to keep track of the current node
        current_node = self.head

        # Iterate through the linked list until we reach the end
        while current_node.next:
            # If the next node has the data value for the node we are looking for, 
            # Set the current node's pointer to it's pointer (effectively deleting it)

            if current_node.next.data == data:
                current_node.next = current_node.next.next 
                return

            # Otherwise, move on to the next node - deletion node not found
            current_node = current_node.next

        print("Node with data '%s' not found" % data)


    def insert(self, prev_node, data):
        """
        insert a node after a specific node.
        """
        # Create Node with Data passed through insert_after_node method
        new_node = Node(data)

        # Set new_node's next pointer to the previous node's next pointer
        new_node.next = prev_node.next

        # Set previous node's next pointer to new_node
        prev_node.next = new_node

    def print_list(self):
        """
        print the linked list.
        """
        # Create a variable to keep track of the current node
        current_node = self.head

        # Iterate through the linked list until we reach the end
        inc = 0
        while current_node:
            print(f'Node {inc}: {current_node.data}', end=', ')
            current_node = current_node.next
            inc += 1


# Testing

# Create a linked list
testList = LinkedList()
testList.append('A')
testList.append('B')
testList.append('C')
testList.append('D')

testList.print_list()
print('\n')

testList.prepend('Z')
testList.delete('C')

testList.print_list()
print('\n')

# Insert 'E' after the second node in the List
testList.insert(testList.head.next, 'E')

testList.print_list()
print('\n')
