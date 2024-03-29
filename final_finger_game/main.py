# week1:Elements and Class
#     create fingers,cursor,targets class
#     AWSD to move


#week2: Game structure and Class optmized
#     make left hand and right hand a class by using Finger()
#     Finger.press_key(): when press 'AWSD', there will be a key under the finger
#     count down number 5 sec
#     reorganize repeative parameters
#     classify three program_state, and put related UI into each state.
        # all solved
            #????? # l_index_target.random(100,500)
            # freeze with random position
            #????? line 328-336 freeze with mouseclick to create new cursor pattern 
            # maybe use list to store wrong mouseclick position 


#week3: Child Class; Game test; win state; player tests
    # Class optimized with Child Class, and independent py files.
    # all function done without win state(including random targets every 5 sec, move fingers, mouse click to instantiate menu and cursor) 
    # first game test: 5 sec count down and specific position match is so difficult, so the timer will adjust to longer time, and instead of matching positions, use distance range.
    #  if cursor matches the target, it will turn green, but if others dont match their targets in 10 sec, the cursor will reset to black
    # oh noooo 10sec is so hard too!!! timer = 20s, margins of error(d to target) < 5
    # update ending context related to play rounds
    # upadate sound by import p5.sound lib in imdex.html:<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/addons/p5.sound.min.js"></script>
    # mouse and key sounds
    # create a dictionary for font color set
    # timer color change
    # secret button for me to cheat on time

    # player test feedback:
        # instruction not readable: what is ASWD? what's the rules?
        # difficult to match targets, especially ring and index fingers， change timer_limit to 15sec

#week4: documentation and user experience check

#instruction:
#'ESC' to return home
# 'SPACE' to start
# Game rule: use 'AWSD' to control left hand, and mouse to control right hand. Every 5 second there will be a random cursor-target and three finger-targets. Try to match targets in 5 second and then you win.
import js
p5 = js.window
from player import *
from timer import *
from hand import *
from target import *

font_c ={
    'title':'#ab4c15',
    'text':'#c8c8c8' ,
    'text1':'#523818'
         }
nail = ["#523818","#237bad"]
cursor_c = ["#000000","#44ba00"]
bg = {
    'r':45, 
    'g':156, 
    'b':150
}
timer_limit = 15

# 3 main status of the game
program_state = 'INTRO'
# program_state = 'PLAY'
# program_state = 'END'
win = False
cursor_match = False
mid_match = False
ring_match = False
index_match = False
cursor_list = []
menu_list = []

#audio
click_sound = None
release_sound = None
keydown_sound = None
keyup_sound = None


# fonts
font_key = p5.loadFont('font/Monofett-Regular.ttf')
font_num = p5.loadFont('font/digital-7.ttf')

#intro elements
intro_lhand = LeftHand(200,400)
intro_rhand = RightHand(400,400)
intro_cursor=Cursor(400,180)

intro_lhand.index.c = nail[1] 
intro_lhand.mid.c = nail[1] 
intro_lhand.ring.c = nail[1] 
intro_rhand.index.c = nail[1] 
intro_rhand.mid.c = nail[1] 
#play elements
cursor = Cursor(0,0)
cursor_target = CursorTarget(p5.random(100,500),p5.random(100,500))
l_mid_target=FingerTarget(100,p5.random(100,500),mid_l,mid_w)
l_ring_target=FingerTarget(p5.random(100,500),510,ring_l,ring_w)
l_index_target=FingerTarget(p5.random(100,500),510,index_l,index_w)
lhand = LeftHand(100,500)
rhand = RightHand(500,500)

timer = Timer(580,50,timer_limit,targets=[cursor_target, l_mid_target, l_ring_target, l_index_target])



def setup():
    global keydown_sound, keyup_sound, click_sound, release_sound
    p5.rectMode(p5.CENTER)
    p5.createCanvas(600, 600) 
    print('finished setup') 

    keydown_sound = p5.loadSound('sound/keydown.mp3')
    keyup_sound = p5.loadSound('sound/keyup.mp3')
    click_sound = p5.loadSound('sound/click.mp3')
    release_sound = p5.loadSound('sound/release.mp3')
   
def draw():
    global win, program_state, cursor_list, menu_list, timer
    global cursor_match, mid_match, ring_match, index_match 
    
    
    p5.background(bg['r'], bg['g'], bg['b'])   
    
    #intro   
    if program_state == 'INTRO':
        timer.round = 1
        p5.textFont(font_key) 
        p5.fill(font_c['text1']) 
        p5.textAlign(p5.CENTER)
        p5.textSize(30)
        p5.text('Every finger has its own job', 300, 80)
        p5.textSize(50)
        p5.fill(font_c['title']) 
        p5.text('Mind Your Own Business', 300, 150)
        intro_lhand.draw()
        intro_rhand.draw()
        intro_cursor.draw()
        p5.textAlign(p5.LEFT)
        p5.fill(font_c['text1'])
        p5.textSize(20)
        p5.text('Press', 80, 285)
        p5.textSize(30)
        p5.text('A W S D', 80, 310)
        p5.textSize(20)
        p5.text('to move', 80, 330)
        p5.text('left hand', 80, 350)
        p5.textAlign(p5.RIGHT)
        p5.text('Move and click', 520, 220)
        p5.text('mouse', 520, 240)
        p5.text('to move and confirm', 520, 260)
        p5.text('the cursor', 520, 280)
        p5.textAlign(p5.CENTER)
        p5.textSize(20)
        p5.text('Try to move to targets in time!', 300, 490)
        p5.textSize(30)
        p5.fill(font_c['text'])
        p5.text('Click SPACE to start', 300, 520)
        p5.text('Click ESC to return home', 300, 550)
        

    # play
    elif program_state =='PLAY':
        # draw 4 targets
        cursor_target.draw()
        l_mid_target.draw()
        l_ring_target.draw()
        l_index_target.draw()
        # draw player cursor move with mouse
        cursor.follow()

        # draw error cursor and menu controlled by mouse: ususally when you click right button, menu appears, and click left button, menu disappears.
        for i in range(len(menu_list)):
            newmenu = menu_list[i]
            newmenu.draw()
        for j in range(len(cursor_list)):
            wrong_cursor = cursor_list[j]
            wrong_cursor.draw()
        
   

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
                if lhand.mid.y>=p5.height+lhand.mid.l/2:
                    lhand.mid.y= -lhand.mid.l/2
        
        # if fingers matches targets, their nails will change color
        if lhand.ring.is_match(l_ring_target):
            ring_match = True
            lhand.ring.c = nail[1]
        else:
            ring_match = False
            lhand.ring.c = nail[0]
        if lhand.mid.is_match(l_mid_target):
            mid_match = True
            lhand.mid.c = nail[1]
        else:
            mid_match = False
            lhand.mid.c = nail[0]
        if lhand.index.is_match(l_index_target):
            index_match = True
            lhand.index.c = nail[1]
        else:
            index_match = False
            lhand.index.c = nail[0]

        # if cursor matches the target, it will change to green
        if cursor_match:
            cursor.c = cursor_c[1]
        else:
            cursor.c = cursor_c[0] 


        lhand.draw()
        rhand.draw()
        timer.update()
        
        # when time up and not all match, reset the game
        if timer.end():
            cursor_match = False
            mid_match = False
            ring_match = False
            index_match = False
            cursor.c = cursor_c[0]
        #if all matched, win
        if cursor_match == True and mid_match == True and ring_match == True and index_match ==True:
            program_state ='END'
        
    # end
    elif program_state =='END': 
        p5.textAlign(p5.CENTER)
        p5.textSize(200) 
        p5.fill(font_c['title'])
        p5.text('WIN!!!', 300, 300)
        p5.textSize(25)
        p5.fill(font_c['text1'])
        if timer.round <3:
            p5.text(f"Bravo! You passed with only {timer.round} round.", 300, 400)
            p5.text("You must be the master of your fingers!", 300, 430)
        elif timer.round>=3 and timer.round < 6:
            p5.text(f"You passed with {timer.round} rounds.", 300, 400)
            p5.text("Try to be friend with your fingers.", 300, 430)
        elif timer.round>=6:
            p5.text(f"I'm so sorry. You passed with {timer.round} rounds.", 300, 400)
            p5.text("Looks like you don't know your fingers very well...", 300, 430)
        
        

    



    
    


def keyPressed(event):
    global keydown_sound
    keydown_sound.play()
    #a secret timer/difficulty adjust trick for programmer/me,'['to minus,']'to add, backspace to reset to 10
    global timer_limit, timer
    if p5.key == ']':
        timer_limit += 1
        timer = Timer(580,50,timer_limit,targets=[cursor_target, l_mid_target, l_ring_target, l_index_target]) 
    elif p5.key == '[':
        if(timer_limit > 1):
            timer_limit -= 1
            timer = Timer(580,50,timer_limit,targets=[cursor_target, l_mid_target, l_ring_target, l_index_target])
    elif(p5.keyCode == p5.BACKSPACE):
        timer_limit = 10
        timer = Timer(580,50,timer_limit,targets=[cursor_target, l_mid_target, l_ring_target, l_index_target])

def keyReleased(event):
    global keyup_sound, timer
    global program_state
    keyup_sound.play()
    if program_state == 'INTRO' and p5.key ==" ":
        program_state = 'PLAY'
        print('change program_state to ' + program_state)
    elif (program_state == 'PLAY' or program_state == 'END') and p5.keyCode == p5.ESCAPE:
        program_state = 'INTRO'
        timer.round = 1
        print('change program_state to ' + program_state)

    

def mousePressed(event):
    
    global cursor_list, menu_list, cursor, cursor_target,win,timer, rhand
    global cursor_match, click_sound
    cursor_match = False
    click_sound.play()
    if p5.mouseButton == p5.LEFT:
        rhand.index.c=nail[1]  #nail change color when click   
        new_cursor = Cursor(x=p5.mouseX,y=p5.mouseY)
        cursor_list.append(new_cursor)
        if cursor.is_match(cursor_target):
            cursor_match = True
            cursor_list.clear()# if the cursor matched, clear all wrong cursors
            
        if len(menu_list)>0:
            menu_list.clear() # when click left, cleare all menus 
    elif p5.mouseButton == p5.RIGHT: 
        rhand.mid.c=nail[1]  #nail change color when click 
        new_menu = Menu(x = p5.mouseX, y = p5.mouseY)
        menu_list.append(new_menu)
    print(cursor_match)

def mouseReleased(event):
    global release_sound
    release_sound.play()
    # when click mouse, related finger's nail will change color
    rhand.index.c=nail[0]
    rhand.mid.c=nail[0] 

        