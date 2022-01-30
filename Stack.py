class stack:
    def __init__(self):
        ptr=[]
    
    def delete(self):
        self.ptr.pop()
    def enter(self,a):
        self.ptr.append(a)
    
if __name__=='__main__':
    s=stack()
    s.ptr=['a','b','c','d']
    s.delete()
    s.enter('j')
    print(s.ptr)
