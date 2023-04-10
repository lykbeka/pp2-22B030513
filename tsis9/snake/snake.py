import random,time,sys
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
YELLOW=(255,255,0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
BROWN=(139,69,19)
clock = pygame.time.Clock()
SPD=5
LEVEL=1
SCORE=0
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        
        
        
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )
            
    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy
    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    def coll(self):
        head1=pygame.Rect(
                self.body[0].x * BLOCK_SIZE,
                self.body[0].y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        if head1.colliderect(r_t):
            return True
        elif head1.colliderect(r_r):
            return True
        elif head1.colliderect(r_l):
            return True
        elif head1.colliderect(r_b):
            return True
        return False
    def fcoll(self,food):
        for i in range(1,len(self.body)-1):
            if food.location.x != self.body[i].x:
                continue
            if food.location.y != self.body[i].y:
                continue
            return True
        return False


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)
r_t=pygame.Rect(0,0,800,40)
r_l=pygame.Rect(0,40,40,720)
r_r=pygame.Rect(760,40,40,720)
r_b=pygame.Rect(0,760,800,40)
class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)
        global F
        self.ran=random.randint(1,3)
        F=self.ran
    def draw(self):
        if self.ran==1:
            pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
            )
        elif self.ran==2:
            pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
            )
        else:
            pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
            )
    def spwn(self):
        self.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
        self.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    pygame.time.set_timer(pygame.USEREVENT,5000)

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
            if event.type ==pygame.USEREVENT:
                food.spwn()
                while snake.fcoll(food):
                    food.spwn()
                food.__init__(food.location.x ,food.location.y)
                pygame.time.set_timer(pygame.USEREVENT,5000)
        snake.move(dx, dy)
        global SCORE,SPD,LEVEL
        score=font_small.render("SCORE:"+str(SCORE), True, WHITE)
        level=font_small.render("LEVEL:"+str(LEVEL), True, WHITE)
        game_over = font.render("Game Over",True, WHITE)
        
        if snake.coll():
            time.sleep(1)
                   
            SCREEN.fill(RED)
            SCREEN.blit(game_over, (220,300))
          
            pygame.display.update()
          
            time.sleep(2)
            pygame.quit()
            sys.exit()  
        
        
        
        if snake.check_collision(food):    
            for i in range(1,F+1):
                SCORE+=1
                snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
                )      
            food.spwn()
            while snake.fcoll(food):
                food.spwn()
            food.__init__(food.location.x ,food.location.y)
            pygame.time.set_timer(pygame.USEREVENT,5000)
            if SCORE>=LEVEL*4:
                LEVEL+=1
                SPD+=1
        pygame.draw.rect(SCREEN,BROWN,r_t)
        pygame.draw.rect(SCREEN,BROWN,r_l)
        pygame.draw.rect(SCREEN,BROWN,r_r)
        pygame.draw.rect(SCREEN,BROWN,r_b)
        SCREEN.blit(score,(10,10))
        SCREEN.blit(level,(200,10))   
        

        snake.draw()
        food.draw()
        draw_grid()
        pygame.display.flip()
        clock.tick(SPD)


if __name__ == '__main__':
    main()