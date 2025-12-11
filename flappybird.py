import pygame,time,pyautogui,random
pygame.init()
W,H=pyautogui.size()
canvas=pygame.display.set_mode((W,H))
pygame.display.set_caption("flappy bird")
bg=pygame.transform.scale(pygame.image.load("bg.png"),(W*1.5,H*(3/4)))
sw,sh=70,70
ground=pygame.transform.scale(pygame.image.load("ground.png"),(W*1.5,H/4))
scroll=0
speed=4
flying=False
gameover=False
class Bird(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.images=[]
          for i in range(3):
               image=pygame.image.load(f"bird{i+1}.png")
               self.images.append(image)
          self.index=0 
          self.image=self.images[self.index]
          self.rect=self.image.get_rect()
          self.rect.center=100,H/2
          self.counter=0
          self.velocity=0

     def update(self):
          
          if flying:
               if pygame.mouse.get_pressed()[0]:
                    print("hello")
                    self.velocity=-10
               self.velocity+=0.2
               if self.velocity>8:
                    self.velocity=8
               if self.rect.y<H*3/4-30:  
                    self.rect.y+=self.velocity
               self.counter+=1
               if self.counter==5:
                    self.counter=0
                    self.index+=1
                    if self.index>2:
                         self.index=0
               self.image=self.images[self.index]
          
bird=pygame.sprite.Group()
flappy=Bird()
bird.add(flappy)
while True:
    #canvas.fill("white")
     canvas.blit(bg,(scroll,0))
     canvas.blit(ground,(scroll,H*3/4))
     bird.draw(canvas)
     flappy.update()
     scroll-=speed
     if scroll<-200:
          scroll=0
     for i in pygame.event.get():
               if i.type==pygame.QUIT:
                    pygame.quit()

     if not gameover and not flying and pygame.mouse.get_pressed()[0]:
          flying=True
     pygame.display.update()

