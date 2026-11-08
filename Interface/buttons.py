# Definition des fonctions liees aux boutons 

import pygame


def draw_buttons (screen, rect, text, color, font) : 
    pygame.draw.rect(screen, color, rect, border_radius=25)
    Text = font.render(text, True, (242, 242, 242))
    pos_text = Text.get_rect(center=rect.center)
    screen.blit(Text, pos_text)