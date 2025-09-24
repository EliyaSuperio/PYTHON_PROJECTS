import pygame

pygame.init()

pygame.display.set_caption("BOX GAME")
screen = pygame.display.set_mode((500, 500))

# Colors (R, G, B)
WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# player
player_size = 50
player_x =  2 
player_y =  2
playerx_change = 0
playery_change = 0

running = True
while running:
    # exiting the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # CONTROL FOR THE BOX
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerx_change = -1
            if event.key == pygame.K_d:
                playerx_change =  1
            if event.key == pygame.K_w:
                playery_change = -1
            if event.key == pygame.K_s:
                playery_change = +1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerx_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playery_change = 0

    player_x += playerx_change
    player_y += playery_change

    # keep the box inside the screen.
    if player_x < 0:
        player_x = 0
    if player_x > 500 - player_size:
        player_x = 500 - player_size
    if player_y < 0:
        player_y = 0
    if player_y > 500 - player_size:
        player_y = 500 - player_size

    screen.fill((0,0,0))
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
    
    # change the display & updates
    
    
    pygame.display.flip()
    # pygame.display.update()
