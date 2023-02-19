import js
p5 = js.window
###########This is a game that players can interact with directional keys "aswd" and mouse. You can see the things you've ignored when operating. That's your finger!
#positions of fingers
ring_x = 50
mid_y = 150
index_x = 100
normal_x = 75
normal_y = 150
#length of fingers
l_ring = 90
l_mid = 100
l_index = 70
#colors of nails
nail = ["#523818","#237bad"]
nail_color = nail[0]
c_l_index = nail[0]
c_l_mid = nail[0]
c_l_ring = nail[0]
c_r_index = nail[0]
c_r_mid = nail[0]

#arrow with variables: positions.
def arrow(x,y):
    p5.fill(0)
    p5.noStroke()
    p5.push()
    p5.translate(x-p5.width/2,y)
    p5.rotate(p5.radians(-45))
    p5.triangle(150,150,145,160,155,160)
    p5.rect(150,160,4,10)
    p5.pop()
#finger with variables: positionx and y, length, color
def finger(x,y,m,c):
    p5.noStroke()
    p5.fill(232, 205, 172)
    p5.rect(x,y,20,m)
    #finger tip
    p5.ellipse(x,y-m/2,20,20)
    p5.fill(c)
    p5.rect(x,y-m/2,15,10)
    p5.ellipse(x,y-m/2-5,15,10)
    #finger wrinkles
    p5.stroke(117, 110, 99)
    p5.strokeWeight(2)
    p5.line(x-5,y-m/3+3,x+5,y-m/3+3)
    p5.line(x-5,y-m/3,x+5,y-m/3)
    p5.line(x-5,y,x+5,y)
    p5.line(x-7,y+3,x+7,y+3)
    p5.line(x-5,y+6,x+5,y+6)
    
def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

def draw():
    
    global ring_x, index_x, mid_y, normal_x, normal_y, nail_color,c_l_index,c_l_mid,c_l_ring,c_r_index,c_r_mid
    p5.background(45, 156, 150)    
    
    #hint text of key
    p5.textFont('Helvetica', 300)
    p5.noStroke()
    p5.fill(173, 117, 49)
    p5.text(str(p5.key), 10, 150)
    
    ############################## Left hand with keyboard

    if (p5.keyIsPressed):
        #p5.text("pressed",10,10)
        nail_color = nail[0]
        if (p5.key == 'a') or (p5.key == 'A'):  
            ring_x = ring_x - 1
            c_l_ring = nail[1]
        elif (p5.key == 's') or (p5.key == 'S'):
            mid_y = mid_y + 1
            c_l_mid = nail[1]
        elif (p5.key == 'w') or (p5.key == 'W'):
            mid_y = mid_y - 1
            c_l_mid = nail[1]
        elif (p5.key == 'd') or (p5.key == 'D'):
            index_x = index_x + 1
            c_l_index = nail[1]
    else: 
        nail_color = nail[0]
        c_l_index = nail[0]
        c_l_mid = nail[0]
        c_l_ring = nail[0]
        #p5.text("not pressed",10,10)
    finger(ring_x,normal_y,l_ring,c_l_ring)
    finger(index_x,normal_y,l_index,c_l_index)
    finger(normal_x,mid_y,l_mid,c_l_mid)

    ####################### Right hand with mouse
    if (p5.mouseIsPressed == True):
        p5.fill(186, 155, 180)
        p5.noStroke()
        p5.textSize(200)
        # p5.mouseButton is equal to p5.LEFT with 'left' (or one-figer) click:
        if (p5.mouseButton == p5.LEFT):
            c_r_index = nail[1]
            p5.text("Left",10,280)
        # p5.mouseButton is equal to p5.RIGHT with 'right' (or two-finger) click:
        elif (p5.mouseButton == p5.RIGHT):
            c_r_mid = nail[1]
            p5.text("Right",10,280)
    else:
        c_r_index = nail[0]
        c_r_mid = nail[0]
        p5.text(" ",10,280)
        
    arrow(p5.mouseX,p5.mouseY)
    finger(200,200,l_index,c_r_index)
    finger(230,200,l_mid,c_r_mid)
