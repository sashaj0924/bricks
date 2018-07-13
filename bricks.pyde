xCoordinate = random(20, 380)
speedx = 6
speedy = 5
yCoordinate = 50
ellipseSize = 20
red = random(255)
green = random(255)
blue = random(255)
r1 = 244
g1 = 208
b1 = 63
r2 = 125
g2 = 60
b2 = 152
r3 = 9
g3 = 246
b3 = 54
r4 = 170
g4 = 183
b4 = 184
r5 = 246
g5 = 9
b5 = 41 

def setup():
    global paddleSize
    size(400, 500)
    paddleSize= 60

    
def draw():
    global paddleSize
    background(0)
    global xCoordinate, speedx, yCoordinate, speedy, red, green, blue, ellipseSize
    global r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4, r5, g5, b5
    xCoordinate += speedx
    yCoordinate += speedy
    if xCoordinate >= 400-(ellipseSize/2) or xCoordinate <= ellipseSize/2:
        speedx = -speedx
    if yCoordinate <= 30 + ellipseSize/2:
        speedy = -speedy
    if yCoordinate == 450:
        if xCoordinate <= mouseX+(paddleSize/2) and xCoordinate >= mouseX- (paddleSize/2):
            speedy = -speedy
            
    fill(150)
    ellipse(xCoordinate, yCoordinate, ellipseSize, ellipseSize)
    noStroke()
    fill( r1, g1, b1)
    rect( 0, 0,  80, 30)
    fill(r2, g2, b2)
    rect (80, 0, 80, 30)
    fill(r3, g3, b3)
    rect( 160, 0, 80, 30)
    fill(r4, g4, b4)
    rect (240, 0, 80, 30)
    fill(r5, g5, b5)
    rect (320, 0, 80, 30)
    
    if yCoordinate == 40:
        if xCoordinate >= 0 and xCoordinate < 80:
            r1 = 0
            g1 = 0
            b1 = 0
    if yCoordinate == 40:
        if xCoordinate >= 80 and xCoordinate < 160:
            r2 = 0
            g2 = 0
            b2 = 0
    if yCoordinate == 40:
        if xCoordinate >= 160 and xCoordinate < 240:
            r3 = 0
            g3 = 0
            b3 = 0
    if yCoordinate == 40:
        if xCoordinate >= 240 and xCoordinate < 320:
            r4 = 0
            g4 = 0
            b4 = 0
    if yCoordinate == 40:
        if xCoordinate >= 320 and xCoordinate < 400:
            r5 = 0
            g5 = 0
            b5 = 0
            
    if r1 == 0 and r2 == 0 and r3 == 0 and r4 == 0 and r5 == 0:
        if g1 == 0 and g2 == 0 and g3 == 0 and g4 == 0 and g5 == 0:
            if b1 == 0 and b2 == 0 and b3 == 0 and b4 == 0 and b5 == 0:
                fill(0)
                rect(0, 0, 400, 500)
                fill(255)
                text("GAME OVER", 167, 240)
                text("YOU WIN!!", 173, 255)
                
    elif yCoordinate >= 490:
        fill(0)
        rect(0, 0, 400, 500)
        fill(255)
        text("GAME OVER", 167, 240)
        text("YOU LOSE", 173, 255)
        
    
    fill( 246, 31, 9)
    rect(mouseX - paddleSize/2 , 460, paddleSize, 20)

    
