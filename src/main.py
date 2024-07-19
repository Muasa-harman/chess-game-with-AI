import pygame
import sys
from const import *
from game import Game
from square import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption('Chess game')
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            pygame.display.update()        

if __name__ == "__main__":
    main = Main()
    main.mainloop()