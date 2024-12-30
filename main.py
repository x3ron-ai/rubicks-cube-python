import sys
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from rubick import RCube
import time 
pygame.init()
cube = RCube()
display = (1200, 800)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

glEnable(GL_DEPTH_TEST)

gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

colors = {
	'red':(1,0,0),
	'green':(0,1,0),
	'blue':(0,0,1),
	'white':(1,1,1),
	'yellow':(1,1,0),
	'orange':(1,0.5,0)
}

angle_x = 0
angle_y = 0
mouse_x = 0
mouse_y = 0
is_dragging = False
shift_pressed = False
hh = False
def draw_cube():
	global hh
	glBegin(GL_QUADS)
	sites = cube.get_sites()
	glColor3f(.1,.1,.1)
	# u
	glVertex3f(-1, .99, -1)
	glVertex3f(1, .99, -1)
	glVertex3f(1, .99, 1)
	glVertex3f(-1, .99, 1)
	# f
	glVertex3f(-1, 1, .99)
	glVertex3f(1, 1, .99)
	glVertex3f(1, -1, .99)
	glVertex3f(-1, -1, .99)
	# r
	glVertex3f(.99, 1, 1)
	glVertex3f(.99, 1, -1)
	glVertex3f(.99, -1, -1)
	glVertex3f(.99, -1, 1)
	# d
	glVertex3f(-1, -.99, -1)
	glVertex3f(1, -.99, -1)
	glVertex3f(1, -.99, 1)
	glVertex3f(-1, -.99, 1)
	# b
	glVertex3f(-1, 1, -.99)
	glVertex3f(1, 1, -.99)
	glVertex3f(1, -1, -.99)
	glVertex3f(-1, -1, -.99)
	# l
	glVertex3f(-.99, 1, 1)
	glVertex3f(-.99, 1, -1)
	glVertex3f(-.99, -1, -1)
	glVertex3f(-.99, -1, 1)


	for site_index in range(6):
		site = sites[site_index]
		for j in range(9):
			y = j // 3 # тут по идее ряд
			i = j % 3 # тут по идее колонка
			fragment_color = site.fragments[j].color

			glColor3f(*colors[fragment_color])

			# чекаем в какую грань идет фрагмент
			if site_index == 0: # top
				x_start = -1 + (i*2/3)+0.05
				x_end = x_start + (2/3)-0.1
				y_start = -1 + (y*2/3)+0.05
				y_end = y_start + (2/3)-0.1
				glVertex3f(x_start, 1, y_start)
				glVertex3f(x_end, 1, y_start)
				glVertex3f(x_end, 1, y_end)
				glVertex3f(x_start, 1, y_end)
			elif site_index == 1: # front
				x_start = -1 + (i*2/3)+0.05
				x_end = x_start + (2/3)-0.1
				y_start = -1 + (y*2/3)+0.05
				y_end = y_start + (2/3)-0.1
				glVertex3f(x_start, -y_start, 1)
				glVertex3f(x_end, -y_start, 1)
				glVertex3f(x_end, -y_end, 1)
				glVertex3f(x_start, -y_end, 1)
			elif site_index == 2: # right
				x_start = -1 + (i*2/3)+0.05
				x_end = x_start + (2/3)-0.1
				y_start = -1 + (y*2/3)+0.05
				y_end = y_start + (2/3)-0.1
				glVertex3f(1, -y_start, -x_end)
				glVertex3f(1, -y_start, -x_start)
				glVertex3f(1, -y_end, -x_start)
				glVertex3f(1, -y_end, -x_end)
			elif site_index == 3: # back
				x_start = -1 + (i*2/3)+0.05
				x_end = x_start + (2/3)-0.1
				y_start = -1 + (y*2/3)+0.05
				y_end = y_start + (2/3)-0.1
				glVertex3f(-x_start, -y_start, -1)
				glVertex3f(-x_end, -y_start, -1)
				glVertex3f(-x_end, -y_end, -1)
				glVertex3f(-x_start, -y_end, -1)
			elif site_index == 4: # left
				x_start = -1 + (i*2/3)+0.05
				x_end = x_start + (2/3)-0.1
				y_start = -1 + (y*2/3)+0.05
				y_end = y_start + (2/3)-0.1
				glVertex3f(-1, -y_start, x_start)
				glVertex3f(-1, -y_start, x_end)
				glVertex3f(-1, -y_end, x_end)
				glVertex3f(-1, -y_end, x_start)
			elif site_index == 5: # down
				x_start = -1 + (y*2/3)+0.05
				x_end = x_start + (2/3)-0.1
				y_start = -1 + (i*2/3)+0.05
				y_end = y_start + (2/3)-0.1
				glVertex3f(x_start, -1, y_start)
				glVertex3f(x_end, -1, y_start)
				glVertex3f(x_end, -1, y_end)
				glVertex3f(x_start, -1, y_end)
				if not hh:
					print(x_start, y_start)
				if j == 8:
					hh = True

	
	glEnd()

def main():
	global angle_x, angle_y, mouse_x, mouse_y, is_dragging, shift_pressed

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					is_dragging = True
					mouse_x, mouse_y = event.pos 

			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					is_dragging = False

			if event.type == pygame.MOUSEMOTION:
				if is_dragging:
					dx = event.pos[0] - mouse_x
					dy = event.pos[1] - mouse_y 

					angle_x += dy * 0.1
					angle_y += dx * 0.1

					mouse_x, mouse_y = event.pos

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
					shift_pressed = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					cube.make_r_move(shift_pressed)
				elif event.key == pygame.K_l:
					cube.make_l_move(shift_pressed)
				elif event.key == pygame.K_f:
					cube.make_f_move(shift_pressed)
				elif event.key == pygame.K_u:
					cube.make_u_move(shift_pressed)
				elif event.key == pygame.K_d:
					cube.make_d_move(shift_pressed)
				elif event.key == pygame.K_b:
					cube.make_b_move(shift_pressed)

				if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
					shift_pressed = True
				print(cube.cool_show())

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		glPushMatrix()

		glRotatef(angle_x, 1, 0, 0)
		glRotatef(angle_y, 0, 1, 0)

		draw_cube()

		glPopMatrix()

		pygame.display.flip()
		pygame.time.wait(10)

if __name__ == "__main__":
	main()
