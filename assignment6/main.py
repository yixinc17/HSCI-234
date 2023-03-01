import js
p5 = js.window
program_state = 'state1'
program_timer = 0
size = 100
def setup():
    p5.createCanvas(300, 300)  
    print('finished setup() at ' + str(p5.millis()) + " ms")

def draw():
    p5.rectMode(p5.CENTER)
    global program_timer, program_state,size
    p5.background(204, 195, 180) 
          
       
    # compare current running time to saved timer plus interval:
    if(p5.millis() > program_timer + 3000):  
        if(program_state == 'state1'):
            program_state = 'state2'
        elif(program_state == 'state2'):
            program_state = 'state1'
        program_timer = p5.millis()  # update timer
        print(program_state)
        if(program_state == 'state1'):
            size = 250
        elif(program_state == 'state2'):
            size = 50
        if(program_state == 'state3'):
            p5.fill(0, 124, 240)
            size = 100
        else:
            p5.fill(255, 0, 140)
        p5.noStroke()        
        p5.rect(150,150,size,size)



def keyPressed(event):
    global program_state
    if(p5.key=='1'):
        print('1')
        program_state = 'state1'
    elif(p5.key=='2'):
        print('2')
        program_state = 'state2'
    elif(p5.key=='3'):
        print('3')
        program_state = 'state3'



def keyReleased(event):
    pass

def mousePressed(event):
    global program_state
    if(program_state != 'state3'):
        program_state = 'state3'    
    print('change program_state to ' + program_state)



def mouseReleased(event):
    global program_state,program_timer
    if(program_state == 'state3'):
        program_state = 'state1' 
        program_timer = p5.millis()
    print('change program_state back to ' + program_state)








