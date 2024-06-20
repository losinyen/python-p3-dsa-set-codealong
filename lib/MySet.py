class MySet:
    def __init__(self, enumerable = []):

        self.dictionary = {}
        
        for value in enumerable:
            self.dictionary[value] = True

    def has(self,values):
        return values in self.dictionary 


    def add(self,values):
        self.dictionary[values]=True
        return self          

    def delete(self,values):
        self.dictionary.pop(values, None)
        return self
    
    def size(self):
         return len(self.dictionary)


set = MySet([1, 2, 3])

print(set)
