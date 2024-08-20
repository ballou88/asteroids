import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (updateable, drawable, shots)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updateable:
            obj.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
