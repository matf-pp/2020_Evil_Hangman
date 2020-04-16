import pygame

pygame.init()
visina_prozora = 650
sirina_prozora = 1000
prozor=pygame.display.set_mode((sirina_prozora, visina_prozora))

CRNA = (0, 0, 0)

slike = [pygame.image.load('il2.png'), pygame.image.load('il3.png'), pygame.image.load('il4.png'), pygame.image.load('il5.png'), pygame.image.load('il6.png'), pygame.image.load('il7.png'), pygame.image.load('il1.png')]


#ovom funkcijom iscrtavamo prozor igre
def crtanje_prozora():
    global slike
    ZUTA = (238, 232, 170)
    SVETLOZELENA=(208,240,192)
    prozor.fill(SVETLOZELENA)
    pygame.display.update()

     
igra = True

while igra:
    crtanje_prozora()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            igra = False    
    

   
pygame.quit()