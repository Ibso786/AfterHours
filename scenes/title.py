
import pygame, random

class TitleScene:
    def __init__(self,game):
        self.game=game
        self.particles=[]

    def handle_event(self,e):
        if e.type==pygame.KEYDOWN:
            self.game.change_scene("garage")

    def update(self,dt):
        for _ in range(4):
            self.particles.append([random.randint(0,1280),720,random.randint(2,7)])
        self.particles=[p for p in self.particles if p[1]>0]
        for p in self.particles:
            p[1]-=p[2]

    def draw(self,screen):
        screen.fill((8,8,18))
        for p in self.particles:
            pygame.draw.circle(screen,(0,255,180),(int(p[0]),int(p[1])),2)

        title=pygame.font.SysFont("consolas",80).render("AFTERHOURS",True,(0,255,200))
        msg=pygame.font.SysFont("consolas",28).render("PRESS ANY KEY",True,(255,255,255))

        screen.blit(title,(290,250))
        screen.blit(msg,(500,360))
