import pygame as pg
import sys
from scripts.scenes.game import Game
from scripts.scenes.scene1 import Scene1
from scripts.scenes.scene2 import Scene2
from scripts.scenes.scene3 import Scene3
from scripts.scenes.transition import Transition

# GAME LAUNCHES HERE
g = Game()
pg.display.set_caption("ODD FILES")
# MAIN MENU
while g.menuRunning:
    g.mainMenu(g.canvas)
    g.handle_menu_clicks()  # Check for button clicks in the menu
    g.menu()

#Scene 1
s1 = Scene1(g.screen,g.clock)
s1.sceneRunning = True
s1.dialogue_system.start_dialogue()
while s1.scene1Playing:
    s1.main2()

# GAME RUNNING
g.dialogue_system.start_dialogue()
g.running = True  # Change it when the button function is added
while g.running:
    g.main()
    #g.game_over()
print("TIME TO SEARCH")

#Scene 2
s2 = Scene2(g.screen,g.clock)
s2.scene1Playing = True
s2.dialogue_system.start_dialogue()
while s2.scene1Playing:
    s2.main2()

print("Transition scene")
#Transition
t = Transition(g.screen,g.clock)
t.transitionPlaying = True
while t.transitionPlaying:
    t.main2()


'''---------------------------------------------------------------------------------------------------------------------------'''



#BOSSES
#VIRUS
s3 = Scene3(g.screen,g.clock)
s3.virusPlaying = True
while s3.virusPlaying:
    s3.main()

#Quit Game
pg.quit()
sys.exit()
