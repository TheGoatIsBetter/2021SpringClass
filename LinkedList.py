class Node:
    #has information of itself, as well as a pointer to the next node
    def __init__(self, stuff, next_node=None):
        self.stuff = stuff
        self.next = next_node

    def __repr__(self):
        return str(self.stuff)

#honestly this is pretty much a tweak of Joe's with a few tiny optimizations and a whole lot of comments... (I'd like to note some of the optimizations you mentioned in class, I had already optimized before you mentioned)
class LinkedList:
    def __init__(self, data=[]):
        self.head = None
        if data:
            previous_node = None
            for thing in data:
                #make new node
                new_node = Node(thing)
                #if self.head doesn't exist make it the new node
                if not self.head:
                    self.head = new_node
                #else make a new node on the one after the previous node
                else:
                    previous_node.next = new_node
                #make that new node the previous node to move on
                previous_node = new_node
    
    def _get_tail(self):
        #sets current to head
        current_node = self.head
        #while there is a head and node after the head
        while current_node and current_node.next:
            #set current to one after the current
            current_node = current_node.next
        #return the where it leaves off when it eventually has no next node
        return current_node


    def append_left(self, thing):
        #makes a new node that has the next thing as the current head
        new_node = Node(thing, self.head)
        #sets head to the new node instead as it is on the left now
        self.head = new_node

    def append_right(self,thing):
        if self.head:
            #gets tail
            tail_node = self._get_tail()
            #sets the thing after tail to new node
            tail_node.next = Node(thing)
        else:
            #if there is no data, make new node at head instead
            self.head = Node(thing)

    def pop_left(self):
        #pops the left off and returns it
        old_head = self.head
        self.head = self.head.next
        return old_head

    def pop_right(self):
        #pops right using same concept as trailing node, however it is sure to set the next of the previous node to None
        previous_node = None
        current_node = self.head
        while current_node and current_node.next:
            previous_node = current_node
            current_node = current_node.next
        if previous_node:
            previous_node.next = None
        else:
            self.head = None
        return current_node

    def __repr__(self):
        #records nodes into a list and returns said list as representation
        current_node = self.head
        nodes_contents = []
        while current_node:
            nodes_contents.append(current_node.contents)
            current_node = current_node.next
        nodes_contents.append("None")
        return nodes_contents

Listthing = LinkedList(['thing1','thing2','thing3'])
