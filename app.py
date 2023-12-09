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
# utils 
from utils.collide import collide

pygame.font.init()

pygame.display.set_caption("Touhou Project")
font_primary = pygame.font.SysFont("OCR-A Extended", 20)
font_secondary = pygame.font.SysFont("Impact", 40)

FPS = 60
clock = pygame.time.Clock()


def main():
    run = True
    level = 0
    lives = 5

    enemies = []
    initial_wave_length = 3

    player = Player((window.WIDTH / 2) - 35, window.HEIGHT - 120, 75, 75)
    
    lost = False
    won = False
    loading_count = 0

    def redraw_window():
        window.WINDOW.blit(background.BACKGROUND, (0,0))
        
        # draw text
        score_label = font_primary.render(f"Score: {player.score}", 1, (255,255,255))
        window.WINDOW.blit(score_label, (10, 10))
        level_label = font_primary.render(f"Level: {level}", 1, (255,255,255))
        window.WINDOW.blit(level_label, (window.WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(window.WINDOW)
            
        # draw lives
        for i in range(1, lives + 1):
            window.WINDOW.blit(misc_objects.HEART, ((window.WIDTH - int(misc_objects.HEART_WIDTH * i) - misc_objects.HEART_WIDTH / 2), (window.HEIGHT - misc_objects.HEART_HEIGHT) - misc_objects.HEART_WIDTH / 2))

        player.draw(window.WINDOW)

        if lost:
            lost_label = font_secondary.render("Game Over", 1, (255,255,255))
            window.WINDOW.blit(lost_label, (window.WIDTH / 2 - lost_label.get_width() / 2, window.HEIGHT / 2 - lost_label.get_height() / 2))
            final_score_label = font_primary.render(f"Final Score: {player.score}", 1, (255,255,255))
            window.WINDOW.blit(final_score_label, (window.WIDTH / 2 - final_score_label.get_width() / 2, (window.HEIGHT / 2 - lost_label.get_height() / 2) + lost_label.get_height()))
            
        if won:
            won_label = font_secondary.render("You Won!", 1, (255,255,255))
            window.WINDOW.blit(won_label, (window.WIDTH / 2 - won_label.get_width() / 2, window.HEIGHT / 2 - won_label.get_height() / 2))
            final_score_label = font_primary.render(f"Final Score: {player.score}", 1, (255,255,255))
            window.WINDOW.blit(final_score_label, (window.WIDTH / 2 - final_score_label.get_width() / 2, (window.HEIGHT / 2 - won_label.get_height() / 2) + won_label.get_height()))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            loading_count += 1
        
        if level >= 10:
            won = True
            loading_count += 1

        if lost or won:
            if loading_count > FPS * 3:
                run = False
            else:
                continue
                
        if len(enemies) == 0:
            level += 1
            wave_length = int((initial_wave_length * level) * 1.85)
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, window.WIDTH - 50), random.uniform(-200, int(-(window.HEIGHT * ((level - 1) * 0.21 + 1)))), random.choice(["alien", "blue", "purple"]), velocity=1)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    quit()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x + player.velocity > 0:
            player.x -= player.velocity
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.x + player.width < window.WIDTH:
            player.x += player.velocity
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.y > 0:
            player.y -= player.velocity
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.y + player.height < window.HEIGHT:
            player.y += player.velocity
            
        player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy.velocity)
            enemy.move_lasers(player)
            
            if random.randrange(0, int(1.75 * FPS)) == 1:
                enemy.shoot()
                
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
                player.increment_score()
            elif (enemy.y + enemy.height > window.HEIGHT):
                enemies.remove(enemy)
                lives -= 1
        
        player.move_lasers(enemies)
        
# start program
main()