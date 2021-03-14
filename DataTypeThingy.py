class Stack(list):
    def __init__(self):
        super().__init__()

    def pop(self):
        return_thing = self[-1]
        self.remove(return_thing)
        return return_thing

    def contains(self,item):
        return self.__contains__(item)



#creates a stack
stacklist = Stack()

print('STACK PROOF:')
print(stacklist.contains('Thing0'))
stacklist.append('0')
print(stacklist.contains('Thing0'))
print(stacklist)
stacklist.append('1')
stacklist.append('2')
stacklist.append('3')
stacklist.append('4')
stacklist.append('1')
print(stacklist)
print(stacklist.pop())
print(stacklist.pop())
print(stacklist.pop())