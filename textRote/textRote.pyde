# The message to be displayed
message = "text along a curve"

# The radius of a circle
r = 100

def setup():
    global f
    size(320, 320)
    f = createFont("Georgia",40,True)
    textFont(f)
    # The text must be centered!
    textAlign(CENTER)
    smooth()
    frameRate(60)

offset=0
def draw():
    global r, f, offset
    background(255)

    # Start in the center and draw the circle
    translate(width / 2, height / 2)
    noFill()
    stroke(0)
    ellipse(0, 0, r*2, r*2)

    # We must keep track of our position along the curve
    arclength = 0
    offset-=0.005
    # For every box
    for i in xrange(len(message)):

        # Instead of a constant width, we check the width of each character.
        currentChar = message[i]
        w = textWidth(currentChar)

        # Each box is centered so we move half the width
        arclength += w/2
        # Angle in radians is the arclength divided by the radius
        # Starting on the left side of the circle by adding PI
        theta = offset + arclength / r   

        pushMatrix();
        # Polar to cartesian coordinate conversion
        translate(r*cos(theta), r*sin(theta))
        # Rotate the box
        rotate(theta+sin(offset+i))   # rotation is offset by 90 degrees
        # Display the character
        fill(0)
        text(currentChar,0,0)
        popMatrix()
        # Move halfway again
        arclength += w/2
