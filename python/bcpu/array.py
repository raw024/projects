from bcpu import *

array = """

Set(r10,0) #start of array
Set(r1,0) # data

Store(r10,r1)
Addi(r10,r10,1)
Addi(r1,r1,1)
Subi(r13,pc,3)
Subi(r2,r1,10) # array size 10
Moven(pc,r13,r2)



"""

load(array)
run()
