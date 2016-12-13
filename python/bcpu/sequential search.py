from bcpu import *

array = """

Set(r10,10) #start of array
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


#test
Set(r1,9) # <<< key

sequentialsearch = """

Set(r3,0)
Subi(r3,r3,1) # answer will default to -1
Set(r11,0) # index

Set(r10,10) # << index 0 (WHERE THE FIRST INDEX OF THE ARRAY IS STORED
Load(r2,r10) # <<<<loop to here
Sub(r5,r2,r1) # compare
Addi(r13,pc,7)
Movez(pc,r13,r5) # break, goto found

Addi(r10,r10,1) #address increment
Addi(r11,r11,1) #index increment
Subi(r12,r11,10) # << array size = 10
Subi(r14,pc,7)
Moven(pc,r14,r12)

Movez(r3,r11,r5) # check found







"""

load(sequentialsearch)
run()











































