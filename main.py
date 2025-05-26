import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    pygame.init()
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    main_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")

    while True:
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_detected(main_player):
                sys.exit("GAME OVER")
            for shot in shots:
                if asteroid.collision_detected(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)


if __name__ == "__main__":
    main()
