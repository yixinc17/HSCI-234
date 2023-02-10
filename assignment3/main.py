import js
p5 = js.window
hair = ["#d9d7c5","#a8bda4","#a3c6d6","#c9a1a9"]
lips = ["#d4043c","#c78a6f","#5e3d2f","#1f636b","#7e6d8f","#000000","#bda5f2","#0d0dff","#dba995","#996a7e"]
lipc =0
hairc =0
def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)
def petal():
    p5.fill(10,20,255)
    p5.noStroke()
    p5.ellipse(0,0,10,2)
def center(x):
    p5.fill(100,80,200)
    p5.noStroke()
    p5.ellipse(150,150,x,x)
def flower(x):
    for i in range(x):
        p5.push()
        p5.rotate(i*p5.PI/x)
        petal()
        center(1) 
        p5.pop()
       

    
def bg(x):
    p5.background(159, 191, p5.random(200,255))  
    p5.push()
    for i in range(int(p5.width/x)):
        for j in range(int(p5.height/x)):
            p5.push()
            p5.translate(i*int(p5.width/x),j*int(p5.height/x))
            # p5.scale(1/x)
            flower(20-x)
            
            p5.pop()
          
    p5.pop()

def face():
    p5.rectMode(p5.CENTER)
    p5.fill(240, 234, 216)
    p5.noStroke()
    p5.ellipse(150,150,100,100)#face
    p5.ellipse(150,180,80,80)#chin
    p5.rect(150,200,20,150)#neck
    for i in range(2):
        p5.ellipse(100*(i+1),170,20,30)#ear
#######################################################lip with color
def lip(n):
    x=150
    y=190
    p5.fill(lips[n])
    p5.noStroke()
    #upper lip
    p5.ellipse(x-3,y,10,10)
    p5.ellipse(x+3,y,10,10)
    p5.triangle(x-5,y-5,x-5,y+4,x-18,y+5)
    p5.triangle(x+5,y-5,x+5,y+4,x+18,y+5)
    #lower lip
    p5.arc(x, y+4, 35, 18, p5.radians(0), p5.radians(-180))
####################################################hair bottom with color
def hairb(n):
    p5.fill(0)
    p5.rectMode(p5.CENTER)
    p5.rect(150, 200, 120, 150)
    p5.fill(hair[n])
    p5.rect(150, 200, 100, 150)
###############################################hair top
def hairt():
    p5.fill(0)
    p5.arc(150, 130, 120, 110, p5.radians(-210), p5.radians(40))

    
def draw():
    lipc = int(p5.map(p5.mouseY,0,300,0,10)) #map index for lip color list from 0 to 9
    hairc = int(p5.map(p5.mouseX,0,300,0,4)) #map index for hair color list from 0 to 3
#make sure index for color not exceed
    # if lipc<0:
    #     lipc = 0
    if lipc>9:
        lipc = 9
    # if hairc<0:
    #     hairc = 0
    if hairc>3:
        hairc = 3
    bg(int(p5.random(10,15)))  #random color and grids of bg
    p5.noStroke()
    p5.fill(0)
    #p5.text(str(int(p5.width/10)),10,20)
    hairb(hairc)
    face()
    hairt()
    lip(lipc)

    # #check lipc and hairc
    # p5.stroke(0)
    # p5.text("lipc = " + str(lipc), 10, 20)
    # p5.text("hairc = " + str(hairc), 10, 40)


    # useful built-in variables in p5:
    # p5.text("p5.width = " + str(p5.width), 10, 20)
    # p5.text("p5.height = " + str(p5.height), 10, 40)
    # p5.text("p5.mouseX = " + str(p5.mouseX), 10, 60)
    # p5.text("p5.mouseY = " + str(p5.mouseY), 10, 80)
    # p5.stroke(0)
    # p5.noFill()
    # x = p5.width / 2  # assign x to center of canvas horizontally 
    # y = p5.height / 2  # assign y to center of canvas vertically
    # w = p5.mouseX  # horizontal cursor position
    # h = p5.mouseY  # vertical cursor position
    # p5.ellipse(x, y, w, h)import js