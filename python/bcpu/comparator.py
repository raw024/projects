from bcpu import *

equal = """

Set(R0,0)
Or(R3,R1,R2)
And(R4,R1,R2)
Not(R4,R4)
And(R3,R3,R4)
Set(R4,1)
Movez(R0,R4,R3)



"""

notequal = """

Set(R0,0)
Or(R3,R1,R2)
And(R4,R1,R2)
Not(R4,R4)
And(R3,R3,R4)
Set(R4,1)
Movex(R0,R4,R3)



"""

lessthan = """

Sub(R3,R1,R2)
Set(R0,0)
Set(R4,1)
Moven(R0,R4,R3)



"""

greaterthan = """

Sub(R3,R2,R1)
Set(R0,0)
Set(R4,1)
Moven(R0,R4,R3)



"""

lessthanorequal = """

Sub(R3,R2,R1)
Set(R0,0)
Set(R4,1)
Movep(R0,R4,R3)



"""

greaterthanorequal = """

Sub(R3,R1,R2)
Set(R0,0)
Set(R4,1)
Movep(R0,R4,R3)



"""

load(equal)
run()
