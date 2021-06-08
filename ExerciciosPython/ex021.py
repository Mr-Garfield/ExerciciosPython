'''
Projeto: Reproduzindo um arquivo MP3
'''
import pygame

pygame.mixer.init()# Inicia
pygame.mixer.music.load('Forever - Anno Domini Beats.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()