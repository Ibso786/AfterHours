
import pygame
from systems.save_system import load_save

class GarageScene:
    def __init__(self,game):
        self.game=game
        self.profile=load_save()

    def handle_event(self,e):
        pass

    def update(self,dt):
        pass

    def draw(self,screen):
        screen.fill((15,15,25))

        title=pygame.font.SysFont("consolas",48).render("GARAGE",True,(0,255,200))
        screen.blit(title,(40,20))

        pygame.draw.rect(screen,(35,35,50),(70,120,500,260),border_radius=10)

        pygame.draw.rect(screen,(70,70,90),(750,120,300,180),border_radius=10)

        car=self.profile["cars"][0]

        f=pygame.font.SysFont("consolas",28)

        screen.blit(f.render(f"Cash: ${self.profile['cash']}",True,(255,255,255)),(90,150))
        screen.blit(f.render(f"Rep: {self.profile['rep']}",True,(255,255,255)),(90,190))
        screen.blit(f.render(f"Current Car: {car}",True,(255,255,255)),(90,240))

        pygame.draw.rect(screen,(0,255,200),(850,170,120,60),border_radius=6)
        screen.blit(f.render("CIVIC",True,(0,0,0)),(865,185))

        screen.blit(f.render("RACES COMING IN V4",True,(0,255,150)),(90,330))
