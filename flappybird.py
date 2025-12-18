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
pipegap=200
pipe_frequency=3000
lastPipe=pygame.time.get_ticks()-pipe_frequency

class Pipe(pygame.sprite.Sprite):
     def __init__(self,x,y,pos):
          super().__init__()
          self.image=pygame.image.load("pipe.png")
          self.rect=self.image.get_rect()
          if pos=="top":
               self.image=pygame.transform.flip(self.image,False,True)
               self.rect.bottomleft=[x,y-pipegap/2]
          if pos=="bottom":
               self.rect.topleft=[x,y+pipegap/2]
     def update(self):
          self.rect.x-=speed
          if self.rect.right<0:
               self.kill()


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
pipe_group=pygame.sprite.Group()
bird=pygame.sprite.Group()
flappy=Bird()
bird.add(flappy)
while True:
    #canvas.fill("white")
     #print(pygame.time.get_ticks())
     canvas.blit(bg,(scroll,0))
     canvas.blit(ground,(scroll,H*3/4))
     bird.draw(canvas)
     pipe_group.draw(canvas)

     flappy.update()
     scroll-=speed
     if scroll<-200:
          scroll=0
     if flying and not gameover:
          timeNow=pygame.time.get_ticks()
          if timeNow-lastPipe>3000:
               pipeHeight=random.randint(-100,100)
               bpipe=Pipe(W,H/2+pipeHeight,"bottom")
               tpipe=Pipe(W,H/2+pipeHeight,"top")
               pipe_group.add(bpipe)
               pipe_group.add(tpipe)
               lastPipe=timeNow
          pipe_group.update()

     for i in pygame.event.get():
               if i.type==pygame.QUIT:
                    pygame.quit()

     if not gameover and not flying and pygame.mouse.get_pressed()[0]:
          flying=True
     pygame.display.update()

