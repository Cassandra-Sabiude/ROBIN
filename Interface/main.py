# Programme de l'interface de la tablette
import pygame
import buttons

pygame.init() # Mise en route

# Creation des variables
screen = pygame.display.set_mode((800, 480))
page = "home"

Title_Font = pygame.font.Font(None, 55)
Text_Title1 = Title_Font.render("Hi I'm ROBIN !", True, (27, 42, 65))
Text_Title2 = Title_Font.render("Do you want to play with me ?", True, (27, 42, 65))

# Definitions des dessins boutons
Dance_Button = pygame.Rect (50, 150, 300, 280)
Mirror_Button = pygame.Rect (450, 150, 300, 280)
Back_Buttons =pygame.Rect (25,25,35,35)
Back_Buttons_font =  pygame.font.Font(None, 15)
Button_Font= pygame.font.Font(None, 50)

Run = True
# Boucle permettant de garder la fenetre ouverte
while Run:

    # Dessin
    screen.fill((242, 242, 242))

    if page=="home" :
        x_center= screen.get_width() // 2
        Height_line = Title_Font.get_linesize()
        screen.blit(Text_Title1, Text_Title1.get_rect(midtop=(x_center, 25)))
        screen.blit(Text_Title2, Text_Title2.get_rect(midtop=(x_center, 35 + Height_line)))

        buttons.draw_buttons(screen, Dance_Button, "Dance", (240, 147, 251), Button_Font)
        buttons.draw_buttons(screen, Mirror_Button, "Mirror", (145, 223, 243), Button_Font)

    elif page=="dance":
        Dance_title= Title_Font.render("Wich dance ?", True, (27, 42, 65))
        screen.blit(Dance_title, Dance_title.get_rect(midtop=(screen.get_width() // 2, 30)))
        buttons.draw_buttons(screen, Back_Buttons, "Home", (90, 99, 108), Back_Buttons_font)

    elif page=="mirror": 
        Mirror_title = Title_Font.render("It's time to move !", True, (27, 42, 65))
        screen.blit(Mirror_title, Mirror_title.get_rect(midtop=(screen.get_width() // 2, 30)))
        buttons.draw_buttons(screen, Back_Buttons, "Home", (90, 99, 108), Back_Buttons_font)

    # Boucle des evenements dans la fenetre
    for evenement in pygame.event.get(): 
        if evenement.type == pygame.QUIT: # Regarde si on appui sur la croix de la fenêtre
            Run = False

        elif evenement.type == pygame.MOUSEBUTTONDOWN: # Test si bouttons cliqués
            if page=="home" :
                if Dance_Button.collidepoint(evenement.pos):
                    page="dance"
                    print("Dance button clicked")
                elif Mirror_Button.collidepoint(evenement.pos) :
                    page="mirror"
                    print("Mirror button clicked")
            
            elif page=="dance" : 
                if Back_Buttons.collidepoint(evenement.pos):
                    page="home"
            
            elif page=="mirror" : 
                if Back_Buttons.collidepoint(evenement.pos):
                    page="home"

    pygame.display.flip()


pygame.quit() #Fermeture de la fenetre