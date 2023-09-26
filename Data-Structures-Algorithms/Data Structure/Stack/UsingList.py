class stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size    #here we need to private __stack
        self.top = -1
        
        
    def push(self,value):
        if self.size -1 == self.top:
            return 'Stack Overflow!'
        self.top += 1 
        self.stack[self.top] = value
            
    def pop(self):
        if self.top == -1:
            return 'Stack is already Empty!'
        else:
            data = self.stack[self.top]
            self.top -= 1
            return data
        
    def traverse(self):
        res = ''
        for i in range(self.top + 1):
            res = res + str(self.stack[i]) + '-'
        return res[-1]
            