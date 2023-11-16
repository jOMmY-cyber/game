import pygame 
from player import rect 
import random
from ball import ball
import time
pygame.init()
#ra = rect(5,10,3,2) 
screen = pygame.display.set_mode((300,300))
ball1 = ball(screen,(255,0,0))
ball2 = ball(screen,(255,255,100))
ball3 = ball(screen,(0,0,255))
clk= pygame.time.Clock()
run = True
score = 0
start = time.time()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
combo = 0
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    mou = pygame.mouse.get_pos()
    x,y = mou
    rand = random.randint(0,300)

  

    screen.fill((255,200,255))
    x = x-25
    
    player = pygame.Rect(x,250,50,10)
    xmin = x
    xmax = x+50
    score,combo = ball1.checkhit( xmin, xmax, score,combo)
    # score,combo = ball2.checkhit( xmin, xmax, score,combo)
    # score,combo = ball3.checkhit( xmin, xmax, score,combo)
    ball1.draw()
    # ball2.draw()
    # ball3.draw()
    if combo >0:
        text = myfont.render('combo'+str(combo), False, (0, 0, 0))
    else : text = myfont.render('', False, (0, 0, 0))
    
    screen.blit(text,(200,10))
    pygame.draw.rect(screen, (255,255,0),player )
    clk.tick(60)
    pygame.display.update()
    if time.time()-start > 15:
        print('your score =',score)
        run = False       