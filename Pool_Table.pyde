'''WCM POW August 28, 2017
Pool Table Problem'''

#scale factor
scl = 30

ballList = []

class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def update(self):
        fill(0)
        ellipse(self.x*scl,self.y*scl,10,10)
        
class Trail:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def update(self):
        fill(0,0,255) #blue
        ellipse(self.x*scl,self.y*scl,2,2)

        
class Cueball():
    def __init__(self):
        self.x = 0
        self.y = 0        
        self.bounces = 0
        self.xvel = 0.5
        self.yvel = 0.5
        
    def update(self):
        #left wall
        if self.x <= 0 and self.xvel < 0:
            self.x = 0
            self.xvel = -self.xvel
            self.bounces += 1
            println(str(self.x)+','+str(self.y))
            ballList.append(Ball(self.x,self.y))
        #right wall
        if self.x >= 12 and self.xvel > 0:
            self.x = 12
            self.xvel = -self.xvel
            self.bounces += 1
            println(str(self.x)+','+str(self.y))
            ballList.append(Ball(self.x,self.y))
        #top wall
        if self.y <= 0 and self.yvel < 0:
            self.y = 0
            self.yvel = -self.yvel
            self.bounces += 1
            println(str(self.x)+','+str(self.y))
            ballList.append(Ball(self.x,self.y))
        #bottom wall
        if self.y >= 10 and self.yvel > 0:
            self.y = 10
            self.yvel = -self.yvel
            self.bounces += 1
            println(str(self.x)+','+str(self.y))
            ballList.append(Ball(self.x,self.y))
            
        #increment position by velocity
        self.x += self.xvel
        self.y += self.yvel
        #draw trail
        ballList.append(Trail(self.x,self.y))
        #draw ball
        fill(255,0,0)
        ellipse(self.x*scl,self.y*scl,20,20)
        #if self.cue:
        #if it's in a pocket (0,0),(0,10),(12,0),(12,10)
        if self.x == 0:
            if self.y == 0 or self.y == 10:
                println("Done"+','+str(self.bounces))
                noLoop()
        if self.x == 12:
            if self.y == 0 or self.y == 10:
                println("Done"+','+str(self.bounces))
                noLoop()

def setup():
    size(600,600)
    ballList.append(Cueball())
    
def draw():
    background(255)
    println(len(ballList))
    translate(100,100)
    #table
    fill(0,255,0) #green
    rect(0,0,12*scl,10*scl)
    for ball in ballList:
        ball.update()
    