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
class Player:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.direction=0
    def draw(self,l):
        global c
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




player1=Player(10,150)
player2=Player(150,150)
def setup():
    p5.rectMode(p5.CENTER)
    p5.createCanvas(600, 600) 
    print('finished setup') 
 
   
def draw():
    global d, direction
    p5.background(45, 156, 150)            

    d=p5.dist(player1.x,player1.y,player2.x,player2.y)
    # print(d)
    if(d<100):
        p5.noStroke()
        p5.fill(255,0,0)
        p5.ellipse(150,150,50,50)
        c=nail[1]
    else:
        c=nail[0]#?????????????????????????????????????????????QUESTION:not sure why the color doesnt change
       
    player1.draw(100)
    player2.draw(80)   
    player1.automove_random(0,300)      


#arrow button to change direction and position of player2
def keyPressed(event):
    global speed, direction
    if(p5.keyCode == p5.RIGHT_ARROW):
        n=speed
        player2.direction=p5.PI/2
        player2.move(n, 0)        
    elif(p5.keyCode == p5.LEFT_ARROW):
        n=-speed
        player2.direction=-p5.PI/2
        player2.move(n, 0)
    elif(p5.keyCode == p5.UP_ARROW):
        n=-speed
        player2.direction=0
        player2.move(0, n)    
    elif(p5.keyCode == p5.DOWN_ARROW):
        n=speed
        player2.direction=p5.PI
        player2.move(0, n)    


def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
