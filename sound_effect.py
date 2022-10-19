import pygame

pygame.mixer.init()

pygame.mixer.music.load("music/bg_music.ogg")
pygame.mixer.music.play(-1)
laser = pygame.mixer.Sound("music/laser1.wav")
explosion = pygame.mixer.Sound("music/Explosion.wav")