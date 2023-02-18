import js
p5 = js.window

ring_x = 100
mid_y = 150
index_x = 200
# def preload():
#     img = p5.loadImage('image/ring.png')

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)
    # p5.image(img,ring_x,150)



    
def draw():
    global ring_x, index_x, mid_y
    if (p5.keyIsPressed):
        p5.fill(0,255,200)
        if (p5.key == 'a') or (p5.key == 'A'):  
            ring_x = ring_x - 1
        elif (p5.key == 's') or (p5.key == 'S'):
            mid_y = mid_y + 1
        elif (p5.key == 'w') or (p5.key == 'W'):
            mid_y = mid_y - 1
        elif (p5.key == 'd') or (p5.key == 'D'):
            index_x = index_x + 1
    else: 
        p5.fill(0)  # white    
    p5.rect(index_x,150,10,200)
    p5.rect(ring_x,150,10,180)
    p5.rect(150,mid_y,10,220)