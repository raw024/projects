from bcpu import *

stack = """

Set(r10,0) #start of array address

#push 7
Addi(r10,r10,1)
Set(r1,7) # <<<<
Store(r10,R1)

#pop into r2
Load(r2,r10) #<<<<
Subi(r10,r10,1)

#checkempty
Subi(r6,r10,0) #<<<<<
#check if r6 == 0


"""

load(stack)
run()
