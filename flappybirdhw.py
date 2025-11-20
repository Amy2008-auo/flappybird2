import pygame,time,pyautogui,random
pygame.init()
W,H=pyautogui.size()
canvas=pygame.display.set_mode((W,H))
pygame.display.set_caption("under the sea")
bg=pygame.transform.scale(pygame.image.load("sea.jpg"),(W*1.5,H*(3/4)))
sw,sh=70,70
ground=pygame.transform.scale(pygame.image.load("seaground.jpg"),(W*1.5,H/4))
scroll=0
speed=4

while True:
    #canvas.fill("white")
    canvas.blit(bg,(scroll,0))
    canvas.blit(ground,(scroll,H*3/4))
    scroll-=speed
    if scroll<-200:
        scroll=0
    for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()


    pygame.display.update()

