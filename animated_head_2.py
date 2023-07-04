import pygame,time
import sys,math
import pyttsx
from pygame import gfxdraw


PI = math.pi
pygame.init()
screen = pygame.display.set_mode((640, 480))
back = (255,255,255)
color = (255,255,0)
mouth_flag = False
import threading


engine = pyttsx.init()
engine.say('Good morning.')
while True:
  time.sleep( 0.25 )
  screen.fill(back)
  pygame.gfxdraw.filled_circle(screen,320,240,100,color)
  pygame.gfxdraw.filled_circle(screen,270,210,20,(0,0,0))
  pygame.gfxdraw.filled_circle(screen,370,210,20,(0,0,0))
  if mouth_flag==False:
   pygame.gfxdraw.arc(screen,320,240,75,25, 155, (0,0,0))
   mouth_flag=True
  else:
   pygame.gfxdraw.line(screen,270,290,370,290,(0,0,0))
   mouth_flag=False
if __name__ == "__main__":
    t1 = threading.Thread(target = pygame.display.update, args = () )
    t2 = threading.Thread(target=engine.runAndWait, args=())

    t1.start()

    t2.start()

    t1.join()
    t2.join
