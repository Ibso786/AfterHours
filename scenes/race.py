import pygame
import random
from systems.save_system import save_game

class RaceScene:

    def __init__(self, game):
        self.game = game

        self.progress = 0
        self.enemy_progress = 0

        self.finished = False
        self.reward = 0

        self.rpm = 1000
        self.boost = 0

    def handle_event(self, e):

        if self.finished:
            if e.type == pygame.KEYDOWN:
                self.game.change_scene("garage")

    def update(self, dt):

        if self.finished:
            return

        self.rpm += random.randint(50, 120)

        if self.rpm > 8000:
            self.rpm = 3000

        self.boost = min(20, self.boost + 0.15)

        self.progress += random.uniform(0.5, 1.2)
        self.enemy_progress += random.uniform(0.4, 1.1)

        if self.progress >= 100:

            self.finished = True
            self.reward = random.randint(250, 700)

            self.game.scenes["garage"].profile["cash"] += self.reward
            self.game.scenes["garage"].profile["fuel"] -= 5

            save_game(
                self.game.scenes["garage"].profile
            )

        elif self.enemy_progress >= 100:

            self.finished = True

    def draw(self, screen):

        screen.fill((10, 10, 20))

        font = pygame.font.SysFont("consolas", 30)

        title = font.render(
            "DRAG RACE",
            True,
            (0,255,200)
        )

        screen.blit(title, (40,30))

        pygame.draw.rect(
            screen,
            (50,50,60),
            (100,200,1000,30)
        )

        pygame.draw.rect(
            screen,
            (0,255,200),
            (100,200,self.progress*10,30)
        )

        pygame.draw.rect(
            screen,
            (50,50,60),
            (100,300,1000,30)
        )

        pygame.draw.rect(
            screen,
            (255,80,80),
            (100,300,self.enemy_progress*10,30)
        )

        screen.blit(
            font.render(
                f"RPM: {int(self.rpm)}",
                True,
                (255,255,255)
            ),
            (100,420)
        )

        pygame.draw.rect(
            screen,
            (40,40,40),
            (100,470,400,25)
        )

        pygame.draw.rect(
            screen,
            (0,255,150),
            (100,470,int(self.boost*20),25)
        )

        screen.blit(
            font.render(
                f"BOOST: {self.boost:.1f} PSI",
                True,
                (255,255,255)
            ),
            (100,510)
        )

        if self.finished:

            text = "YOU WIN"

            if self.enemy_progress >= 100:
                text = "YOU LOSE"

            result = pygame.font.SysFont(
                "consolas",
                60
            ).render(
                text,
                True,
                (255,255,255)
            )

            screen.blit(result,(420,100))

            if text == "YOU WIN":

                screen.blit(
                    font.render(
                        f"+${self.reward}",
                        True,
                        (0,255,150)
                    ),
                    (520,180)
                )

            screen.blit(
                font.render(
                    "PRESS ANY KEY",
                    True,
                    (255,255,255)
                ),
                (450,600)
            )
