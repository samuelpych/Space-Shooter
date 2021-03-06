"""
spaceshooter.py
Author: Sam Pych
Credit: source code for space shooter and tutorial, ggame repository, Kyle Postans

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar

Your game must include the following:

A fixed star field background.
At least one player.
Either multiple playes, or some (in)animate object(s) to avoid.
Animated rocket thrust for the ship sprites.
Collisions destroy ships.
Moving and rotating ships - physics realism at your discretion.
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame


class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)
class Sun(Sprite):
    asset= ImageAsset("images/sun.png")
    width=100
    height=100
    def __init__(self, position):
        super().__init__(Sun.asset,position)
        self.fxcenter=.5
        self.fycenter=.5
    
class SpaceShip(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        Spacewar.listenKeyEvent("keydown", "space", self.thrustOn)
        Spacewar.listenKeyEvent("keyup", "space", self.thrustOff)
        Spacewar.listenKeyEvent("keydown", "w", self.up)
        Spacewar.listenKeyEvent("keydown","a",self.left)
        Spacewar.listenKeyEvent("keydown","s",self.down)
        Spacewar.listenKeyEvent("keydown","d",self.right)
        Spacewar.listenKeyEvent("keydown","left arrow",self.rotateleft)
        Spacewar.listenKeyEvent("keydown","right arrow",self.rotateright)
        Spacewar.listenKeyEvent("keyup","right arrow",self.stopplz)
        Spacewar.listenKeyEvent("keyup","left arrow",self.stopplz)
        
        
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        boom=self.collidingWithSprites(Sun)
        if self.x >1240:
            self.x=1239
        if self.x <-1:
            self.x=0
        if self.y >512:
            self.y=513
        if self.y <-1:
            self.y=0
        if len(boom) >0:
            self.visible=False
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
    def thrustOn(self, event):
        self.thrust = 1
    def stopplz(self, event):
        self.vr=0
    def thrustOff(self, event):
        self.thrust=0
    def up(self, event):
        self.vy -=2
    def down(self, event):
        self.vy +=2
    def left(self, event):
        self.vx -=2
    def right(self, event):
        self.vx +=2
    def rotateleft(self, event):
        self.vr +=.01
    def rotateright(self, event):
        self.vr -=.1
class Spacewar(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        for x in range(self.width//Stars.width + 1):
            for y in range(self.height//Stars.height + 1):
                Stars((x*Stars.width, y*Stars.height))
                self.sun=Sun((self.width/2, self.height/2))
        self.listenKeyEvent('keydown', 'space', self.space)
        self.listenKeyEvent('keydown', 'left', self.space)
        
        SpaceShip((350,250))

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

    def space(self, evt):
        print('printing this for fun')
        



app = Spacewar(0,0)
app.run()
"""
Spacewar.listenKeyEvent("keydown", "w", ...
Spacewar.listenKeyEvent("keydown", "a",
Spacewar.listenKeyEvent("keydown", "s",
Spacewar.listenKeyEvent("keydown", "d",
Spacewar.listenKeyEvent("keyup", "w",
Spacewar.listenKeyEvent("keyup", "a",
Spacewar.listenKeyEvent("keyup", "s",
Spacewar.listenKeyEvent("keyup", "d",
"""