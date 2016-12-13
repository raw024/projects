from bcpu import *

#put -926 into register
# CORRECT
Q1 = """

Set(r9, 158)
Seth(r9,3)
Set(r0,0)
Sub(r9,r0,r9)

"""

load(Q1)
run()

#put777 into register and store into address 70 then load it into r7
#CORRECT
Q2 = """

Set(r2,9)
Seth(r2,3) # and so forth


"""

load(Q2)
run()

#NOT CORRECT :'(
Q3 = """

Set(r8,0b11110011)
Seth(r8,0b11110000)
Set(r1,0b1100000)
Not(r1,r1)
And(r8,r8,r1)
Set(r1,0)
Seth(r1,0b00001100)
Or(r8,r8,r1)




"""


load(Q3)
run()



#test for Q 4
Set(r3,4)
#MAYBE INCORRECT
Q4 = """

Set(r3,4) # test

Set(r0,0) # counter
Set(r4,1)
Addi(r10,pc,6) # goto end
Sub(r5,r3,r0)
Movez(pc,r10,r5)
Add(r4,r4,r4)
Addi(r0,r0,1)
Subi(pc,pc,4)
Move(r4,r4) #end


"""

load(Q4)
run()

#CORRECT
Q5 = """

Set(r5,1)
Set(r10,70) #start of array
Set(r1,70) # data
Set(r11,83)
Set(r4,2)

Store(r10,r1)
Addi(r10,r10,1)
Add(r1,r1,r4)
Subi(r13,pc,3)
Sub(r2,r1,r11) # array size 10
Moven(pc,r13,r2)

Subi(r5,r5,1)
Set(r11,9)
Set(r4,1)
Set(r1,2)
Movez(pc,r13,r5)


"""

load(Q5)
run()

#INCORRECT
Q6 = """

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

load(Q6)
run()

#test for Q 7
Set(r6,9)

Q7 = """

Subi(r6,r6,8)

Addi(r5,pc,9)
Moven(pc,r5,r6) #equals 7

Addi(r5,pc,10)
Movez(pc,r5,r6) # equals 8

Addi(r5,pc,11)
Movep(pc,r5,r6) # equals 9

Set(r7,0)
Set(r4,4)
Addi(pc,pc,9)

Set(r7,7)
Set(r1,1)
Addi(pc,pc,6)

Set(r7,8)
Set(r2,2)
Addi(pc,pc,3)

Set(r7,9)
Set(r3,3)



"""

load(Q7)
run()

Q8 = """

Set(r2,20)
Addi(r4,pc,8)


Set(r3,0)
Set(r1,1)


Sub(r5,r3,r2)
Movep(pc,r4,r5)
Add(r3,r3,r1)
Addi(r1,r1,2)

Subi(pc,pc,4) #loop back

Move(r3,r3)

"""

load(Q8)
run()


Q9 = """

Set(r0,0)
Set(r1,1)
Subi(r6,r0,1)
Subi(r7,r0,1)
Subi(r8,r0,1)



Set(r10,80)
Set(r11,80)


Addi(r10,r10,1)
Set(r1,10)
Store(r10,r1)


Set(r1,11)
Store(r10,r1)
Addi(r10,r10,1)

Subi(r5,r10,r11)
Addi(r3,pc,4)
Movez(pc,r3,r5)      # check if zero before continuing

Load(r6,r10)
Subi(r10,r10,1)







Subi(r5,r10,r11)
Addi(r3,pc,4)
Movez(pc,r3,r5)  # check if zero before continuing

Load(r7,r10)
Subi(r10,r10,1)






Subi(r5,r10,r11)
Addi(r3,pc,4)
Movez(pc,r3,r5) # check if zero before continuing

Load(r8,r10)
Subi(r10,r10,1)










"""

load(Q9)
run()

Q10 = """

Set(r6,0b11001100)
Seth(r6,0b11001111) #test
Move(r7,r6)

Set(r1,1)
Not(r3,r1)
And(r7,r7,r3)

Set(r4,1)

Set(r5,0)
Moven(r5,r1,r7)
Add(r7,r7,r7)
Add(r7,r7,r5)
Add(r4,r4,r4)
Subi(r13,pc,5)
Movep(pc,r13,r4)

Move(r7,r7)



"""

load(Q10)
run()
















