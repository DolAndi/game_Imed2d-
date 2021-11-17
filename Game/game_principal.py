import pygame
import time
import random
pygame.init()
largura = 736
altura = 669
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Pokémon Dodge")
icone = pygame.image.load("assets2/pikachuicon.png")
pygame.display.set_icon(icone)
pikachu = pygame.image.load("assets2/pikachu2.png")
larguraPikachu = 110
fundo = pygame.image.load("assets2/cidade_pallet.png")
pokeball = pygame.image.load("assets2/pokeball2.jpg")
capturadoSound = pygame.mixer.Sound("assets2/pikachu_scream.mp3")
descargaSound = pygame.mixer.Sound("assets2/descarga.mp3")
descargaSound.set_volume(0.2)

def mostraPikachu(x, y):
    gameDisplay.blit(pikachu, (x, y))
def mostraPokeball(x, y):
    gameDisplay.blit(pokeball, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Desvios:"+str(contador), True, white)
    gameDisplay.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(capturadoSound)
    pygame.mixer.music.stop()
    escreverTela("Você Morreu!")

def game():
    pygame.mixer.music.load("assets2/pokemonbattle.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    ironPosicaoX = largura*0.2
    ironPosicaoY = altura*0.2
    movimentoX = 0
    velocidade = 15
    misselAltura = 25
    misselLargura = 25
    misselVelocidade = 3
    misselX = random.randrange(0, largura)
    misselY = -200
    desvios = 0
    pygame.mixer.Sound.play(descargaSound)
    while True:
        # pega as ações da tela. Ex.: fechar, click de uma tecla ou do mouse
        acoes = pygame.event.get()  # devolve uma lista de ações
        # [ini] mapeando as ações
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
        # [end] mapeando as ações
        # definindo o fundo do game
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        # definindo o fundo do game]
        escreverPlacar(desvios)
        misselY = misselY + misselVelocidade
        mostraPokeball(misselX, misselY)
        if misselY > altura:
            misselY = -200
            misselX = random.randrange(0, largura)
            desvios = desvios+1
            misselVelocidade += 3
            pygame.mixer.Sound.play(descargaSound)
        ironPosicaoX += movimentoX
        if ironPosicaoX < 0:
            ironPosicaoX = 0
        elif ironPosicaoX > largura-larguraPikachu:
            ironPosicaoX = largura-larguraPikachu
        # analise de colisão com o IronMan
        if ironPosicaoY < misselY + misselAltura:
            if ironPosicaoX < misselX and ironPosicaoX+larguraPikachu > misselX or misselX+misselLargura > ironPosicaoX and misselX+misselLargura < ironPosicaoX+larguraPikachu:
                dead()
        # analise de colisão com o IronMan
        mostraPikachu(ironPosicaoX, ironPosicaoY)
        pygame.display.update()
        clock.tick(60)  # faz com que o while execute 60x por segundo
game()
