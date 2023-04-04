from vpython import *
from time import *
#ball=sphere(color=color.red)
#mybox=box(color=color.yellow,length=12,width=1,height=(.2))
#myTube=cylinder(color=color.orange,length=12,width=1,height=.5)
#vector(x,y,z) +value moves position UP, -value moves position DOWN
ceiling=box(pos=vector(0,5,0),color=color.white,length=10,height=.1,width=10)
floor=box(pos=vector(0,-5,0),color=color.orange,length=10,height=.1,width=10)
leftWall=box(pos=vector(5,0,0),color=color.green,length=.1,height=10,width=10)
rightWall=box(pos=vector(-5,0,0),color=color.green,length=.1,height=10,width=10)
backWall=box(pos=vector(0,0,-5),color=color.purple,length=10,height=10,width=.1)
while True:
    pass

