import js
import random
p5 = js.window
x = 150
y = 150
d = 30
index0 = 0
index1 = 0
index2 = 0
randCol = ""
colorls = ["#D0B2CD","#F9C3D0","#7DA2CD","#C0B061","#F5EAB2","#C2DAF9","#C64F8E","#913939"]

def setup():
    p5.createCanvas(300, 300)   

def draw():
    p5.background(204,102,0,255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)

    for i in range(20):
        x =  i*25
        for j in range(20):
            y =  j*25
            index0 = i % 3
            index2 = (i+2) % 8
            index1 = (i+1) % 8
            
            p5.push()
            
            # body************************************
            p5.fill("#B7DAB0")
            p5.stroke(255)
            p5.ellipse(x,y,d,d)
                        
            p5.push()
            # one ear*************************************
            p5.fill(colorls[index1])
            p5.noStroke()
            p5.translate(170,-250)
            
            p5.rotate(p5.PI/4)
            p5.ellipse(x,y,15,8)        
            p5.pop()          
            # one ear*************************************
            p5.push()            
            p5.fill(colorls[index1])
            p5.noStroke()
            p5.translate(200,-250)
            
            p5.rotate(p5.PI/4)
            p5.ellipse(x,y,15,8)
            p5.pop()
          
            p5.pop()