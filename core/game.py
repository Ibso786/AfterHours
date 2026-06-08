
import pygame
from scenes.title import TitleScene
from scenes.garage import GarageScene
from scenes.race import RaceScene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption("AfterHours")
        self.clock = pygame.time.Clock()
        self.scenes = {
        "title": TitleScene(self),
        "garage": GarageScene(self),
        "race": RaceScene(self)
    }
        self.current = "title"

    def change_scene(self,name):
        self.current=name

    def run(self):
        running=True
        while running:
            dt=self.clock.tick(60)/1000
            scene=self.scenes[self.current]

            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    running=False
                scene.handle_event(e)

            scene.update(dt)
            scene.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
