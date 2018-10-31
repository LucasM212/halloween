height2 = -100
x = 320
x2 = -100
x3 = 640
height3 = 240

def setup():
    global sat_img
    size(640, 480)
    sat_img = loadImage("halloween-scarecrow-clipart-2.png")
    
    
def draw():
    
    global x
    global height2
    global x2
    global x3
    global height3
    
    if height2 >= 640:
        height2 = -100
    height2 += 1
    
    if x2 >= 800:
        x2 = -100
    x2 += 1
    
    if x3 <= -100:
        x3 = 640
    x3 -= 1
    
    background(139, 90, 0)
    
    noStroke()
    fill(255,255,0)
    ellipse(x, height2, 100, 100)
    
    fill(0, 0, 0)
    ellipse(x2, height/2, 50, 50)
    ellipse(x2+30, height/2, 50, 50)
    ellipse(x2+10, height/2-20, 50, 50)
    
    fill(0, 0, 0)
    ellipse(x3, height3, 50, 50)
    ellipse(x3+30, height3, 50, 50)
    ellipse(x3+10, height3-20, 50, 50)
    
    image(sat_img, 50, 50, 550, 550)

    
