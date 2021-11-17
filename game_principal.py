import pygame
import time
import random
pygame.init()
largura = 736
altura = 669
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)
pygame.display.set_caption("Pokémon Dodge")
icone = pygame.image.load("assets/pikachuicon.png")
pygame.display.set_icon(icone)
pikachu = pygame.image.load("assets/pikachu2.png")
larguraPikachu = 256
fundo = pygame.image.load("assets/cidade_pallet.png")
pokeball = pygame.image.load("assets/pokeball2.jpg")
capturadoSound = pygame.mixer.Sound("assets/pikachu_scream.mp3")
descargaSound = pygame.mixer.Sound("assets/descarga.mp3")
descargaSound.set_volume(0.2)
nomeJogador = str(input("Insira o seu nome: "))
emailJogador = str(input("Insira o seu email: "))
arquivo = open("historico.txt", "a")
arquivo.write("Participante: " + nomeJogador + " email: " + emailJogador + "\n")
def mostraPikachu(x, y):
    gameDisplay.blit(pikachu, (x, y))
def mostraPokeball(x, y):
    gameDisplay.blit(pokeball, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, red)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 70)
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
    escreverTela("Você foi capturado!")
def game():
    pygame.mixer.music.load("assets/pokemonbattle.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    pikachuPosicaoX = largura*0.2
    pikachuPosicaoY = altura*0.62
    movimentoX = 0
    velocidade = 15
    pokeballAltura = 10
    pokeballLargura = 10
    pokeballVelocidade = 3
    pokeballX = random.randrange(0, largura)
    pokeballY = -200
    desvios = 0
    pygame.mixer.Sound.play(descargaSound)
    while True:
        acoes = pygame.event.get() 
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
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        escreverPlacar(desvios)
        pokeballY = pokeballY + pokeballVelocidade
        mostraPokeball(pokeballX, pokeballY)
        if pokeballY > altura:
            pokeballY = -200
            pokeballX = random.randrange(0, largura)
            desvios = desvios+1
            pokeballVelocidade += 3
            pygame.mixer.Sound.play(descargaSound)
        pikachuPosicaoX += movimentoX
        if pikachuPosicaoX < 0:
            pikachuPosicaoX = 0
        elif pikachuPosicaoX > largura-larguraPikachu:
            pikachuPosicaoX = largura-larguraPikachu
        if pikachuPosicaoY < pokeballY + pokeballAltura:
            if pikachuPosicaoX < pokeballX and pikachuPosicaoX+larguraPikachu > pokeballX or pokeballX+pokeballLargura > pikachuPosicaoX and pokeballX+pokeballLargura < pikachuPosicaoX+larguraPikachu:
                dead()
        mostraPikachu(pikachuPosicaoX, pikachuPosicaoY)
        pygame.display.update()
        clock.tick(60) 
game()