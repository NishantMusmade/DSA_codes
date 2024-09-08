class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.n = 0

    def __str__(self):
        curr = self.top
        result = ''
        while curr!=None:
            result = result + str(curr.data)
            curr = curr.next
        return result
    
    def isEmpty(self):
        return self.top == None
    
    def peek(self):
        return self.top.data
    
    def size(self):
        return self.n
    
    def push(self,data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.n = self.n+1

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        else:
            element = self.top
            self.top = self.top.next
            element.next = None
            self.n = self.n-1

    
s = stack()
print(s)

dec_num = int(input("Enter a decimal number: "))
i=5
while dec_num > 0:
    remainder = dec_num%2
    s.push(remainder)
    dec_num = dec_num//2

print('The binary conversion of decimal is :',s)
