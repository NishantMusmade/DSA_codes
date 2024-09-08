# We are assuming that the number of elements from which we have to find mean are known before hand
# So, we will use array for stack implementation, and also we dont have to do insertion and deletion operation
# the motive of this code is to find minimum element in O(1) time complexity

#regular stack operations
class stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    
    def __str__(self):
        return str(self.stack)

    def isEmpty(self):
        return self.top == -1

    def push(self,data):
        if self.top == self.size -1:
            return 'Stack Overflow'
        else:
            self.top = self.top + 1
            self.stack[self.top] = data
    
    def pop(self):
        if self.top == -1:
            return 'Stack Underflow'
        else:
            element = self.stack[self.top]
            self.top = self.top - 1
    
    def peek(self):
        if self.top == -1:
            return 'Stack is empty'
        else:
            return stack[self.top]

#Stack for efficient finding of minimum element  
class efficient_stack:
    def __init__(self):
        self.rStack = stack(size)   #r for regular
        self.minStack = stack(1) #for minimum element

    def push(self,data):
        self.rStack.push(data)

        if self.minStack.isEmpty():
            self.minStack.push(data)
        else:
            if self.minStack.top > data:
                self.minStack.pop()
                self.minStack.push(data)
        
        print('Regular stack: ',self.rStack)
        print('Min stack: ',self.minStack)

    def min(self):
        if self.minStack.top == -1:
            return 'Minimum stack is empty'
        else:
            return self.minStack.stack[self.minStack.top]

elements = input('Enter the elements: ').split()
print(elements)
size = len(elements)

e = efficient_stack()

for i in elements:
    e.push(int(i))


print(e.min())




