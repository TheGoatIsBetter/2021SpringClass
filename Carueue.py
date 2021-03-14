
#Stacking list... like how you stack plates and remove them from the same stack at the top
class Stack(list):
    def __init__(self):
        super().__init__()

    def pop(self):
        return super().pop(-1)

    def contains(self,item):
        return self.__contains__(item)



#creates a stack
stacklist = Stack()


#Think of a stack like a stack of plates, you put on the top and take from the top
print('STACK PROOF:')
print(stacklist.contains('Thing0'))
stacklist.append('0')
print(stacklist.contains('Thing0'))
stacklist.append('1')
stacklist.append('2')
stacklist.append('3')
stacklist.append('4')
stacklist.append('1')
print(stacklist)
print(stacklist.pop())
print(stacklist.pop())
print(stacklist.pop())


#Queue... like a line waiting for food, the first there gets out first
class Queue(list):
    def __init__(self):
        super().__init__()

    def pop(self):
        return super().pop(0)

    def contains(self, item):
        return self.__contains__(item)

    def carueue(self):
        index_location = super().index("Carmen Sandiego")
        print(f'Carmen Sandiego is at index {index_location}.')


#creates a queue
queuelist = Queue()

print('QUEUE PROOF:')
print(queuelist.contains('0'))
queuelist.append('0')
print(queuelist.contains('0'))
queuelist.append('1')
queuelist.append('2')
queuelist.append('3')
queuelist.append('4')
queuelist.append('1')
print(queuelist)
print(queuelist.pop())
print(queuelist.pop())
print(queuelist.pop())

#carmen proof
print('CARMEN PROOF:')
carueuelist = Queue()
carueuelist.append('0')
carueuelist.append('1')
carueuelist.append('2')
carueuelist.append('Carmen Sandiego')
carueuelist.append('3')
carueuelist.append('4')
carueuelist.carueue()



