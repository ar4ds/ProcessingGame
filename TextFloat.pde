PFont f;
String message = "Each character is written individually.";

void setup() {
  size(400, 150);
  f = createFont("Arial",20,true);
}

void draw()
{
}

void mouseMoved()
{
  drawT();
}

void drawT() {
  float w = width/message.length();
  background(255);
  fill(0);
  textFont(f);
  int x = 10;
  for (int i = 0; i < message.length(); i++) {
    textSize(max(50-abs(mouseX - w*i), 3));
    text(message.charAt(i),w*i,height*.25);
    // textWidth() spaces the characters out properly.
    x += textWidth(message.charAt(i));
  }
}
