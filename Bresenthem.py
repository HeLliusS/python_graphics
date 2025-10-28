import pygame as pg

def Bresenthem(x0, y0, x1, y1):
    dots = [[x0, y0]]
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    if x1 - x0 >= 0:
        sx = 1
    else:
        sx = -1

    if y1 - y0 >= 0:
        sy = 1
    else:
        sy = -1

    e = dx - dy
    
    x = x0
    y = y0
    while x != x1 or y != y1:
        te = e * 2
        if te > -dy:
            e -= dy
            x += sx
        if te < dx:
            e += dx
            y += sy

        dots += [[x, y]] 

    return dots

def drawl(dots):
    screen = pg.display.set_mode((800, 600))
    for i in dots:
        screen.set_at(i, (255, 255, 255))

        pg.display.flip()

x0, y0, x1, y1 = map(int, input().split())

d = Bresenthem(x0, y0, x1, y1)

drawl(d)

run = True
while run: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()
