#from Node import Node

class Node:
    #has information of itself, as well as a pointer to the next node
    def __init__(self, stuff, next_node=None, prev_node=None):
        self.stuff = stuff
        self.next = next_node
        self.prev = prev_node

    def __repr__(self):
        return str(self.stuff)

#took init and repr from Joe, as well as the idea to use Node import
class DoublyLinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        if args:
            nodes = [Node(arg) for arg in args]
            #creates nodes in list
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
                nodes[i + 1].prev = nodes[i]
            self.head = nodes[0]
            self.tail = nodes[-1]

    def __repr__(self):
        current_node = self.head
        results = ''
        while current_node:
            results += str(current_node) + '\n'
            current_node = current_node.next
        return results

    def add_head(self, new_node):
        new_node = Node(new_node)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            #set the current head's previous and the new nodes next to the current head
            self.head.prev = new_node
            new_node.next = self.head
            #set the new nodes previous to none and then set it to the new head
            new_node.prev = None
            self.head = new_node

    def add_tail(self, new_node):
        new_node = Node(new_node)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            #set the current tail's next and the new nodes prev to the current tail
            self.tail.next = new_node
            new_node.prev = self.tail
            #set the new nodes next to none and then set it to the new tail
            new_node.next = None
            self.tail = new_node


    #I could definitely make this smaller with some black magic crap but I'd rather not... this took long enough...
    def pop(self, position):
        tail_of_list = False
        head_of_list = False
        current_position = 0
        #checks to see if the bounds have been overstepped in either direction, and if so, flags whichever end it is to be the pop
        #if using positive position
        if position >= 0:
            try:
                current_node = self.head
                for i in range(position):
                    current_position += 1
                    current_node = current_node.next
                    if current_node == None:
                        raise ReferenceError()         
            except:
                tail_of_list = True
                if position > current_position:
                    print(f"Position {position} requested bigger than amount of the {current_position} list nodes present, using tail instead")
        #if using negative position
        else:
            try:
                current_node = self.tail
                for i in range(abs(position)-1):
                    current_position += 1
                    current_node = current_node.prev
                    if current_node == None:
                        raise ReferenceError()         
            except:
                head_of_list = True
                if position < current_position:
                    print(f"Position {abs(position)} requested bigger than amount of the {current_position} list nodes present, using head instead")

        #pops head
        if position == 0 or head_of_list:
            result = self.head
            self.head = self.head.next
            self.head.prev = None

        #pops tail
        elif position == -1 or tail_of_list:
            result = self.tail
            self.tail = self.tail.prev
            self.tail.next = None

        #pops anything in between
        else:
            #if not negative pos
            if abs(position) == position:
                current_node = self.head
                for i in range(position):
                    current_node = current_node.next
            #if negative pos
            else:
                current_node = self.tail
                for i in range(abs(position)-1):
                    current_node = current_node.prev

            #sets result and connects other nodes
            result = current_node

            next_node = current_node.next
            prev_node = current_node.prev

            prev_node.next = next_node
            next_node.prev = prev_node

        return result
        

#this was also taken from Joe for simplicities sake
if __name__ == "__main__":
    test_list = DoublyLinkedList(1)
    print(test_list)
    print(test_list.head == test_list.tail)
    test_list.add_head(42)
    print('after addition at head:')
    print(test_list)
    test_list.add_tail(Node("billy"))
    print('after addition at tail:')
    print(test_list)
    print(f"Pop: {test_list.pop(-2)}") #any position based on number, negatives work too!
    print('after pop:')
    print(test_list)
    
   

