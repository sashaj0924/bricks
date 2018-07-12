xCoordinate = 50
speedx = 5
speedy = 5
yCoordinate = 50
ellipseSize = 20
red = random(255)
green = random(255)
blue = random(255)

def setup():
    global paddleSize
    size(400, 500)
    paddleSize= 60

    
def draw():
    global paddleSize
    background(0)
    global xCoordinate, speedx, yCoordinate, speedy, red, green, blue, ellipseSize
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
    fill (212, 135, 173)
    noStroke()
    fill( 244, 208, 63)
    rect( 0, 0,  80, 30)
    fill(125, 60, 152 )
    rect (80, 0, 80, 30)
    fill( 9, 246, 54)
    rect( 160, 0, 80, 30)
    fill(170, 183, 184)
    rect (240, 0, 80, 30)
    fill(246, 9, 41 )
    rect (320, 0, 80, 30)
    
    fill( 246, 31, 9)
    rect(mouseX - paddleSize/2 , 460, paddleSize, 20)

    
