


class stack:
    def __init__(self):
        self.values=[]
        def push (self,x):
            self.values = [x] + self.values
            
        def pop (self,x):
            return self.values.pop(0)
            
obj = stack()
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.values)