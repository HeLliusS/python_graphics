import pygame as pg
import math


def XTurn(d, s_r, c_r):
    return [d[0], c_r * d[1] - s_r * d[2], s_r * d[1] + c_r * d[2]]

def YTurn(d, s_r, c_r):
    return [c_r * d[0] + s_r * d[2], d[1], -s_r * d[0] + c_r * d[2]]

def ZTurn(d, s_r, c_r):
    return [c_r * d[0] - s_r * d[1], s_r * d[0] + c_r * d[1], d[2]]


def DrawPolygon(dots, color = (255, 255, 255, 255)):
    rd = [[dots[0][0] * 100, dots[0][1] * 100], [dots[1][0] * 100, dots[1][1] * 100], [dots[2][0] * 100, dots[2][1] * 100], [dots[3][0] * 100, dots[3][1] * 100]]
    pg.draw.aalines(screen, color, False, rd + [rd[0]])

def DefCube(dots):
    pols = [[dots[0], dots[1], dots[5], dots[4]], [dots[1], dots[2], dots[6], dots[5]], [dots[2], dots[3], dots[7], dots[6]], [dots[3], dots[0], dots[4], dots[7]], [dots[4], dots[5], dots[6], dots[7]], [dots[0], dots[1], dots[2], dots[3]]]
    return pols

def DrawCube(pols, color = (255, 255, 255, 255)):
    DrawPolygon(pols[0], color)
    DrawPolygon(pols[1], color)
    DrawPolygon(pols[2], color)
    DrawPolygon(pols[3], color)
    DrawPolygon(pols[4], (255, 0, 0))
    DrawPolygon(pols[5], (0, 0, 255))

screen = pg.display.set_mode((800, 600))

td_c = [0, 0, 0]



td = [[1.4142135623730951, 1.0, 0.0], [0.0, 1.0, 1.4142135623730951], [0.0, -1.0, 1.4142135623730951], [1.4142135623730951, -1.0, 0.0], [0.0, 1.0, -1.4142135623730951], [-1.4142135623730951, 1.0, 0.0], [-1.4142135623730951, -1.0, 0.0], [0.0, -1.0, -1.4142135623730951]]

pols = DefCube(td)

DrawCube(pols)

pg.display.flip()

s = input("Вокруг какой оси крутить?\n") 

while(s != "stop"): 
    if(s == "z"):
        rads = math.radians(float(input()))
        c_rads = math.cos(rads)
        s_rads = math.sin(rads)

        for i in range(len(td)):
            td[i] = ZTurn(td[i], s_rads, c_rads)
        
        pols = DefCube(td)

        screen.fill((0, 0, 0))

        DrawCube(pols)

        pg.display.flip()
    elif(s == "y"):
        rads = math.radians(float(input()))
        c_rads = math.cos(rads)
        s_rads = math.sin(rads)

        for i in range(len(td)):
            td[i] = YTurn(td[i], s_rads, c_rads)

        pols = DefCube(td)

        screen.fill((0, 0, 0))

        DrawCube(pols)

        pg.display.flip()
    elif(s == "x"):
        rads = math.radians(float(input()))
        c_rads = math.cos(rads)
        s_rads = math.sin(rads)

        for i in range(len(td)):
            td[i] = XTurn(td[i], s_rads, c_rads)

        pols = DefCube(td)

        screen.fill((0, 0, 0))
        
        DrawCube(td)

        pg.display.flip()
    elif(s == "p"):
        print(td, sep='\n')
    else:
        print("Выбери x y z")

    s = input("Вокруг какой оси крутить?\n") 

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()