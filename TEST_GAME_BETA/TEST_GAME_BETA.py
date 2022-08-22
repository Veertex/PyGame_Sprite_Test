import time
import sys
import pygame
from pygame import sprite
from pygame.locals import *

###########################################################
# CLASE ANIMACION_PERSONAJE
###########################################################

class animacion_personaje():
    def __init__(self, nombre_animacion, sprites_animacion=[]):
        self.nombre_animacion=nombre_animacion
        self.sprites_animacion=sprites_animacion
        
sprites_animacion_jugador_atacando=[]
sprites_animacion_jugador_atacando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_ATAQUE_FINAL/PLAYER_ATAQUE_FINAL0.png"))
sprites_animacion_jugador_atacando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_ATAQUE_FINAL/PLAYER_ATAQUE_FINAL1.png"))
sprites_animacion_jugador_atacando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_ATAQUE_FINAL/PLAYER_ATAQUE_FINAL2.png"))
sprites_animacion_jugador_atacando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_ATAQUE_FINAL/PLAYER_ATAQUE_FINAL3.png"))

animacion_jugador_atacando=animacion_personaje("animacion_jugador_atacando",sprites_animacion_jugador_atacando)

sprites_animacion_jugador_saltando=[]
sprites_animacion_jugador_saltando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_SALTO_FINAL/PLAYER_SALTO_FINAL0.png"))
sprites_animacion_jugador_saltando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_SALTO_FINAL/PLAYER_SALTO_FINAL1.png"))

animacion_jugador_saltando=animacion_personaje("animacion_jugador_saltando",sprites_animacion_jugador_saltando)


sprites_animacion_jugador_caminando=[]
sprites_animacion_jugador_caminando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_MOV_FINAL/PLAYER_MOV_FINAL0.png"))
sprites_animacion_jugador_caminando.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_MOV_FINAL/PLAYER_MOV_FINAL1.png"))

animacion_jugador_caminando=animacion_personaje("animacion_jugador_caminando",sprites_animacion_jugador_caminando)

sprites_animacion_jugador_quieto=[]
sprites_animacion_jugador_quieto.append(pygame.image.load("C:/Users/Veertex/Desktop/TEST_GAME_BETA/PLAYER_SPRITES/PLAYER_STATIC_FINAL/PLAYER_STATIC_FINAL0.png"))

animacion_jugador_quieto=animacion_personaje("animacion_jugador_quieto",sprites_animacion_jugador_quieto)

###########################################################
# CLASE ESTADO_JUGADOR
###########################################################

class estado_personaje():
    def __init__(self, nombre_estado, animacion_estado_jugador=[]):
        self.estado_activado=False
        self.nombre_estado=nombre_estado
        self.animacion_estado_jugador=animacion_estado_jugador

estado_jugador_atacando=estado_personaje("estado_jugador_atacando",animacion_jugador_atacando)
estado_jugador_saltando=estado_personaje("estado_jugador_saltando",animacion_jugador_saltando)
estado_jugador_caminando=estado_personaje("estado_jugador_caminando",animacion_jugador_caminando)
estado_jugador_quieto=estado_personaje("estado_jugador_quieto",animacion_jugador_quieto)

estados_jugador=[]
estados_jugador.append(estado_jugador_atacando)
estados_jugador.append(estado_jugador_saltando)
estados_jugador.append(estado_jugador_caminando)
estados_jugador.append(estado_jugador_quieto)

###########################################################
# CLASE JUGADOR
###########################################################

class jugador(pygame.sprite.Sprite):
    def __init__(self,estados_jugador=[]):
        super().__init__()
        self.estados_jugador=estados_jugador
        self.estado_jugador=self.estados_jugador[3]
        self.index_sprite=0
        self.image=self.estado_jugador.animacion_estado_jugador.sprites_animacion[self.index_sprite]
        self.rect=self.image.get_rect()

    def update(self):
        
        if self.index_sprite<len(self.estado_jugador.animacion_estado_jugador.sprites_animacion):
            self.image=pygame.transform.scale(self.estado_jugador.animacion_estado_jugador.sprites_animacion[self.index_sprite],(200,175))
            self.index_sprite+=1
        else:
            self.estado_jugador=self.estados_jugador[3]
            self.index_sprite=0

pygame.init()
ventana = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
pygame.display.set_caption("PYGAME_TEST - TITULO DE VENTANA")
color_rgb=pygame.Color(31, 133, 29)
jugador_1=jugador(estados_jugador)
sprites_en_pantalla=pygame.sprite.Group()




while True:
    pygame.time.delay(45)
    for condicion_salida in pygame.event.get():

        if condicion_salida.type==QUIT:
            pygame.quit()
            sys.exit()

        if condicion_salida.type==pygame.KEYDOWN:
            if condicion_salida.key==pygame.K_LEFT:
                jugador_1.estado_jugador=jugador_1.estados_jugador[2]
                jugador_1.index_sprite=0
        if condicion_salida.type==pygame.KEYDOWN:
            if condicion_salida.key==pygame.K_RIGHT:
                jugador_1.estado_jugador=jugador_1.estados_jugador[2]
                jugador_1.index_sprite=0
        if condicion_salida.type==pygame.KEYDOWN:
            if condicion_salida.key==pygame.K_d:
                jugador_1.estado_jugador=jugador_1.estados_jugador[0]
                jugador_1.index_sprite=0
        if condicion_salida.type==pygame.KEYDOWN:
            if condicion_salida.key==pygame.K_s:
                #jugador_1.estado_jugador=jugador_1.estados_jugador[0]
                #jugador_1.index_sprite=0
                print
        if condicion_salida.type==pygame.KEYDOWN:
            if condicion_salida.key==pygame.K_a:
                #jugador_1.estado_jugador=jugador_1.estados_jugador[0]
                #jugador_1.index_sprite=0
                print

    ventana.fill(color_rgb)
    sprites_en_pantalla.add(jugador_1)
    sprites_en_pantalla.draw(ventana)
    sprites_en_pantalla.update()
    pygame.display.update()









