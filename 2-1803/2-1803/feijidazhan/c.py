import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,512,512)
#刷新
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=5):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed
	def update(self,*args):
		self.rect.y += self.speed
class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Hero(GameSprite):
	def __init__(self):
		super().__init__("./images/hero1.png")
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
				
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.bullets = pygame.sprite.Group()
	def update(self):
		if self.rect.y + self.rect.height <= 0:
			self.rect.y = 50
		elif self.rect.y + self.rect.height >= 512:
			self.rect.y = 450
			
		if self.moving_right == True:
			self.rect.x += 15
		elif self.moving_left == True:
			self.rect.x -= 15
		elif self.moving_up == True:
			self.rect.y -= 15
		elif self.moving_down == True:
			self.rect.y += 15
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		for i in (0,1):
			self.bullet = Bullet()
			self.bullet.rect.bottom = self.rect.y - 15*i
			self.bullet.rect.centerx = self.rect.centerx
			self.bullets.add(self.bullet)

class Enemy(GameSprite):
	def __init__(self):
		super().__init__("./images/enemy0.png")
		self.speed = random.randint(5,10)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
	
	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			print("飞机飞出屏幕")
			self.kill()
	def __del__(self):
			print("敌机摧毁%s"%self.rect)

#创建子弹精灵

class Bullet(GameSprite):
	def __init__(self):
		super().__init__("./images/bullet1.png",-7)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()
