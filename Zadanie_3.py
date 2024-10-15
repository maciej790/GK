#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)

def shutdown():
    pass

def render(deformacja, kolor):
    glClear(GL_COLOR_BUFFER_BIT)
    rysuj_prostokat(0.0, 0.0, 100.0, 50.0, deformacja, kolor)
    glFlush()

def rysuj_prostokat(x, y, a, b, d=1.0, kolor=(1.0, 1.0, 1.0)):
    # skalowanie rozmiarow na podstawie współczynnika deformacji
    przeskalowany_bok_a = a * d
    przeskalowany_bok_b = b * d

    # obliczanie współrzędnych wierzchołków prostokąta
    x1, y1 = x - przeskalowany_bok_a / 2, y - przeskalowany_bok_b / 2
    x2, y2 = x + przeskalowany_bok_a / 2, y - przeskalowany_bok_b / 2
    x3, y3 = x + przeskalowany_bok_a / 2, y + przeskalowany_bok_b / 2
    x4, y4 = x - przeskalowany_bok_a / 2, y + przeskalowany_bok_b / 2

    #ustaw kolor prostokąta
    glColor3f(kolor[0], kolor[1], kolor[2])

    #pierwszy trójkąt
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

    #drugi trójkąt
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio, 1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0, 1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    random.seed()

    # generowanie losowej deformacji i koloru
    deformacja = random.uniform(0.5, 2.0)
    kolor = (random.random(), random.random(), random.random())

    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(deformacja, kolor)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()

if __name__ == '__main__':
    main()
