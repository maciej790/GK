#!/usr/bin/env python3
import sys
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)

def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    rysuj_prostokat(0.0, 0.0, 100.0, 50.0)  # rysowanie pojedynczego prostokąt

    glFlush()

def rysuj_prostokat(x, y, a, b): # prostokąt rysowany z 2-óch trójkątow
    # punkty narożne prostokąta
    polowka_a = a / 2
    polowka_b = b / 2

    # Pierwszy trójkąt
    glColor3f(0.0, 1.0, 0.0)  # Zielony
    glBegin(GL_TRIANGLES)
    glVertex2f(x - polowka_a, y - polowka_b)  # Dolny lewy róg
    glVertex2f(x + polowka_a, y - polowka_b)  # Dolny prawy róg
    glVertex2f(x - polowka_a, y + polowka_b)  # Górny lewy róg
    glEnd()

    # Drugi trójkąt
    glColor3f(1.0, 0.0, 0.0)  # Czerwony
    glBegin(GL_TRIANGLES)
    glVertex2f(x + polowka_a, y - polowka_b)  # Dolny prawy róg
    glVertex2f(x + polowka_a, y + polowka_b)  # Górny prawy róg
    glVertex2f(x - polowka_a, y + polowka_b)  # Górny lewy róg
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
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()

if __name__ == '__main__':
    main()
