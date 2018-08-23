import sys, pygame
pygame.init()

tamanho      =   largura, altura = 400, 640
velocidade   =   [1, 1]
preto	     =   0, 0, 0

tela         =   pygame.display.set_mode(tamanho)
bola         =   pygame.image.load("bola.bmp")
posicao_bola =   bola.get_rect()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                        sys.exit()

        posicao_bola = posicao_bola.move(velocidade)

        if (posicao_bola.left < 0) or (posicao_bola.right > largura):
                velocidade[0] = -velocidade[0]
        
        if (posicao_bola.top < 0)  or (posicao_bola.bottom > altura):
                velocidade[1] = -velocidade[1]

        tela.fill(preto)
        tela.blit(bola, posicao_bola)
        pygame.display.flip()