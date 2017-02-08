import ddf.minim.*;
Minim minim;
AudioPlayer player, player2;

int numFrames = 9;  // The number of frames in the animation
int currentFrame = 0;
Animation[] dragon = new Animation[9];
Animation[] bird = new Animation[10];
boolean toggleDragon = true;
    
void setup() {
  size(800, 600);
  frameRate(6);
  
  dragon[0]  = new Animation("dragon1");
  dragon[1]  = new Animation("dragon2"); 
  dragon[2]  = new Animation("dragon3");
  dragon[3]  = new Animation("dragon4"); 
  dragon[4]  = new Animation("dragon5");
  dragon[5]  = new Animation("dragon6"); 
  dragon[6]  = new Animation("dragon7");
  dragon[7]  = new Animation("dragon8"); 
  dragon[8]  = new Animation("dragon9");
  bird[0]  = new Animation("bird1");
  bird[1]  = new Animation("bird2"); 
  bird[2]  = new Animation("bird3");
  bird[3]  = new Animation("bird4"); 
  bird[4]  = new Animation("bird5");
  bird[5]  = new Animation("bird6"); 
  bird[6]  = new Animation("bird7");
  bird[7]  = new Animation("bird8"); 
  bird[8]  = new Animation("bird9");
  bird[9]  = new Animation("bird10");
  
  // we pass this to Minim so that it can load files from the data directory
  minim = new Minim(this);
  
  // loadFile will look in all the same places as loadImage does.
  // this means you can find files that are in the data folder and the 
  // sketch folder. you can also pass an absolute path, or a URL.
  //put your audio file names between the quotes, and drag them over this window 
  player = minim.loadFile("data/addingMachine1.mp3");
  player2 = minim.loadFile("data/addingMachine3.mp3");
  
} 

void draw() { 
  background(0);
  
  if (toggleDragon == true) {
       // Use % to cycle through frames
      dragon[currentFrame].display(0, 0);
      player.pause();
      player.rewind();
          if(!isPlaying(player2)){
      player2.rewind();        
      player2.play();
            }
      if (!mousePressed) {
        currentFrame = (currentFrame+1) % numFrames;
      }
  } else {
    // Use % to cycle through frames
      bird[currentFrame].display(0, 0);
      player2.pause();
      player2.rewind();
      if(!isPlaying(player)){
        player.rewind();        
        player.play();
      }
      if (!mousePressed) {
        currentFrame = (currentFrame+1) % numFrames;
      }
  }
  
}

void mouseClicked() {
  if (toggleDragon == true) {
    toggleDragon = false;
  } else {
    toggleDragon = true;
  }
}

// Class for animating a sequence of GIFs

class Animation {
  PImage[] images;
  int frame;
  
  Animation(String imagePrefix) {
    images = new PImage[2];

    images[0] = loadImage("data/" + imagePrefix + ".1.png");
    images[1] = loadImage("data/" + imagePrefix + ".2.png");
  }

  void display(float xpos, float ypos) {
    frame = (frame+1) % 2;
    image(images[frame], xpos, ypos);
  }
  
  int getWidth() {
    return images[0].width;
  }
}