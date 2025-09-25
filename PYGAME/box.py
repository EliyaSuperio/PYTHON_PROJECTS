import pygame

pygame.init()

pygame.display.set_caption("2 BOX")

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# BOX 1 
box_color = BLUE
box_size = 50
box_x = 100
box_y = 400
box_speed = 1 

# BOX 2
box2_color = RED
box2_size = 50
box2_x = 400
box2_y = 400
box2_speed = 1

# bullet 
bullets = []
bullet_speed = 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                box_color = WHITE
            if event.key == pygame.K_2:
                box_color = GREEN
            if event.key == pygame.K_3:
                box_color = BLUE
            
            if event.key == pygame.K_SPACE:
                bullet_x = box_x + 25
                bullet_y = box_y 
                bullets.append([bullet_x, bullet_y])

            if event.key == pygame.K_l:
                print("l got pressed ")
                bullet2_x = box2_x + 25
                bullet2_y = box2_y
                bullets.append([bullet2_x, bullet2_y])


    keys = pygame.key.get_pressed()
    # box 1
    if keys[pygame.K_a]:
        box_x -= box_speed
    if keys[pygame.K_w]:
        box_y -= box_speed
    if keys[pygame.K_s]:
        box_y += box_speed
    if keys[pygame.K_d]:
        box_x += box_speed

    # box 2
    if keys[pygame.K_LEFT]:
        box2_x -= box2_speed
    if keys[pygame.K_UP]:
        box2_y -= box2_speed
    if keys[pygame.K_DOWN]:
        box2_y += box2_speed
    if keys[pygame.K_RIGHT]:
        box2_x += box2_speed

    # BOX 1 BORDER LIMIT
    if box_x < 0:
        box_x = 0
    if box_x > 200:
        box_x = 200
    if box_y < 0:
        box_y = 0
    if box_y > 450:
        box_y = 450
    
    # BOX 2 BORDER LIMIT
    if box2_x < 0:
        box2_x = 0
    if box2_x > 450:
        box2_x = 450
    if box2_x == 250:
        box2_x = 251
    if box2_y < 0:
        box2_y = 0
    if box2_y > 450:
        box2_y = 450

    for bullet in bullets:
        bullet[1] -= bullet_speed

    bullet = [b for b in bullets if b[1] > 0]



    screen.fill((0,0,0))
    pygame.draw.rect(screen, box_color, (box_x, box_y, box_size, box_size))
    pygame.draw.rect(screen, box2_color, (box2_x, box2_y, box2_size, box2_size))
   

    for bullet in bullets:
        start = (bullet[0], bullet[1])
        end = (bullet[0], bullet[1] - 10)
        pygame.draw.line(screen, GREEN, start, end, 3) 

    pygame.display.flip()
