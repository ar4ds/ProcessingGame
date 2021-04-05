add_library('minim')
cellsize = 5  # Dimensions of each cell in the grid

def setup():
    global img, cols, rows, cellsize, radius,audio
    audio=Minim(this).loadFile('apple.mp3',1024)
    audio.loop()
    frameRate(120)
    # size(1024,1920, P3D) 
    size(1000,999, P3D) 
    radius=min(width,height)*.5
    img  = loadImage("2.jpg")
    cols = width/cellsize              # Calculate number of columns
    rows = height/cellsize             # Calculate number of rows
    cursor(CROSS)

def draw():
    global img, cols, rows, cellsize,radius,audio
    voice=audio.mix.level()
    background(0)
    loadPixels()                                    
    # Begin loop for columns
    for i in xrange(cols):
        # Begin loop for rows
        for j in range(rows):
            x = i*cellsize + cellsize/2  # x position
            y = j*cellsize + cellsize/2  # y position
            loc = x + y*width            # Pixel array location
            c = img.pixels[loc]          # Grab the color
            distance=abs(dist(radius,radius,x,y)-radius*voice)
            if distance>radius*.05 or distance<20:
                continue
            z = distance * brightness(img.pixels[loc]) - 100.0
            
            
            # Translate to the location, set fill and stroke, and draw the rect
            pushMatrix()
            translate(x,y,z*.05)
                        
            stroke(255,25,255, 50*(1+voice))
            strokeWeight(1)
            line(0,0,radius-x,radius-y)
            len=1
            # line(0,0,(radius-x)*len,(radius-y)*len)
            
            fill(c)
            noStroke()
            # rectMode(CENTER)
            # rect(0,0,cellsize,cellsize)            
            ellipseMode(CENTER)
            ellipse(0,0,cellsize,cellsize)
            popMatrix()
