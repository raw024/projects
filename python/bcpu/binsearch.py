from bcpu import *

array = """

Set(r10,0) #start of array
Set(r1,0) # data

Store(r10,1)
Addi(r10,r10,1)
Addi(r1,r1,1)
Subi(r13,pc,3)
Subi(r2,r1,10) # array size 10
Moven(pc,r13,r2)



"""

load(array)
run()


binsearch = """
Set(r1,7) # key
Set(r3,0)
Subi(r3,r3,1) # ans = -1

Set(r4,0) # array Start
Set(r5,9) # array end

Move(r6,r4) # first
Move(r7,r5) # last

Addi(r13,pc,1) # start while label


Sub(r10,r7,r6) # mid

Set(r12, 20)
Add(r12,pc,r12) # done address
Moven(pc,r12,r10) # goto done

#mid // 2
Set(r9,0)
    Subi(r10,r10,2)
Addi(r11,pc,4) # skip to end of div
Moven(pc,r11,r10)
    Addi(r9,r9,1)
Subi(pc,pc,4)
#end of div

Add(r10,r6,r9) #mid = first + mid//2

Load(r2,r10)
Sub(r8,r1,r2) # test = key - L[mid]

Sub(r9,r10,r4) #index of mid
Movez(r3,r9,r8) # ? ==
Addi(r12,pc,7) # done address
Movez(pc,r12,r8) # goto done

Addi(r0,r10,1)
Movep(r6,r0,r8) # test > 0

Subi(r0,r10,1)
Moven(r7,r0,r8) # test < 0

Move(pc,r13) # loop back to start of while

Move(r3,r3) # print answer














"""


load(binsearch)
run()

