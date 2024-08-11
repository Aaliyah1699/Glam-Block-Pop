import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Glam Block Pop')

#  Bat
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100

#  Ball
ball = pygame.image.load('./images/ball.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200, 300)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

#  Brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_cols + brick_gap) // 2
#  Calculate bricks
for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX, brickY))

clock = pygame.time.Clock()
game_over = False
x = 0

while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))
    #  Place bricks on screen
    for b in bricks:
        screen.blit(brick, b)

    #  Place bat & ball on screen
    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()

    #  Move bat
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    bat_rect[0] = x
    #  Move ball & restrict it to not go off-screen
    if pressed[K_SPACE]:
        ball_served = True
    #  Batting the ball
    if bat_rect[0] + bat_rect.width >= ball_rect[0] >= bat_rect[0] and \
            ball_rect[1] + ball_rect.height >= bat_rect[1] and \
            sy > 0:
        sy *= -1
        # Increase difficulty
        sx *= 1.01
        sy *= 1.01
        continue

    # Top
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1
    # Bottom
    if ball_rect[1] >= screen.get_height() - ball_rect.height:
        ball_served = False
        ball_rect.topleft = ball_start
    # Left
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1
    # Right
    if ball_rect[0] >= screen.get_width() - ball_rect.width:
        ball_rect[0] = screen.get_width() - ball_rect.width
        sx *= -1

    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy

    pygame.display.update()

pygame.quit()
