import sys
import re


class Queue:
    def __init__(self):
        self.elements=[]

    def getSize(self):
        return len(self.elements)

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        temp = self.elements[0]
        self.elements.pop(0)
        return temp

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def getInOneLine(self):
        print(' '.join(map(str, self.elements))) 


class Stack:

    def __init__(self, size=10):
        self.elements= []
        self.size = size

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.elements.append(value)
        
    def pop(self):
        element = self.elements[len(self.elements)- 1]
        self.elements.pop()
        return element

    def put(self, value):
        self.elements.pop()
        self.elements.append(value)

    def peek(self):
        return self.elements[len(self.elements) - 1]

    def expand(self):
        #second_size = len(self.elements)*2
        #self.elements [second_size] = []
        self.size = self.size *2

    def getInOneLine(self):
        print(' '.join(map(str, self.elements))) 

    def getSize(self):
        return len(self.elements)

    def getCapacity(self):
        return self.size


class Node:
    def __init__(self, val):
        self.elements = val


class LinkedList:
    def __init__(self):
        self.elements = []

    def getList(self):
        print(' '.join(map(str, self.elements))) 

    def insertFront(self, new_data):
        self.elements = [new_data] + self.elements

    def insertEnd(self, new_data):
        self.elements.append(new_data)

    def reverse(self):
        self.elements.reverse()


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
