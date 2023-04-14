import pygame
import datetime
pygame.init()
w = 600
h = 400
angle1 = 0
angle2 = 0


f_sys = pygame.font.SysFont('twcen',30)
sc = pygame.display.set_mode((w,h),pygame.RESIZABLE)
pygame.display.set_caption("clock")

sc.fill((255,255,255))

mickey_surf = pygame.image.load("mickeyclock.jpg")
left_hand_surf = pygame.image.load("left_hand.png").convert_alpha()
right_hand_surf = pygame.image.load("right_hand.png").convert_alpha()

mickey_surf = pygame.transform.scale( mickey_surf ,(mickey_surf.get_width()//2.7 , mickey_surf.get_height()//2.7))
clock = pygame.time.Clock()
x=0
while True:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()
    angle1 = -t.second*6
    angle2 = -t.minute *6
    
    left_hand_surf1 = pygame.transform.rotate(left_hand_surf,x)
    right_hand_surf1 = pygame.transform.rotate(right_hand_surf,angle2)
    
    right_hand_surf1=pygame.transform.scale(right_hand_surf1,(right_hand_surf1.get_width()//1.2 ,right_hand_surf1.get_height()//1.5))
    left_hand_surf1=pygame.transform.scale(left_hand_surf1,(left_hand_surf1.get_width()//1.2 , left_hand_surf1.get_height()//1.5))
    
    mickeyrect = mickey_surf.get_rect(center = (w//2,h//2))
    left_hand_rect = left_hand_surf1.get_rect(center = (w//2,h//2))
    right_hand_rect = right_hand_surf1.get_rect(center = (w//2,h//2))
    objects=[mickey_surf,left_hand_surf1,right_hand_surf1]
    rec=[mickeyrect,left_hand_rect,right_hand_rect]
    for i in range(0,3):
        sc.blit(objects[i],rec[i])    
    x-=1
    pygame.display.update()

    clock.tick(60)

run()