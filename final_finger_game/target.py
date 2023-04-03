# Target class:
# a parent class for all target elements: fingers and cursor
# a shared function is random(a,b), to give the target a new random location
# a shared color (170)

import js
p5 = js.window

class Target:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.c=170
    def random(self,a,b):
        self.x = p5.random(a,b)
        self.y = p5.random(a,b)
class CursorTarget(Target):
    def draw(self):
        p5.noFill()
        p5.stroke(self.c)
        p5.strokeWeight(2)
        p5.push()
        p5.translate(self.x+10,self.y)  
        p5.rotate(p5.radians(-45))     
        p5.triangle(0,0,-5,10,5,10)
        p5.rect(0,10,4,10)
        p5.pop()

class FingerTarget(Target):
    def __init__(self,x=0,y=0,l=70,w=18):
        self.x=x
        self.y=y
        self.c=170
        self.w=w
        self.l=l
    def draw(self):
        x=self.w/4
        p5.strokeWeight(2)
        p5.push()
        p5.translate(self.x,self.y)
        p5.stroke(self.c)
        p5.noFill()
        p5.rect(0,0,self.w,self.l)
        #finger tip
        p5.ellipse(0,0-self.l/2,self.w,self.w)
        p5.rect(0,0-self.l/2,self.w/3*2,13)
        p5.ellipse(0,0-self.l/2-5,self.w/3*2,10)
        #finger wrinkles       
        p5.line(0-x,0-self.l/3+3,0+x,0-self.l/3+3)
        p5.line(0-x,0-self.l/3,0+x,0-self.l/3)
        p5.line(0-x,0,0+x,0)
        p5.line(-2-x,0+3,2+x,0+3)
        p5.line(0-x,0+6,0+x,0+6)
        p5.pop()
    # a slight variation of random function:
    # mid_finger can only move with y, and ring and index can only move with x 
    def random(self,a,b):
        if self.l == 100 and self.w == 18:
            # mid finger
            self.x = 100
            self.y = p5.random(a,b)
        else:
            #ring and index finger
            self.x = p5.random(a,b)
            self.y = 510
    

