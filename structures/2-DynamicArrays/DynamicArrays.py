"""
    This type of array, memory is allocated at run 
    time and does not have a fixed size. It has a underlying
    static array that is easly replaceable
"""

class Array:
    def __init__ (self, len):
        self.size = 0
        self.capacity = len
        self.arr = [0] * len
        
    def get(index):
        return self.arr[index]
    
    def pushback(i, n):
        self.arr[i] = n
        self.size += 1
        
    def pop():
        self.arr[self.size] = 0
        self.size -= 1
        
    def resize():
        self.capacity *= 2
        newArr = [0] * self.capacity
        
        for i in range(self.size):
            newArr[i] = self.arr[i];
            
        return newArr
    
    def getSize():
        return self.size
    
    def getCapacity():
        return self.capacity
    
arr = Array(5)

