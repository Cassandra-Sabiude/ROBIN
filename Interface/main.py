# Programme de l'interface de la tablette
import pygame

pygame.init() # Mise en route

# Creation des variables
screen = pygame.display.set_mode((800, 480))

Title_Font = pygame.font.Font(None, 55)
Text_Title1 = Title_Font.render("Hi I'm ROBIN !", True, (27, 42, 65))
Text_Title2 = Title_Font.render("Do you want to play with me ?", True, (27, 42, 65))

# Definitions des boutons
Dance_Button = pygame.Rect (50, 150, 300, 280)
Mirror_Button = pygame.Rect (450, 150, 300, 280)
Button_Font= pygame.font.Font(None, 50)
Dance_B_Text = Button_Font.render("Dance", True, (242, 242, 242))
Mirror_B_Text = Button_Font.render("Mirror", True, (242, 242, 242))

Run = True
# Boucle permettant de garder la fenetre ouverte
while Run:

    # Dessin
    screen.fill((242, 242, 242))

    x_center= screen.get_width() // 2
    Height_line = Title_Font.get_linesize()
    screen.blit(Text_Title1, Text_Title1.get_rect(midtop=(x_center, 25)))
    screen.blit(Text_Title2, Text_Title2.get_rect(midtop=(x_center, 35 + Height_line)))

    pygame.draw.rect(screen, (237, 144, 243), Dance_Button, border_radius=25)
    pos_TDB = Dance_B_Text.get_rect(center=Dance_Button.center)
    screen.blit(Dance_B_Text, pos_TDB)
    pygame.draw.rect(screen, (145, 223, 243), Mirror_Button, border_radius=25)
    pos_TMB = Mirror_B_Text.get_rect(center=Mirror_Button.center)
    screen.blit(Mirror_B_Text, pos_TMB)

    # Boucle des evenements dans la fenetre
    for evenement in pygame.event.get(): 
        if evenement.type == pygame.QUIT: # Regarde si on appui sur la croix de la fenêtre
            Run = False

        elif evenement.type == pygame.MOUSEBUTTONDOWN: # Test si bouttons cliqués
            if Dance_Button.collidepoint(evenement.pos):
                print("Dance button clicked")
            elif Mirror_Button.collidepoint(evenement.pos) :
                print("Mirror button clicked")


    pygame.display.flip()


pygame.quit() #Fermeture de la fenetre