import js
p5 = js.window
#1. Create a global variable random_size that is a random integer value between 25 - 125. 
random_size = int(p5.random(25,125)) 
alpha = 1
random_size1 = int(p5.random(25,125)) 
random_size2 = int(p5.random(25,125)) 
random_size3 = int(p5.random(25,125)) 
startpointx=0
startpointy=0
endpointx=0
endpointy=0
color = ["#d9d7c5","#a8bda4","#a3c6d6","#c9a1a9"]

#11. [Extra-credit] Write moveto(x, y) and lineto(x, y) functions to draw lines of a square.
def moveto(x1, y1):
    global startpointx, startpointy
    startpointx=x1
    startpointy=y1
    return startpointx, startpointy
def lineto(x2, y2):
    global startpointx, startpointy, endpointx, endpointy
    endpointx=x2
    endpointy=y2
    p5.stroke(0,0,255)
    p5.strokeWeight(1)
    p5.line(startpointx, startpointy, endpointx, endpointy)

    
#use moveto(x1, y1) and lineto(x2, y2) to draw
def new_random_square():
    moveto(150,150)
    lineto(150,200)
    moveto(150,200)
    lineto(200,200)
    moveto(200,200)
    lineto(200,150)
    moveto(200,150)
    lineto(150,150)







#3. Write a function definition random_square(size) to draw a random size square.
def random_square(size):
    p5.strokeWeight(2)
    p5.line(0-size/2,0-size/2,0+size/2,0-size/2)
    p5.line(0-size/2,0-size/2,0-size/2,0+size/2)
    p5.line(0-size/2,0+size/2,0+size/2,0+size/2)
    p5.line(0+size/2,0+size/2,0+size/2,0-size/2)



#5. Write another function definition random_square_at(x, y, size) to draw a square.
def random_square_at(x, y, size):
    p5.strokeWeight(2)
    p5.push()
    p5.translate(x,y)
    random_square(size)
    p5.pop()





# #10. Write a function definition inside_square that returns True if the cursor is inside a square.
def inside_square(x,y):    
    if(x>p5.width-10-random_size2/2) and (x<p5.width-10+random_size2) and (y>10-random_size2/2) and (y<10+random_size2/2):        
        p5.stroke(color[2])
        return True
    else:
        p5.stroke(color[0])
        return False
    random_square_at(p5.width-10, 10, random_size2)   
        
#multiple squares
def random_square_loop(x, y, size):
    for i in range(4):
        moveto(x-size/2,y-size/2)
        lineto(x-size/2,y+size/2)
        moveto(x-size/2,y+size/2)
        lineto(x+size/2,y+size/2)
        moveto(x+size/2,y+size/2)
        lineto(x+size/2,y-size/2)
        moveto(x+size/2,y-size/2)
        lineto(x-size/2,y-size/2)
        size-=4


def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    print('finished setup')



def draw():
    global random_size, random_size1,random_size2,random_size3, alpha

    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.text(random_size, 10, 30)
    p5.stroke(0)
    p5.strokeWeight(2)  # set stroke thickness


    # #2. Draw a square of random size using line functions only.
    # p5.line(p5.width/2-random_size/2,p5.height/2-random_size/2,p5.width/2+random_size/2,p5.height/2-random_size/2)
    # p5.line(p5.width/2-random_size/2,p5.height/2-random_size/2,p5.width/2-random_size/2,p5.height/2+random_size/2)
    # p5.line(p5.width/2-random_size/2,p5.height/2+random_size/2,p5.width/2+random_size/2,p5.height/2+random_size/2)
    # p5.line(p5.width/2+random_size/2,p5.height/2+random_size/2,p5.width/2+random_size/2,p5.height/2-random_size/2)
    
    # #4. Use transformation functions to move the square by x and y coordinates.
    # p5.push()
    # p5.translate(50,50)
    # random_square(random_size)
    # p5.pop()

    ##5. Write another function definition random_square_at(x, y, size) to draw a square.
    #random_square_at(20, 150, 10)

    #6. Draw 4 random squares, one in each corner of the canvas.
    p5.stroke(color[1])
    random_square_at(p5.width-10, p5.height-10, random_size1)

    
    #7. Make one of the squares visible only when the mouse is pressed.
    if (p5.mouseIsPressed == True):
        p5.stroke(color[3])
        random_square_at(10,p5.height-10, random_size3)
    
    #8. Animate the transparency of another square.
    p5.stroke(255, 25, 140,alpha)    
    random_square_at(10, 10, random_size)    
    if(alpha>255):
        alpha = 1
    else:
        alpha+=1

    #9. Make another square change color when the cursor is inside of it.
    if(inside_square(p5.mouseX,p5.mouseY)==True):
        p5.stroke(color[2])
    else:
        p5.stroke(color[0])
    random_square_at(p5.width-10, 10, random_size2)   
         
    # #9. Make another square change color when the cursor is inside of it.
    inside_square(p5.mouseX,p5.mouseY)


    new_random_square()
    random_square_loop(150,150,40)




