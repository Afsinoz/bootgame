import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    Shot.containers = (shots,updatable, drawable)

    player = Player(x,y)

    while True:
        delta_time = fps.tick(60)
        dt = delta_time/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for upda in updatable:
            upda.update(dt) 


        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()    
                    asteroid.split()
        





        screen.fill(color=(0,0,0))

        for dr in drawable:
            dr.draw(screen)
        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__=="__main__":
    main()


