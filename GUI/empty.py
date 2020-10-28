import pygame
import time
import sys

a=pygame.display.set_mode()
a.fill((255,255,255))
img=pygame.Surface((300,300))
img.fill((255,0,0))
r=img.get_rect(center=(500,500))
print(r)

m=1
while m!=100:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    a.blit(img,r)
    pygame.display.flip()
    m+=1
    time.sleep(1)

