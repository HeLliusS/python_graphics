import pygame as pg
import sys

sys.setrecursionlimit(100000000)

x0, y0 = map(int, input().split())

mx = 800
my = 600

def DrawRectangle(d1, d2, d3, d4, color = (255, 255, 255, 255)):
    pg.draw.line(screen, color, d1, d2)
    pg.draw.line(screen, color, d2, d3)
    pg.draw.line(screen, color, d3, d4)
    pg.draw.line(screen, color, d4, d1)

def Filler(x, y, new = (255, 255, 255, 255), color = None):
    if color == None:
        color = screen.get_at((x, y))
    
    screen.set_at((x, y), new)
    pg.display.flip()
    
    if x + 1 < mx and color == screen.get_at((x + 1, y)):
        Filler(x + 1, y, new, color)
    if x - 1 >= 0 and color == screen.get_at((x - 1, y)):
        Filler(x - 1, y, new, color)
    if y + 1 < my and color == screen.get_at((x, y + 1)):
        Filler(x, y + 1, new, color)
    if y - 1 >= 0 and color == screen.get_at((x, y - 1)):
        Filler(x, y - 1, new, color)

screen = pg.display.set_mode((mx, my))

DrawRectangle([100, 100], [600, 150], [530, 460], [150, 500])
pg.display.flip()

Filler(x0, y0, new = (255, 255, 255, 255))

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()