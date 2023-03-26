# week1:
#     create fingers,cursor,targets class
#     AWSD to move
#week2:
#     make left hand and right hand a class by using Finger()
#     Finger.press_key(): when press 'AWSD', there will be a key under the finger
#     count down number 5 sec
#     reorganize repeative parameters
#     classify three program_state, and put related UI into each state.

#????? line326 # l_index_target.random(100,500)
# freeze with random position
#????? line 328-336 freeze with mouseclick to create new cursor pattern 
# maybe use list to store wrong mouseclick position 

#instruction:
#'ESC' to return home
# 'SPACE' to start
# Game rule: use 'AWSD' to control left hand, and mouse to control right hand. Every 5 second there will be a random cursor-target and three finger-targets. Try to match targets in 5 second and then you win.

import js
p5 = js.window
nail = ["#523818","#237bad"]
c=nail[0]
bg = {
    'r':45, 
    'g':156, 
    'b':150
}
timer = 0
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
# 3 main status of the game
program_state = 'INTRO'
# program_state = 'PLAY'
# program_state = 'END'
win = False


# fonts
font_key = p5.loadFont('font/Monofett-Regular.ttf')
font_num = p5.loadFont('font/digital-7.ttf')
class Timer:
    def __init__(self,x=0,y=0,t=5):
        self.x=x
        self.y=y
        self.t = t
        self.count = t
        self.timer =0
    def update(self):
        p5.textFont(font_num) 
        p5.fill(46)  
        p5.textSize(40)
        self.count = self.t-int((p5.millis()-self.timer)/1000) 
        if self.count<=0:
            self.count = self.t
            self.timer = p5.millis()
        p5.text(self.count, self.x,self.y)
        

            

        

class Cursor:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def draw(self,x,y):
        self.x = x
        self.y = y
        p5.fill(0)
        p5.noStroke()
        p5.push()
        p5.translate(self.x+10,self.y)  
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
        self.x = x
        self.y = y
        p5.noFill()
        p5.stroke(c)
        p5.strokeWeight(2)
        p5.push()
        p5.translate(self.x+10,self.y)  
        p5.rotate(p5.radians(-45))     
        p5.triangle(0,0,-5,10,5,10)
        p5.rect(0,10,4,10)
        p5.pop()
    
class Finger:
    def __init__(self,x=0,y=0,l=70,w=18):
        self.x=x
        self.y=y
        self.direction=0
        self.c=nail[0]
        self.w=w
        self.l=l
    def draw(self,c):
        x=self.w/4
        p5.push()
        p5.translate(self.x,self.y)
        p5.rotate(self.direction)  
        p5.noStroke()
        p5.fill(232, 205, 172)
        p5.rect(0,0,self.w,self.l)
        #finger tip
        p5.ellipse(0,0-self.l/2,self.w,self.w)
        p5.fill(c)
        p5.rect(0,0-self.l/2,self.w/3*2,13)
        p5.ellipse(0,0-self.l/2-5,self.w/3*2,10)
        #finger wrinkles
        p5.stroke(117, 110, 99)
        p5.strokeWeight(2)
        p5.line(0-x,0-self.l/3+3,0+x,0-self.l/3+3)
        p5.line(0-x,0-self.l/3,0+x,0-self.l/3)
        p5.line(0-x,0,0+x,0)
        p5.line(-2-x,0+3,2+x,0+3)
        p5.line(0-x,0+6,0+x,0+6)
        p5.pop()



    def press_key(self,key):
        p5.textAlign(p5.CENTER)
        p5.textFont(font_key) 
        p5.fill(171, 76, 21)  
        p5.textSize(40)
        p5.text(key, self.x, self.y-self.l/2)

    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y



class FingerTarget:
    def __init__(self,x=0,y=0,l=70,w=18):
        self.x=x
        self.y=y
        self.direction=0
        self.c=170
        self.w=18
        self.l=70
    def draw(self,c):
        x=self.w/4
        p5.strokeWeight(2)
        p5.push()
        p5.translate(self.x,self.y)
        p5.rotate(self.direction)  
        p5.stroke(c)
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
    def random(self,a=100,b=500):
        global timer
        if(p5.millis()>timer+5000):
            self.x = p5.random(a,b)
            self.y = p5.random(a,b)
            timer=p5.millis()
        self.draw(self.c)

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
        self.little.draw(c)
        self.ring.draw(c)
        self.mid.draw(c)
        self.index.draw(c)  
        self.thumb.draw(c)  

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
        self.little.draw(c)
        self.ring.draw(c)
        self.mid.draw(c)
        self.index.draw(c)  
        self.thumb.draw(c)  




intro_lhand = LeftHand(200,400)
intro_rhand = RightHand(400,400)

timer = Timer(580,50,5)
cursor = Cursor(150,150)
cursor_target = CursorTarget(0,0)
l_mid_target=FingerTarget(0,0,mid_l,mid_w)
l_ring_target=FingerTarget(0,0,ring_l,ring_w)
l_index_target=FingerTarget(0,0,index_l,index_w)

lhand = LeftHand(100,500)
rhand = RightHand(500,500)
# left_pos_y=500
# left_pos_x=100
# right_pos_y=500
# right_pos_x=500
# #left hand
# l_little=Finger(left_pos_x-40,left_pos_y+20)
# l_ring=Finger(left_pos_x-20,left_pos_y+10)
# l_mid=Finger(left_pos_x,left_pos_y)
# l_index=Finger(left_pos_x+20,left_pos_y+10)
# l_thumb=Finger(left_pos_x+50,left_pos_y+30)
# #right hand
# r_little=Finger(right_pos_x+40,right_pos_y+20)
# r_ring=Finger(right_pos_x+20,right_pos_y+10)
# r_mid=Finger(right_pos_x,right_pos_y)
# r_index=Finger(right_pos_x-20,right_pos_y+10)
# r_thumb=Finger(right_pos_x-50,right_pos_y+30)


def setup():
    p5.rectMode(p5.CENTER)
    p5.createCanvas(600, 600) 
    print('finished setup') 
 
   
def draw():
    global win, program_state
    
    p5.background(bg['r'], bg['g'], bg['b'])   
 
    #intro   
    if program_state == 'INTRO':
        p5.textFont(font_key) 
        p5.fill(171, 76, 21)  
        p5.textAlign(p5.CENTER)
        p5.textSize(50)
        p5.text('Mind Your Own Business', 300, 150)
        intro_lhand.draw()
        intro_rhand.draw()
        cursor.draw(400,180)
        p5.textSize(30)
        p5.fill(200)
        p5.text('Click SPACE to start', 300, 520)
        p5.text('Click ESC to return home', 300, 550)
        p5.fill(200)
        p5.textAlign(p5.LEFT)
        p5.textSize(20)
        p5.text('Press', 80, 300)
        p5.text('A W S D', 80, 320)
        p5.text('to move', 80, 340)
        p5.text('left hand', 80, 360)
        p5.textAlign(p5.RIGHT)
        p5.text('Move and click', 520, 220)
        p5.text('mouse', 520, 240)
        p5.text('to move and confirm', 520, 260)
        p5.text('the cursor', 520, 280)

    # play
    elif program_state =='PLAY':
        # cursor_target.draw(p5.random(100,500),p5.random(100,500),cursor_target.c)
        # l_mid_target.draw(l_mid_target.c)
        # l_ring_target.draw(l_ring_target.c)
        # l_index_target.draw(l_index_target.c)
        cursor.draw(p5.mouseX,p5.mouseY)
        #AWSD to move left fingers
        if p5.keyIsPressed==True:
            if p5.key == "A" or p5.key =="a":
                lhand.ring.x-=1
                lhand.ring.press_key('A')
                if lhand.ring.x<=-lhand.ring.w/2:
                    lhand.ring.x= p5.width+lhand.ring.w/2
            if p5.key == "D" or p5.key =="d":
                lhand.index.x+=1
                lhand.index.press_key('D')
                if lhand.index.x>=p5.width+lhand.index.w/2:
                    lhand.index.x= -lhand.index.w/2
            if p5.key == "W" or p5.key =="w":
                lhand.mid.y-=1
                lhand.mid.press_key('W')
                if lhand.mid.y<=-lhand.mid.l/2:
                    lhand.mid.y= p5.height+lhand.mid.l/2
            if p5.key == "S" or p5.key =="s":
                lhand.mid.y+=1
                lhand.mid.press_key('S')
                if lhand.mid.y>=p5.height+lhand.mid.y/2:
                    lhand.mid.y= -lhand.mid.w/2
        lhand.draw()
        rhand.draw()
        if win:
            program_state = 'END'
        else:
            timer.update()
            # l_index_target.random(100,500)
            
        if (p5.mouseIsPressed == True):
            if (p5.mouseButton == p5.LEFT):
                new = Cursor(x=p5.mouseX,y=p5.mouseY)
                global cursor_list
                cursor_list.append(new)
        
        for i in range(len(cursor_list)):
            new_cursor = cursor_list[i]
            new_cursor.draw()
        
    # end
    elif program_state =='END':  
        p5.text('ENDING', 20, 40)
    



    
    













# #draw hands   
#     l_little.draw(50,14,c)
#     l_ring.draw(80,16,c)
#     lhand.mid.draw(100,18,c)
#     l_index.draw(70,18,c)  
#     l_thumb.draw(30,20,c)      
#     r_little.draw(50,14,c)
#     r_ring.draw(80,16,c)
#     r_mid.draw(100,18,c)
#     r_index.draw(70,18,c)  
#     r_thumb.draw(30,20,c) 
#arrow button to change direction and position of player2




def keyPressed(event):
    pass

def keyReleased(event):
    global program_state
    if program_state == 'INTRO' and p5.key ==" ":
        program_state = 'PLAY'
        print('change program_state to ' + program_state)
    elif (program_state == 'PLAY' or program_state == 'END') and p5.keyCode == p5.ESCAPE:
        program_state = 'INTRO'
        print('change program_state to ' + program_state)

    

def mousePressed(event):
    pass
def mouseReleased(event):
    pass
        