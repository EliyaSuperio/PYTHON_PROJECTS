import pygame 

pygame.init()

pygame.display.set_caption("circle game")
screen = pygame.display.set_mode((800,600))

circler = 40 
circlex = 200
circley = 200
circle_speed = 1
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circlex -= circle_speed
    if keys[pygame.K_RIGHT]:
        circlex += circle_speed
    if keys[pygame.K_UP]:
        circley -= circle_speed
    if keys[pygame.K_DOWN]:
        circley += circle_speed


    if circlex < 40:
        circlex = 40
    if circlex > 760:
        circlex = 760
    if circley < 40:
        circley = 40
    if circley > 560:
        circley = 560
    screen.fill((255,255,255))

#   pygame.draw.circle(surface, color, (x, y), radius)
    pygame.draw.circle(screen, (0, 255, 0), (circlex, circley), circler)

    pygame.display.flip()
