#player1 randomly move per 0.5 sec
#arrow to control player2, try to avoid colliding
#when colliding, a red ball  appears
#QUESTION:line79,the color of nail wont change as they collide
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
        p5.translate(x-100,y)  
        p5.rotate(p5.radians(-45))     
        p5.triangle(150,150,145,160,155,160)
        p5.rect(150,160,4,10)
        p5.pop()
class Finger:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.direction=0
        self.c=nail[0]
    def draw(self,l,c):
        m=l
        p5.push()
        p5.translate(self.x,self.y)
        p5.rotate(self.direction)  
        p5.noStroke()
        p5.fill(232, 205, 172)
        p5.rect(0,0,20,m)
        #finger tip
        p5.ellipse(0,0-m/2,20,20)
        p5.fill(c)
        p5.rect(0,0-m/2,15,10)
        p5.ellipse(0,0-m/2-5,15,10)
        #finger wrinkles
        p5.stroke(117, 110, 99)
        p5.strokeWeight(2)
        p5.line(0-5,0-m/3+3,0+5,0-m/3+3)
        p5.line(0-5,0-m/3,0+5,0-m/3)
        p5.line(0-5,0,0+5,0)
        p5.line(0-7,0+3,0+7,0+3)
        p5.line(0-5,0+6,0+5,0+6)
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



cursor = Cursor(150,150)
mid_l=Finger(10,150)
index_l=Finger(150,150)
def setup():
    p5.rectMode(p5.CENTER)
    p5.createCanvas(600, 600) 
    print('finished setup') 
 
   
def draw():
    global d, direction
    p5.background(45, 156, 150)            

   
    mid_l.draw(100,c)
    index_l.draw(80,c)   
    mid_l.automove_random(0,300)   
    cursor.draw(p5.mouseX,p5.mouseY)


#arrow button to change direction and position of player2
def keyPressed(event):
    global speed, direction
    if(p5.keyCode == p5.RIGHT_ARROW):
        n=speed
        index_l.direction=p5.PI/2
        index_l.move(n, 0)        
    elif(p5.keyCode == p5.LEFT_ARROW):
        n=-speed
        index_l.direction=-p5.PI/2
        index_l.move(n, 0)
    elif(p5.keyCode == p5.UP_ARROW):
        n=-speed
        index_l.direction=0
        index_l.move(0, n)    
    elif(p5.keyCode == p5.DOWN_ARROW):
        n=speed
        index_l.direction=p5.PI
        index_l.move(0, n)    


def keyReleased(event):
    pass

def mousePressed(event):
    pass
def mouseReleased(event):
    pass