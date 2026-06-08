import pygame
pygame.init()
s1 = pygame.mixer.Sound("drum.mp3")
s2 = pygame.mixer.Sound("notification.wav")
s2.play()
s1.play()
p = input()