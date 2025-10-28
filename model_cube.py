import pygame as pg
import math


def XTurn(d, s_r, c_r):
    return [d[0], c_r * d[1] - s_r * d[2], s_r * d[1] + c_r * d[2]]

def YTurn(d, s_r, c_r):
    return [c_r * d[0] + s_r * d[2], d[1], -s_r * d[0] + c_r * d[2]]

def ZTurn(d, s_r, c_r):
    return [c_r * d[0] - s_r * d[1], s_r * d[0] + c_r * d[1], d[2]]

def ThreeToTwo(d, c_d):
    t_d = [d[0], d[1]] 
    return [c_d[0] + t_d[0] * 100, c_d[1] + t_d[1] * 100]

def DrawPolygon(dots, norm, color = (255, 255, 255, 255)):
    if norm[2] >= 0:
        shadow = norm[2] ** (1/2)
        rcolor = [color[0] * shadow, color[1] * shadow, color[2] * shadow, 255]
        pg.draw.polygon(screen, rcolor, dots, 0)
#        pg.draw.polygon(screen, (0, 0, 0, 255), dots, 1)
    

def VectPrVect(a, b):
    return [-a[1] * b[2] + a[2] * b[1], -a[0] * b[2] + a[2] * b[0], -a[0] * b[1] + a[1] * b[0]]

def VectToNorm(a):
    l = sum([i**2 for i in a]) ** 0.5
    return [i / l for i in a]


def DefVect(d0, d1):
    return [d1[i] - d0[i] for i in range(len(d0))]

def DefCube(dots):
    poligs = [[dots[0], dots[1], dots[2], dots[3]], [dots[7], dots[6], dots[5], dots[4]], [dots[4], dots[0], dots[3], dots[7]], [dots[1], dots[5], dots[6], dots[2]], [dots[3], dots[2], dots[6], dots[7]], [dots[4], dots[5], dots[1], dots[0]]]
    norm = [VectToNorm(VectPrVect(DefVect(i[0], i[1]), DefVect(i[0], i[2]))) for i in poligs]
    return [poligs, norm]

def DefRCube(dots, c_d):
    r_poligs = [[ThreeToTwo(dots[0], c_d), ThreeToTwo(dots[1], c_d), ThreeToTwo(dots[2], c_d), ThreeToTwo(dots[3], c_d)], [ThreeToTwo(dots[7], c_d), ThreeToTwo(dots[6], c_d), ThreeToTwo(dots[5], c_d), ThreeToTwo(dots[4], c_d)], [ThreeToTwo(dots[4], c_d), ThreeToTwo(dots[0], c_d), ThreeToTwo(dots[3], c_d), ThreeToTwo(dots[7], c_d)], [ThreeToTwo(dots[1], c_d), ThreeToTwo(dots[5], c_d), ThreeToTwo(dots[6], c_d), ThreeToTwo(dots[2], c_d)], [ThreeToTwo(dots[3], c_d), ThreeToTwo(dots[2], c_d), ThreeToTwo(dots[6], c_d), ThreeToTwo(dots[7], c_d)], [ThreeToTwo(dots[4], c_d), ThreeToTwo(dots[5], c_d), ThreeToTwo(dots[1], c_d), ThreeToTwo(dots[0], c_d)]]
    return r_poligs

def DrawCube(poligs, norms, color = (255, 255, 255, 255)):
    DrawPolygon(poligs[0], norms[0], color)
    DrawPolygon(poligs[1], norms[1], color)
    DrawPolygon(poligs[2], norms[2], color)
    DrawPolygon(poligs[3], norms[3], color)
    DrawPolygon(poligs[4], norms[4], color)
    DrawPolygon(poligs[5], norms[5], color)

screen = pg.display.set_mode((800, 600))

td_c = [0, 0, 0]
rd_c = [400, 300]

td = [[1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1], [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1]]

poligs, norms = DefCube(td)
r_poligs = DefRCube(td, rd_c)

DrawCube(r_poligs, norms)

pg.display.flip()

s = input("Вокруг какой оси крутить?\n") 

while(s != "stop"): 
    if(s == "z"):
        rads = math.radians(float(input()))
        c_rads = math.cos(rads)
        s_rads = math.sin(rads)

        for i in range(len(td)):
            td[i] = ZTurn(td[i], s_rads, c_rads)

        poligs, norms = DefCube(td)
        r_poligs = DefRCube(td, rd_c)

        screen.fill((0, 0, 0))

        DrawCube(r_poligs, norms)

        pg.display.flip()
    elif(s == "y"):
        rads = math.radians(float(input()))
        c_rads = math.cos(rads)
        s_rads = math.sin(rads)

        for i in range(len(td)):
            td[i] = YTurn(td[i], s_rads, c_rads)
        
        poligs, norms = DefCube(td)
        r_poligs = DefRCube(td, rd_c)

        screen.fill((0, 0, 0))

        DrawCube(r_poligs, norms)
        
        pg.display.flip()
    elif(s == "x"):
        rads = math.radians(float(input()))
        c_rads = math.cos(rads)
        s_rads = math.sin(rads)

        for i in range(len(td)):
            td[i] = XTurn(td[i], s_rads, c_rads)
        
        poligs, norms = DefCube(td)
        r_poligs = DefRCube(td, rd_c)

        screen.fill((0, 0, 0))

        DrawCube(r_poligs, norms)

        pg.display.flip()
    elif(s == "p"):
        print(td, '\n', poligs, '\n', r_poligs, '\n', norms, sep='\n')
    else:
        print("Выбери x y z")

    s = input("Вокруг какой оси крутить?\n") 

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()