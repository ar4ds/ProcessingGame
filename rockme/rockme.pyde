add_library('minim')

def setup():
    global audio
    #size(800,800)
    fullScreen(P3D)
    background(0)
    mini=Minim(this)
    audio=mini.loadFile("apple.mp3",1024)
    audio.loop()
    
def draw():
    voice = audio.mix.level()
    voice=max(voice,.05)
    bgOffset=.2
    background((1-voice)*255*voice*bgOffset,255*(voice-.5)*bgOffset,255*(voice-.1))
    stroke((1-voice)*255*voice,255*(voice-.5),255*(voice-.1))
    strokeWeight(20)
    noFill()
    ellipseMode(CENTER)
    _size=min(width,height)
    ellipse(width*.5, height*.5, voice*_size, voice*_size)
    offset=voice*(1+voice)
    fill((voice)*255*voice,255*(voice-.5),255*(voice-.1))
    strokeWeight(5)
    ellipse(width*.5, height*.5, voice*_size*offset, voice*_size*offset)
    
    for i in xrange((int)(voice*100)):
        pushMatrix()
        noFill()
        rSize= voice*_size*(1+offset)
        translate(width*.5,height*.5)
        rotate(360*voice)
        strokeWeight(random(6))
        stroke(0)
        rect(0,0,rSize,rSize)
        strokeWeight(random(10))
        rect(-rSize*.5,-rSize*.5,rSize,rSize)
        popMatrix()
