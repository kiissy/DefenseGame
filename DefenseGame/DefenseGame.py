from bangtal import *
import time
import random

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene = Scene("코로나디펜스", "images/startbg.png")

gamebg = Object('images/gamebg.png')
gamebg.locate(scene, 0, 0)

startButton = Object('images/start.png')
startButton.locate(scene, 600, 270)
startButton.show()

endButton = Object('images/end.png')
endButton.locate(scene, 600, 230)
endButton.show()

timer = Timer(10.)
showTimer(timer)

def random_x():
    x = random.randrange(100, 1050)
    return x

def random_y():
    y = random.randrange(50, 600)
    return y

def random_index():
    index = random.randrange(1, 4)
    return index

corona_list = []
def some_show():
    someShow = 0
    for corona in corona_list:
        someShow = someShow + corona.isShow
    return someShow

class Corona(Object):
    def __init__(self, file, scene, x, y):
        super().__init__(file)
        self.x = x
        self.y = y
        self.locate(scene, x, y)
        self.isShow = True
        self.show()
        print(self.x)

    def onMouseAction(self, x, y, action):
        if self.isShow:
            self.hide()
            self.isShow = False

        if not some_show():
            showMessage('Game Clear!')

            startButton.setImage('images/restart.png')
            startButton.show()
            endButton.show()

            timer.stop()

def startButton_onMouse(x, y, action):
    global corona_list
    corona_list = []

    startButton.hide()
    endButton.hide()

    timer.set(10.)
    timer.start()

    gamebg.show()

    for i in range(20):
        corona = Corona("images/corona"+str(random_index())+".png", scene, random_x(), random_y())
        corona_list.append(corona)
startButton.onMouseAction = startButton_onMouse

def endButton_onMouse(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouse

def onTimeout():
    showMessage("Game Failed!!")
    gamebg.hide()
    for i in range(len(corona_list)):
        corona_list[i].hide()
    startButton.setImage('images/restart.png')
    startButton.show()
    endButton.show()
timer.onTimeout = onTimeout

startGame(scene)