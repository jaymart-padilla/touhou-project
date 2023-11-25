import pygame, time, random
# window
from constants import window
# background
from constants import background
# player
from ship.Player import Player
# enemy
from ship.Enemy import Enemy
# assets
from constants import misc_objects
# misc
from constants.fps import FPS

pygame.font.init()

pygame.display.set_caption("Touhou Project")
main_font = pygame.font.SysFont("OCR-A Extended", 20)
lost_font = pygame.font.SysFont("Impact", 40)

clock = pygame.time.Clock()


def main():
    run = True
    level = 0
    lives = 5
    
    enemies = []
    wave_length = 5
    WAVE_LENGTH_INCREMENT = int(wave_length * 1.25)

    player = Player((window.WIDTH / 2) - 35, window.HEIGHT - 100, 75, 75)

    lost = False
    lost_count = 0

    def redraw_window():
        window.WINDOW.blit(background.BACKGROUND, (0,0))
        
        # draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        window.WINDOW.blit(level_label, (window.WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(window.WINDOW)
            
        # draw lives
        for i in range(1, lives + 1):
            window.WINDOW.blit(misc_objects.HEART, ((window.WIDTH - int(misc_objects.HEART_WIDTH * i) - misc_objects.HEART_WIDTH / 2), (window.HEIGHT - misc_objects.HEART_HEIGHT) - misc_objects.HEART_WIDTH / 2))

        player.draw(window.WINDOW)

        if lost:
            lost_label = lost_font.render("Game Over", 1, (255,255,255))
            window.WINDOW.blit(lost_label, (window.WIDTH / 2 - lost_label.get_width() / 2, window.HEIGHT / 2 - lost_label.get_height() / 2))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False

        if len(enemies) == 0:
            level += 1
            wave_length += WAVE_LENGTH_INCREMENT
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, window.WIDTH - 50), random.uniform(-200, int(-(window.HEIGHT * ((level - 1) * 0.5 + 1)))), random.choice(["red", "blue", "green"]), velocity=1)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    quit()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x - player.velocity > 0:
            player.x -= player.velocity
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + player.velocity + player.width < window.WIDTH:
            player.x += player.velocity
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y - player.velocity > 0:
            player.y -= player.velocity
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + player.velocity + player.height + 15 < window.HEIGHT:
            player.y += player.velocity

        for enemy in enemies[:]:
            enemy.move(enemy.velocity)
            if (enemy.y + enemy.height > window.HEIGHT):
                enemies.remove(enemy)
                lives -= 1
            
# start program
main()