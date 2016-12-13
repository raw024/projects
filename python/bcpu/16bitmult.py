from bcpu import *

sixteenbitmult = """
Set(R1,4) # Your input values
Seth(R1,0) # Set High Bits if Needed
Set(R2,6)
Seth(R2,0)

Move(R3,R2) #Copy R2 in order to bit-shift it. 
# R2 in Comments really refers to value in R3.

Set(R8,16) # Loop Constraint
Set(R9,0) # Outside Loop Index
Set(R10,0) # Inside Loop Index
Set(R11,111) # Outside Loop Jump Location
Set(R12,112) # Inside Loop Jump Location

Set(R4,0b1) # Bitmask for R1

# Beginning of Outside Loop
And(R5,R1,R4) # Set Bitmask for R2

# Beginning of Inside Loop
And(R6,R5,R3) # Get Product of Bits
Add(R7,R7,R6) # Add to Running Total
Add(R5,R5,R5) # Shift to Next Bit for R2
# End of Inside Loop

Addi(R10,R10,1) # Incrament Inside Index
Sub(R13,R10,R8) # Subtract Index from Constraint
Moven(PC,R12,R13) # Jump to beginning of Loop if Index less than Constraint
Set(R10,0) # Reset Index if Inside Loop is Over

Add(R3,R3,R3) # Shift R2 for Next R1 Bit (Adds the Zero to the right when multipling it out)
Add(R4,R4,R4) # Shift R1 Bitmask to next Bit
# End of Outside Loop

Addi(R9,R9,1) # Incrament Outside Index
Sub(R13,R9,R8) # Subtract Index from Constraint
Moven(PC,R11,R13) # Jump to beginning of Loop if Index less than Constraint
Set(R9,0) # Reset Index if Outside Loop is Over, not really nessicary, but eh.

Move(R7,R7)

"""
