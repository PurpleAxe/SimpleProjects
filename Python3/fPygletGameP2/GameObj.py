import pyglet

def imgloader(img):
    img = pyglet.image.load("assets/"+img)
    return img

class GameOb:
    def __init__(self, posx, posy, sprite = None, scalex = 1, scaley = 1):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if sprite is not None:
                self.sprite = sprite
                self.sprite.x = self.posx
                self.sprite.y = self.posy
                self.sprite.scale_x = scalex
                self.sprite.scale_y = scaley

    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        self.sprite.x += self.velx * dt
        self.sprite.y += self.vely * dt
        self.posx = self.sprite.x
        self.posy = self.sprite.y
