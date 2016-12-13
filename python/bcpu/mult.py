from bcpu import *

mult = """

Set(r3,10)
Set(r2,11)
Set(r1,1)

And(r7,r1,r2)
Set(r5,0)
Movex(r5,r3,r7)
Set(r4,0)
Add(r4,r4,r5)
Add(r1,r1,r1)
Add(r3,r3,r3)

And(r7,r1,r2)
Set(r5,0)
Movex(r5,r3,r7)
Add(r4,r4,r5)
Add(r1,r1,r1)
Add(r3,r3,r3)

And(r7,r1,r2)
Set(r5,0)
Movex(r5,r3,r7)
Add(r4,r4,r5)
Add(r1,r1,r1)
Add(r3,r3,r3)

And(r7,r1,r2)
Set(r5,0)
Movex(r5,r3,r7)
Add(r4,r4,r5)
Add(r1,r1,r1)
Add(r3,r3,r3)

And(r7,r1,r2)
Set(r5,0)
Movex(r5,r3,r7)
Add(r4,r4,r5)
Add(r1,r1,r1)
Add(r3,r3,r3)

Set(r5,0)
And(r7,r1,r2)
Movex(r5,r3,r7)
Add(r4,r4,r5)

"""

load(mult)
run()
