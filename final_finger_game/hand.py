# hand class: 
# to integrate 5 fingers as a whole LeftHand
# hand = LeftHand(x,y) or RightHand to create a new hand at position(x,y)[CENTER]
# hand.draw() to draw

from player import Finger
import js
p5 = js.window
little_l = 50
little_w = 14
ring_l = 80
ring_w = 16
mid_l = 100
mid_w = 18
index_l = 70
index_w = 18
thumb_l = 30
thumb_w = 20
class LeftHand:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.little=Finger(self.x-40,self.y+20,little_l,little_w)
        self.ring=Finger(self.x-20,self.y+10,ring_l,ring_w)
        self.mid=Finger(self.x,self.y,mid_l,mid_w)
        self.index=Finger(self.x+20,self.y+10,index_l,index_w)
        self.thumb=Finger(self.x+50,self.y+30,thumb_l,thumb_w)
        
    def draw(self):
        self.little.draw()
        self.ring.draw()
        self.mid.draw()
        self.index.draw()  
        self.thumb.draw()  

class RightHand:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.little=Finger(self.x+40,self.y+20,little_l,little_w)
        self.ring=Finger(self.x+20,self.y+10,ring_l,ring_w)
        self.mid=Finger(self.x,self.y,mid_l,mid_w)
        self.index=Finger(self.x-20,self.y+10,index_l,index_w)
        self.thumb=Finger(self.x-50,self.y+30,thumb_l,thumb_w)

    def draw(self):
        self.little.draw()
        self.ring.draw()
        self.mid.draw()
        self.index.draw()  
        self.thumb.draw()  
