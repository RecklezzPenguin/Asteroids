# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game Loop
    while(True):
        #Allows game to be killed when window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collision_check(player):
                sys.exit("Game over!")

        screen.fill((0,0,0))

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        #set to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
