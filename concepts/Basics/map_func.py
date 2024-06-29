store=[
    ("Shirt",8),
    ("Pant",10)
]
euro_to=lambda sto:(sto[0],sto[1]*0.81)

store_euro=list(map(euro_to,store))
for i in store_euro:
    print(i)
    
import functools

values=["H","E","L"]

val=functools.reduce(lambda x,y:x+y,values)
print(val)

fact=[1,2,3]

factorial=functools.reduce(lambda x,y:x*y,fact)
print(factorial)