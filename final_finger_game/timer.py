#Timer class:
# timer count down with target updated
import js
p5 = js.window
font_num = p5.loadFont('font/digital-7.ttf')


# after game test, 5 sec is too difficult
class Timer:
    def __init__(self, x=0, y=0, t=10, targets=None):
        self.x=x
        self.y=y
        self.t = t #countdown time
        self.targets = targets or []
        self.count = t
        self.timer =0
        self.round =1
    def update(self):
        r=p5.map(self.count,self.t,0,0,255)
        p5.fill(r,76,21)
        p5.textFont(font_num)       
        p5.textSize(40)
        self.count = self.t-int((p5.millis()-self.timer)/1000) 
        if self.count<=0:
            self.count = self.t
            self.timer = p5.millis()
            #every t sec, targets updated 
            for target in self.targets:
                target.random(100, 500)
            self.round +=1
        p5.text(self.count, self.x,self.y)
    #to check if a round of timer is end
    def end(self):
        if self.count <=1:
            return True

        