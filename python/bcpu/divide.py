from bcpu import *

#test
Set(r1,3)
Set(r2,7)

divide = """

Set(r3,0)
Set(r4,0)

Sub(r2,r2,r1) # loop begin

Addi(r13,pc,6)
Moven(pc,r13,r2) # goto reverse

Addi(r3,r3,1) 

Addi(r13,pc,4)
Movez(pc,r13,r2) # goto end


Subi(pc,pc,6) #loop back

Add(r2,r2,r1) # reverse last subtraction


Move(r3,r3)
Move(r4,r2)

"""

load(divide)
run()
