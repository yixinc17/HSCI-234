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
    def update(self):
        p5.textFont(font_num) 
        p5.fill(46)  
        p5.textSize(40)
        self.count = self.t-int((p5.millis()-self.timer)/1000) 
        if self.count<=0:
            self.count = self.t
            self.timer = p5.millis()
            for target in self.targets:
                target.random(100, 500)
        p5.text(self.count, self.x,self.y)
    def end(self):
        if self.count <=1:
            return True
        