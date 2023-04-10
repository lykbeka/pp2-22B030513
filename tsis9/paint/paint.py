import collections,math

import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
YELLOW=pygame.Color(255,255,0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                20,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (0, 255, 0),
            (
                20,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button2(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (255, 0, 0),
            (
                60,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255, 0,0),
            (
                60,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button3C(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            RED,
            (
                760,
                300,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            RED,
            (
                760,
                300,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button4C(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            GREEN,
            (
                760,
                340,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            (
                760,
                340,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button5C(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            BLUE,
            (
                760,
                380,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            BLUE,
            (
                760,
                380,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button6E(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            YELLOW,
            (
                760,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            (
                760,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button7(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (255,128,0),
            (
                100,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255,128,0),
            (
                100,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button8(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (255,0,127),
            (
                140,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (255,0,127),
            (
                140,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button9(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (51,255,255),
            (
                180,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (51,255,255),
            (
                180,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass
class Button10(GameObject):
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(
            SCREEN,
            (76,0,153),
            (
                220,
                20,
                self.size,
                self.size,
            )
        )

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (76,0,153),
            (
                220,
                20,
                self.size,
                self.size,
            )
        )

    def update(self, current_pos):
        pass

class Eraser(GameObject):
    def __init__(self, *args, **kwargs):
        self.points: list[Point:] = []  

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                BLACK,
                start_pos=(point.x, point.y),  
                end_pos=(next_point.x, next_point.y),
                width=40
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  
class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points: list[Point:] = []  

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                COLOR,
                start_pos=(point.x, point.y), 
                end_pos=(next_point.x, next_point.y),
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos)) 


class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            COLOR,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos
class Square(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            COLOR,
            (
                start_pos_x,start_pos_y,
                end_pos_x-start_pos_x,
                end_pos_x-start_pos_x
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos
class Rtrian(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            COLOR,
            (
                (start_pos_x,start_pos_y),
                (start_pos_x,end_pos_y),
                (end_pos_x,end_pos_y)
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos
class Etrian(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            COLOR,
            (
                (start_pos_x,start_pos_y),
                (end_pos_x-math.sqrt((end_pos_x-start_pos_x)*(end_pos_x-start_pos_x)+(end_pos_y-start_pos_y)*(end_pos_y-start_pos_y)),end_pos_y),
                (end_pos_x,end_pos_y)
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos
class Romb(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.polygon(
            SCREEN,
            COLOR,
            (
                (start_pos_x,start_pos_y),
                (start_pos_x-(end_pos_x-start_pos_x),end_pos_y),
                (start_pos_x,end_pos_y+(end_pos_y-start_pos_y)),
                (end_pos_x,end_pos_y)
            ),
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Circle(GameObject):
    def __init__(self, start_pos, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  
        start_pos_y = min(self.start_pos.x, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.circle(
            SCREEN,
            COLOR,
            (  
                start_pos_x,
                start_pos_y
            ),
            math.sqrt((start_pos_x-end_pos_x)*(start_pos_x-end_pos_x)+(start_pos_y-end_pos_y)*(start_pos_y-end_pos_y)),
            width=5
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    button = Button()
    button2 =Button2()
    button3c=Button3C()
    button4c=Button4C()
    button5c=Button5C()
    button6e=Button6E()
    button7=Button7()
    button8=Button8()
    button9=Button9()
    button10=Button10()
    objects = [
        button,button2,button3c,button4c,button5c,button6e,button7,button8,button9,button10
    ]
    figures=[]
    global COLOR
    COLOR=WHITE

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    if current_shape!=Rectangle:
                        current_shape = Rectangle
                    else:
                        current_shape=Pen
                elif button2.rect.collidepoint(event.pos):
                    if current_shape!=Circle:
                        current_shape=Circle
                    else:
                        current_shape=Pen
                elif button3c.rect.collidepoint(event.pos):
                    if COLOR!=RED:
                        COLOR=RED
                    else:
                        COLOR=WHITE
                elif button4c.rect.collidepoint(event.pos):
                    if COLOR!=GREEN:
                        COLOR=GREEN
                    else:
                        COLOR=WHITE
                elif button5c.rect.collidepoint(event.pos):
                    if COLOR!=BLUE:
                        COLOR=BLUE
                    else:
                        COLOR=WHITE
                elif button6e.rect.collidepoint(event.pos):
                    if current_shape!=Eraser:
                        current_shape=Eraser
                    else:
                        current_shape=Pen
                elif button7.rect.collidepoint(event.pos):
                    if current_shape!=Square:
                        current_shape=Square
                    else:
                        current_shape=Pen
                elif button8.rect.collidepoint(event.pos):
                    if current_shape!=Rtrian:
                        current_shape=Rtrian
                    else:
                        current_shape=Pen
                elif button9.rect.collidepoint(event.pos):
                    if current_shape!=Etrian:
                        current_shape=Etrian
                    else:
                        current_shape=Pen
                elif button10.rect.collidepoint(event.pos):
                    if current_shape!=Romb:
                        current_shape=Romb
                    else:
                        current_shape=Pen
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    figures.append(active_obj)

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object
        for i in figures:
            i.draw()
        for obj in objects:
            obj.draw()

        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()