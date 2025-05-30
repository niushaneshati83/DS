import unittest
import sys
import functools
import re
def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if attr == 'Node':
                setattr(cls, attr, getattr(cls, attr))
            elif callable(getattr(cls, attr)) :
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

@for_all_methods(staticmethod)
class Utils():
    def parse_line(line, delimiter=' '):
        index = line.index(delimiter) if delimiter in line else None
        if index is None:
            return [line, None]
        result = line[0:index]
        remainingLine = line[index + 1:]
        return [result, remainingLine]

    def delete_end_char(line):
        return line.rstrip(line[-1])

    def get_attribute_pointer(object, attribute):
        return getattr(object, attribute)

    def get_args(argsLine):
        return argsLine.split(',') if len(argsLine) != 0 else []

    def run_function(attribute, args):
        result = attribute(*args)
        if result != None:
            print(result)
      
    def covert_args_to_int(args):
        newArgsList = list(args[1:])
        for i in range(1, len(args)):
            if isinstance(args[i], str) and (args[i].isnumeric() or args[i][0] == '-'):
                newArgsList[i - 1] = int(args[i])
        return tuple([args[0]] + newArgsList)
    
    def delete_quotation(args):
        newArgsList = list(args)
        for i in range(1,len(args)):
            if isinstance(newArgsList[i], str):
                newArgsList[i] = newArgsList[i].replace('\'', '')
        return tuple(newArgsList)

def fix_str_arg(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(len(args) > 1):
            args = Utils.delete_quotation(args)
            args = Utils.covert_args_to_int(args)
        return func(*args, **kwargs)
    return wrapper

def print_raised_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val != None:
                return val
        except Exception as e:
            print(str(e))
    return wrapper

class MinHeap:
    class Node:
        def __init__(self,val):
            self.val = val

    def __init__(self):
        self.heap =[]
        self.NOE =0

    def bubble_up(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if not self.NOE:
            raise Exception('empty')
        if index < 0 or index >= self.NOE:
            raise Exception('out of range index')
    
        while index >0:
            if (index-1)//2 >=0 and self.heap[(index-1)//2].val > self.heap[index].val:
                self.heap[(index-1)//2].val,self.heap[index].val=self.heap[index].val,self.heap[(index-1)//2].val
            else: break
            index =(index-1)//2

    def bubble_down(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if not self.NOE:
            raise Exception('empty')
        if index < 0 or index >= self.NOE:
            raise Exception('out of range index')


        min = index
        while 2*index < self.NOE:
            if 2*index+1 < self.NOE and self.heap[min].val > self.heap[2*index+1].val:
                min = 2*index+1
            if 2*index+2 < self.NOE and self.heap[min].val > self.heap[2*index+2].val:
                min = 2*index+2
            if min != index:
                self.heap[min].val,self.heap[index].val=self.heap[index].val,self.heap[min].val
                index = min
            else: break

    def heap_push(self, value):
        new = self.Node(value)
        self.heap.append(new)
        self.NOE +=1
        self.bubble_up(self.NOE-1)

    def heap_pop(self):
        if not self.NOE:
            raise Exception('empty')
        popped = self.heap[0].val
        self.heap[0].val = self.heap[self.NOE-1].val
        self.NOE -=1
        self.heap.pop()
        if self.NOE:self.bubble_down(0)
        return popped
    def find_min_child(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        if index < 0 or index >= self.NOE:
            raise Exception('out of range index')
        if not self.NOE:
            raise Exception('empty')

        if 2*index < self.NOE:
            min = 2*index+1
            if self.heap[2*index+1].val > self.heap[2*index+2].val:
                 min = 2*index+2
        return min      
    def heapify(self, *args):
        for val in args:
            self.heap_push(val)

            
class HuffmanTree:
    def __init__(self):
        self.letters= []
        self.freqs=[]
        self.head = None
        self.encoded = None

    def set_letters(self,*args):
        self.letters=args
        self.encoded = {i:None for i in self.letters }

    def set_repetitions(self,*args):
        self.freqs=args

    class Node:
        def __init__(self,lett,freq,left=None,right=None):
            self.letter = lett
            self.freq = freq
            self.left = left
            self.right = right
            self.dir=""
            #for 1 or 0

    def build_huffman_tree(self):
        nodes = list(zip(self.freqs,self.letters))
        
        nodes = [self.Node(i,j) for j,i in nodes]
        nodes.sort(key = lambda x : (x.freq,x.letter),reverse=True)
        while len(nodes)>1:
           nodes.sort(key = lambda x : (x.freq),reverse=True)
           r = nodes[-1]
           l = nodes[-2]
           nodes = nodes[:-2]
           r.dir="0"
           l.dir="1"
           new_head= self.Node("",r.freq+l.freq,l,r)
           nodes = [new_head] + nodes
           self.head = new_head
        self.encoding(node = self.head)

    def encoding(self,node,huff =""):
        
        n = huff + node.dir
        if node.right:
            self.encoding(node.right,n)
        if node.left:
            self.encoding(node.left,n)
        
        if not node.right and not node.left:
            self.encoded[node.letter] = n

        
    def get_huffman_code_cost(self):
        res =0
        index =0
        for i in self.encoded:
            res += self.freqs[index]*len(self.encoded[i])
            index+=1
        return res
        
    def text_encoding(self, text):
        let = {}
        for i in text:
            let[i] = let[i]+1 if i in let else 1
        self.letters= list(let.keys())
        self.freqs = list(let.values())
        self.encoded = {i:None for i in self.letters }
        self.build_huffman_tree()
        

CONST=1e-9
class Bst:
    class Node:
        def __init__(self, data,left_child,right_child,parent):
            self.data = data
            self.left_child = left_child
            self.right_child = right_child
            self.parent = parent

    def __init__(self):
        self.root=self.Node(CONST,None,None,None)

    def insert(self, key):
        if self.root.data == CONST:
            self.root = self.Node(key,None,None,None)
        else:
            current= self.root
            while(True):
                if  current.data>key:
                    if current.left_child != None:
                        current = current.left_child
                    else :
                        new_node=self.Node(key,None,None,current)
                        current.left_child=new_node
                        break
                else:
                    if current.right_child != None:
                        current = current.right_child
                    else :
                        new_node=self.Node(key,None,None,current)
                        current.right_child=new_node
                        break

    def print_inorder(self,k):
        if k==None:
            return
        else:
            self.print_inorder(k.left_child)
            print(k.data,end=" ")
            self.print_inorder(k.right_child)

    def inorder(self):
        self.print_inorder(self.root)

class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
