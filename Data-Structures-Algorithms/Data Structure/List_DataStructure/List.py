import ctypes
class mylyst:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_list(self.size)
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
         
        self.A [self.n] = item
        self.n = self.n + 1
    
    def __resize(self,new_capacity):
        B = self.__make_list(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
    
    def  __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) +','
        return "["+ result[:-1] +"]"
    
    def __getitem__(self,index):
        if index < self.n:
            return self.A[index]
        else:
            return "IndexError - Index out of range!"
        
    def __delitem__(self, index):
        if 0<= index <self.n:
            for i in range(index, self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n-1
        else:
            print("IndexError: list assignment index out of range!")
    
    
    def remove(self, item):
        if item in self.A:
            for i in range(self.n):
                if self.A[i] == item:
                    self.__delitem__(i)
        else:
            print("ValueError: list.remove(x): x not in list!")
    
    def pop(self):
        if  0<self.n:
            print(self.A[self.n-1])
            self.n = self.n-1
        elif 0 == self.n:
            return []
        
    def clear(self):
        self.n = 0
        self.size =1
    
    def find(self, item):
        for i in range(self.n):
            if item == self.A[i]:
                return i
        return "ValueError : Not found!"
    
    def insert(self, index, item):
        if self.n == self.size:
            self.__resize(self.size*2)
            
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]
            
        self.A[index] = item
        self.n = self.n + 1

    def __make_list(self, capacity):
        return (capacity * ctypes.py_object)()
    
            