import sys
import pygame
from object import Object 

class Stars:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption('Stars')

		self.bg_color = (0, 0, 102)

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.bg_color)
			self.object.blitme()

			pygame.display.flip()


if __name__ == '__main__':
	sg = Stars()
	sg.run_game()