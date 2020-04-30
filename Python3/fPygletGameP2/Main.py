import pyglet
from pyglet.window import key
from GameObj import GameOb, imgloader

class Gwin(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400, 100)
        self.frame_rate = 1/60.0

        self.fire = False
        self.firerate = 0

        self.fire2 = False
        self.firerate2 = 0

        BGpic = pyglet.sprite.Sprite(imgloader("BG.jpg"))
        self.BG = GameOb(0, 0, BGpic, 5, 5)

        playerE = pyglet.sprite.Sprite(imgloader("poulpe.png"))
        self.player2 = GameOb(300, 100, playerE, 0.5, 0.5)
        self.pth = 1000

        playerS = pyglet.sprite.Sprite(imgloader("poulpi.png"))
        self.player = GameOb(800, 100, playerS, 0.5, 0.5)
        self.poh = 1000

        self.bulletS = imgloader("pew.png")
        self.bullet_list = []

        self.bulletE = imgloader("pew.png")
        self.bulletEL = []

    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.player.velx = 300
        if symbol == key.LEFT:
            self.player.velx = -300
        if symbol == key.UP:
            self.player.vely = 300
        if symbol == key.DOWN:
            self.player.vely = -300
        if symbol == key.NUM_0:
            self.fire = True
        #PLAYE 2
        if symbol == key.D:
            self.player2.velx = 300
        if symbol == key.A:
            self.player2.velx = -300
        if symbol == key.W:
            self.player2.vely = 300
        if symbol == key.S:
            self.player2.vely = -300
        if symbol == key.Q:
            self.fire2 = True

    def on_key_release(self, symbol, modifiers):
        if symbol in (key.RIGHT, key.LEFT):
            self.player.velx = 0
        if symbol in (key.UP, key.DOWN):
            self.player.vely = 0
        if symbol == key.NUM_0:
            self.fire = False
        #player2
        if symbol in (key.D, key.A):
            self.player2.velx = 0
        if symbol in (key.W, key.S):
            self.player2.vely = 0
        if symbol == key.Q:
            self.fire2 = False

    def update_BG(self, dt):
        self.BG.update(dt)
        if self.player.posy >= 650:
            self.BG.vely -= 30 * dt
        if self.player.posy <= 0:
            self.BG.vely += 30 * dt

    def update_player2(self, dt):
        self.player2.update(dt)

    def update_player(self, dt):
        self.player.update(dt)
        if(self.player.posx < 0):
            self.player.sprite.x = 0
        #print(round(self.player.posx, 2), " :X:::Y: ", round(self.player.posy, 2))

    def update_bull(self, dt):
        for bull in self.bullet_list:
            bull.update(dt)
            bull.velx -= 900 * dt
            #print(len(self.bullet_list)," ::::: ",round(bull.posx, 2))
            if bull.posx < -50:
                self.bullet_list.pop(0)
                #print(len(self.bullet_list))

    def update_bull2(self, dt):
        for bull in self.bulletEL:
            bull.update(dt)
            bull.velx += 900 * dt
            #print(len(self.bulletEL)," ::::: ",round(bull.posx, 2))
            if bull.posx > 2000:
                self.bulletEL.pop(0)
                #print(len(self.bulletEL))

    def pfire(self, dt):
        self.firerate -= dt
        if self.firerate <= 0:
            self.bullet_list.append(GameOb(self.player.posx + 75, self.player.posy + 100, pyglet.sprite.Sprite(self.bulletS), 0.2, 0.5))
            self.firerate += 0.09

    def pfireE(self, dt):
        self.firerate2 -= dt
        if self.firerate2 <= 0:
            self.bulletEL.append(GameOb(self.player2.posx + 210, self.player2.posy + 100, pyglet.sprite.Sprite(self.bulletE), 0.2, 0.5))
            self.firerate2 += 0.09

    def pHealth(self):
        for bpo in self.bullet_list:
            if (bpo.posx <= self.player2.posx+1) or (bpo.posx <= self.player2.posx-1):
                self.bullet_list.pop(0)
                self.pth -= 1
                print(self.poh," :P1:::::P2: ", self.pth)

    def pHealth2(self):        #p2
        for bpt in self.bulletEL:
            if ((bpt.posx >= self.player.posx+1) or (bpt.posx >= self.player.posx-1)) and ((bpt.posy <= self.player.posy+100) and (bpt.posy >= self.player.posy-100)):
                self.bulletEL.pop(0)
                self.poh -= 1
                print(self.poh," :P1:::::P2: ", self.pth)

        if self.pth == 0:
            print("Player one wins")
        elif self.poh == 0:
            print("Player two wins")

    def on_draw(self):
        self.clear()
        self.BG.draw()
        self.player.draw()
        self.player2.draw()
        for bull in self.bullet_list:
            bull.draw()
        for bull2 in self.bulletEL:
            bull2.draw()

    def update(self, dt):
        self.update_BG(dt)
        self.update_player(dt)
        self.update_player2(dt)
        if self.fire == True:
            self.pfire(dt)
        self.update_bull(dt)
        if self.fire2 == True:
            self.pfireE(dt)
        self.update_bull2(dt)
        self.pHealth()
        self.pHealth2()

if __name__ == "__main__":
    win = Gwin(1200, 900, "fGame", resizable=True)
    pyglet.clock.schedule_interval(win.update, win.frame_rate)

    pyglet.app.run()
