# week1:
#     create fingers,cursor,targets class
#     AWSD to move
import js
p5 = js.window
nail = ["#523818","#237bad"]
c=nail[0]
d=0
speed=10
timer=0
direction=0
class Cursor:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def draw(self,x,y):
        p5.fill(0)
        p5.noStroke()
        p5.push()
        p5.translate(x+10,y)  
        p5.rotate(p5.radians(-45))     
        p5.triangle(0,0,-5,10,5,10)
        p5.rect(0,10,4,10)
        p5.pop()
class CursorTarget:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.c=170
    def draw(self,x,y,c):
        p5.noFill()
        p5.stroke(c)
        p5.strokeWeight(2)
        p5.push()
        p5.translate(x+10,y)  
        p5.rotate(p5.radians(-45))     
        p5.triangle(0,0,-5,10,5,10)
        p5.rect(0,10,4,10)
        p5.pop()

class Finger:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.direction=0
        self.c=nail[0]
        self.w=0
        self.l=0
    def draw(self,l,w,c):
        x=w/4
        self.w=w
        self.l=l
        p5.push()
        p5.translate(self.x,self.y)
        p5.rotate(self.direction)  
        p5.noStroke()
        p5.fill(232, 205, 172)
        p5.rect(0,0,w,l)
        #finger tip
        p5.ellipse(0,0-l/2,w,w)
        p5.fill(c)
        p5.rect(0,0-l/2,w/3*2,13)
        p5.ellipse(0,0-l/2-5,w/3*2,10)
        #finger wrinkles
        p5.stroke(117, 110, 99)
        p5.strokeWeight(2)
        p5.line(0-x,0-l/3+3,0+x,0-l/3+3)
        p5.line(0-x,0-l/3,0+x,0-l/3)
        p5.line(0-x,0,0+x,0)
        p5.line(-2-x,0+3,2+x,0+3)
        p5.line(0-x,0+6,0+x,0+6)
        p5.pop()



    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y


    def automove_random(self,a=0,b=300):
        global timer
        if(p5.millis()>timer+500):
            self.x = int(p5.random(a,b))
            self.y = int(p5.random(a,b))
            timer=p5.millis()

class FingerTarget:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.direction=0
        self.c=170
        self.w=0
        self.l=0
    def draw(self,l,w,c):
        x=w/4
        self.w=w
        self.l=l
        p5.strokeWeight(2)
        p5.push()
        p5.translate(self.x,self.y)
        p5.rotate(self.direction)  
        p5.stroke(c)
        p5.noFill()
        p5.rect(0,0,w,l)
        #finger tip
        p5.ellipse(0,0-l/2,w,w)
        p5.rect(0,0-l/2,w/3*2,13)
        p5.ellipse(0,0-l/2-5,w/3*2,10)
        #finger wrinkles       
        p5.line(0-x,0-l/3+3,0+x,0-l/3+3)
        p5.line(0-x,0-l/3,0+x,0-l/3)
        p5.line(0-x,0,0+x,0)
        p5.line(-2-x,0+3,2+x,0+3)
        p5.line(0-x,0+6,0+x,0+6)
        p5.pop()
left_pos_y=500
left_pos_x=100
right_pos_y=500
right_pos_x=500
cursor = Cursor(150,150)
cursor_target = CursorTarget(200,200)
#left hand
l_little=Finger(left_pos_x-40,left_pos_y+20)
l_ring=Finger(left_pos_x-20,left_pos_y+10)
l_mid=Finger(left_pos_x,left_pos_y)
l_index=Finger(left_pos_x+20,left_pos_y+10)
l_thumb=Finger(left_pos_x+50,left_pos_y+30)
#right hand
r_little=Finger(right_pos_x+40,right_pos_y+20)
r_ring=Finger(right_pos_x+20,right_pos_y+10)
r_mid=Finger(right_pos_x,right_pos_y)
r_index=Finger(right_pos_x-20,right_pos_y+10)
r_thumb=Finger(right_pos_x-50,right_pos_y+30)


l_mid_target=FingerTarget(100,100)

def setup():
    p5.rectMode(p5.CENTER)
    p5.createCanvas(600, 600) 
    print('finished setup') 
 
   
def draw():
    global d, direction
    p5.background(45, 156, 150)     

    cursor_target.draw(200,200,cursor_target.c)
    l_mid_target.draw(100,18,l_mid_target.c)
#draw hands   
    l_little.draw(50,14,c)
    l_ring.draw(80,16,c)
    l_mid.draw(100,18,c)
    l_index.draw(70,18,c)  
    l_thumb.draw(30,20,c)      
    r_little.draw(50,14,c)
    r_ring.draw(80,16,c)
    r_mid.draw(100,18,c)
    r_index.draw(70,18,c)  
    r_thumb.draw(30,20,c) 

    cursor.draw(p5.mouseX,p5.mouseY)

    

#AWSD to move left fingers
    if p5.keyIsPressed==True:
        if p5.key == "A" or p5.key =="a":
            l_ring.x-=1
            if l_ring.x<=-l_ring.w/2:
                l_ring.x= p5.width+l_ring.w/2
        if p5.key == "D" or p5.key =="d":
            l_index.x+=1
            if l_index.x>=p5.width+l_index.w/2:
                l_index.x= -l_index.w/2
        if p5.key == "W" or p5.key =="w":
            l_mid.y-=1
            if l_mid.y<=-l_mid.l/2:
                l_mid.y= p5.height+l_mid.l/2
        if p5.key == "S" or p5.key =="s":
            l_mid.y+=1
            if l_mid.y>=p5.height+l_mid.y/2:
                l_mid.y= -l_mid.w/2
 

#arrow button to change direction and position of player2
def keyPressed(event):
    pass


def keyReleased(event):
    pass

def mousePressed(event):
    pass
def mouseReleased(event):
    pass