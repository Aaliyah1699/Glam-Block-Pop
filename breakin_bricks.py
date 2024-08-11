import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Glam Block Pop')

#  Bat
bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()

#  Ball
ball = pygame.image.load('./images/ball.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()

#  Brick
brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_rows = 5
brick_cols = 3
#  Calculate bricks
for y in range(brick_rows):
    brickY = y * brick_rect[3]
    for x in range(brick_cols):
        brickX = x * brick_rect[2]
        bricks.append((brickX, brickY))

clock = pygame.time.Clock()
game_over = False

while not game_over:
    dt = clock.tick(50)
    screen.fill((0, 0, 0))
    #  Place bricks on screen
    for b in bricks:
        screen.blit(brick, b)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

pygame.quit()
