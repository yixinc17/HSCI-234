# Player class:
# a parent class for all playerable elements: fingers and mouse-related(menu and cursor)
# a shared function is is_match(target), to see if the player matches targets
import js
p5 = js.window
# fonts
font_key = p5.loadFont('font/Monofett-Regular.ttf')

nail = ["#523818","#237bad"]
cursor_c = ["#000000","#44ba00"]
menu_img = p5.loadImage('image/rightclick.jpg')
font_c ={
    'title':'#ab4c15',
    'text':'#c8c8c8' 
         }
class Player:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y 
        self.d = 0    
    def is_match(self,target):
        self.d = p5.dist(self.x , self.y , target.x, target.y)
        if self.d < 5:
            return True
#right click mouse: menu    
class Menu(Player):
    def draw(self):
        p5.imageMode(p5.CORNER)
        p5.image(menu_img,self.x,self.y)

class Cursor(Player):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y 
        self.c = cursor_c[0]
        self.d = 0
    def draw(self):
        p5.fill(self.c)
        p5.noStroke()
        p5.push()
        p5.translate(self.x+10,self.y)  
        p5.rotate(p5.radians(-45))     
        p5.triangle(0,0,-5,10,5,10)
        p5.rect(0,10,4,10)
        p5.pop()
    def follow(self):
        self.x = p5.mouseX
        self.y = p5.mouseY
        self.draw()


class Finger(Player):
    def __init__(self,x=0,y=0,l=70,w=18):
        self.x=x
        self.y=y
        self.c=nail[0]
        self.w=w
        self.l=l
        self.d = 0
    def draw(self):
        x=self.w/4
        p5.push()
        p5.translate(self.x,self.y)
        p5.noStroke()
        p5.fill(232, 205, 172)
        p5.rect(0,0,self.w,self.l)
        #finger tip
        p5.ellipse(0,0-self.l/2,self.w,self.w)
        p5.fill(self.c)
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
    #when move fingers, related keys will appear under the fingers
    def press_key(self,key):
        p5.textAlign(p5.CENTER)
        p5.textFont(font_key) 
        p5.fill(font_c['title'])  
        p5.textSize(40)
        p5.text(key, self.x, self.y-self.l/2)

    def move(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y