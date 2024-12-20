import sys 
import pygame
from constants import * 
import player
from asteroid import Asteroid
import asteroidfield
import shot 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    shot.Shot.containers = (updatable, drawable)

    asteroid_field = asteroidfield.AsteroidField()
    player_1 = player.Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for i in updatable:
            i.update(dt)

        for i in asteroids:
            if i.collides_with(player_1):
                print("Game over!")
                sys.exit()
            for s in shots:
                if i.collides_with(s):
                    i.kill()
                    s.kill()

        # create a black screen:
        screen.fill((0,0,0))

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()