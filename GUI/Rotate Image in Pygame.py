import pygame, sys
from PIL import Image, ImageTk
def rotate(surface,angle):
    rota=pygame.transform.rotozoom(surface,angle,1)
    rec=rota.get_rect(center=(200,500))
    return rota,rec

clock=pygame.time.Clock()
screen=pygame.display.set_mode((0,0),pygame.RESIZABLE)


img=pygame.image.load("pen.png")
img = pygame.transform.scale(img, (90, 90))

angle=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    angle+=1
    screen.fill((255,255,255))
    img_rot,img_rot_rec=rotate(img,angle)

    screen.blit(img_rot,img_rot_rec)
    pygame.display.flip()
    clock.tick(30)



