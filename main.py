import pygame
import random as rnd
pygame.init()

class Apple():
	def __init__(self, size, cell_x, cell_y, color=[255, 0, 0]):
		self.size 	= cell_size
		self.color 	= color
		self.cell_x = cell_x
		self.cell_y = cell_y

	def generate(self):
		self.x = rnd.randint(0, self.cell_x-1)
		self.y = rnd.randint(0, self.cell_y-1)
		while ([self.x, self.y] in snake.body):
			self.x = rnd.randint(0, self.cell_x-1)
			self.y = rnd.randint(0, self.cell_y-1)

	def draw(self):
		pygame.draw.rect(screen, 
			self.color, 
			(
			 self.x*self.size, 
			 self.y*self.size, 
			 self.size, self.size
			))


		
class Snake():
	def __init__(self, cell_size, body_color=[rnd.randint(0, 255) for i in range(3)]):
		self.body 		= [[3, 0], [2, 0], [1, 0], [0, 0]] 
		self.size 		= len(self.body)
		self.body_color = body_color
		self.cell_size 	= cell_size

	def draw(self):
		for block in self.body:
			pygame.draw.rect(screen, 
				self.body_color, 
				(
				 block[0]*self.cell_size, 
				 block[1]*self.cell_size, 
				 self.cell_size, self.cell_size
				))
	
	def step(self, vector):
		if vector == "right":
			self.body.pop()
			self.body.insert(0, [self.body[0][0]+1, self.body[0][1]])
		elif vector == "left":
			self.body.pop()
			self.body.insert(0, [self.body[0][0]-1, self.body[0][1]])
		elif vector == "top":
			self.body.pop()
			self.body.insert(0, [self.body[0][0], self.body[0][1]-1])	
		elif vector == "down":
			self.body.pop()
			self.body.insert(0, [self.body[0][0], self.body[0][1]+1])

		self.check_coords()

	def append(self):
		self.body.append(snake.body[len(snake.body)-1])

	def check_coords(self):
		global game
		for i in snake.body:
			if snake.body.count(i) > 1:
				game = False
		if snake.body[0][0] > cell_x-1 or snake.body[0][0] < 0:
			game = False
		if snake.body[0][1] > cell_y-1 or snake.body[0][1] < 0:
			game = False
			

def drawWindow():
	for y in range(cell_y):
		for x in range(cell_x):
			pygame.draw.rect(screen, (239, 239, 239), (x*cell_size, y*cell_size, cell_size, cell_size))
 
	snake.step(vector)
	if [apple.x, apple.y] in snake.body:
		snake.append()
		apple.generate()
		print("Apple:  ", apple.x, " ", apple.y)
		print("Length: ", len(snake.body))
		print()

	snake.draw()
	apple.draw()
	window.blit(screen, (0, 0))
	pygame.display.update()

window_w 	= 20*20
window_h 	= 20*20
cell_x 		= 30
cell_y 		= 30
cell_size 	= 20 #px
frameCount 	= 1
clock 		= pygame.time.Clock()

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Snake")
screen = pygame.Surface((window_w, window_h))
screen.fill((209, 209, 209))

snake  = Snake(cell_size)
vector = "right"
apple = Apple(20, 20, 20)
apple.generate()
game = True
while game: 
	pygame.time.delay(60)
	if frameCount >= 10:
		frameCount = 0
	else:
		frameCount += 1
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			game = False
	
	key = pygame.key.get_pressed()
	if key[pygame.K_ESCAPE]:
		game = False

	if key[pygame.K_RIGHT] and vector != "left":
		vector = "right"
	elif key[pygame.K_LEFT] and vector != "right":
		vector = "left"
	elif key[pygame.K_UP] and vector != "down":
		vector = "top"
	elif key[pygame.K_DOWN] and vector != "top":
		vector = "down" 

	drawWindow()



pygame.quit()
