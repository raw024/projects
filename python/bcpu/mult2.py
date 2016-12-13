from bcpu import *

mult = """

Set(r3,24)
Set(r2,12)

Set(r1,1)
Set(r9,15)
Set(r4,0)

And(r7,r1,r2)
Set(r5,0)
Movex(r5,r3,r7)
Add(r4,r4,r5)
Add(r1,r1,r1)
Add(r3,r3,r3)

Subi(r9,r9,1)

Subi(r8,pc,7)

Movep(pc,r8,r9)

Set(r5,0)
And(r7,r1,r2)
Movex(r5,r3,r7)
Add(r4,r4,r5)

"""

load(mult)
run()
