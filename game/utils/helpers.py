import pygame

def draw_text(surface, text, color, size, position):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = position
    surface.blit(text_surface, text_rect)