import pygame
import time
import random
pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
pygame.display.set_caption("Pokémon Dodge")
icone = pygame.image.load("assets/pikachuicon.png")
pygame.display.set_icon(icone)
pikachu = pygame.image.load("assets/pikachu2.png")
larguraPikachu = 105
fundo = pygame.image.load("assets/cidade_pallet.png")
pokeball = pygame.image.load("assets/pokebola.png")
capturadoSound = pygame.mixer.Sound("assets/pikachu_scream.mp3")
capturadoSound.set_volume(0.04)
pikachuSound = pygame.mixer.Sound("assets/pikachuSound.mp3")
pikachuSound.set_volume(0.1)
descargaSound = pygame.mixer.Sound("assets/descarga.mp3")
descargaSound.set_volume(0.1)
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
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render("Desvios:"+str(contador), True, black)
    gameDisplay.blit(texto, (55, 55))
def dead():
    pygame.mixer.Sound.play(pikachuSound)
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(capturadoSound)
    pygame.mixer.music.stop()
    escreverTela("Você foi capturado!")
def game():
    pygame.mixer.music.load("assets/pokemonbattle.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    pikachuPosicaoX = largura*0.42
    pikachuPosicaoY = altura*0.8
    movimentoX = 0
    velocidade = 20
    pokeballAltura = 140
    pokeballLargura = 140
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