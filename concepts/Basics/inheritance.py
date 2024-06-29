class a:
    def c(self):
        print("C")
        
class b:
    def d(self):
        print("D")
        
class g(a,b):
    def h(slef):
        print("H")
class j(b):
    def k(self):
        print("K")
f=b()
f.c()

#Multilevel==>a->b->c
#Multiple==>a,b->c

