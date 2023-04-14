import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
pygame.draw.circle (screen,(200,0,0),(30,30),25)
x=30
y=30
clock=pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y>=50:
               y-=20
        if pressed[pygame.K_DOWN] and y<=550:
               y+=20
        if pressed[pygame.K_LEFT] and x>=50:
               x-=20
        if pressed[pygame.K_RIGHT] and x<=750:
               x+=20
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(200,0,0),(x,y),25)
        

        pygame.display.flip()
        clock.tick(60)