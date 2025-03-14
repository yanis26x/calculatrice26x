import pygame

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
PINK_FLUO = (255, 20, 147)  # Rose fluo

# Dimensions de la fenêtre (agrandie)
WIDTH, HEIGHT = 400, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculatrice26x")

# Charger l'image de fond
background = pygame.image.load("xp.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Police d'écriture
font = pygame.font.Font(None, 50)
big_font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

# Affichage écran
display_rect = pygame.Rect(20, 20, WIDTH - 40, 70)
expression = ""

# Création des boutons
button_size = 80
margin = 15
buttons = []

touches = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", "=", "CLEAR", "+")
]

for row_idx, row in enumerate(touches):
    for col_idx, text in enumerate(row):
        x = col_idx * (button_size + margin) + margin
        y = row_idx * (button_size + margin) + 110
        color = RED if text in ["/", "*", "-", "+", "=", "CLEAR"] else BLACK
        text_color = RED if text not in ["/", "*", "-", "+", "=", "CLEAR"] else BLACK
        buttons.append([text, pygame.Rect(x, y, button_size, button_size), color, text_color, False])

# Boucle principale
running = True
while running:
    screen.blit(background, (0, 0))  # Affichage de l'image de fond
    
    # Affichage de l'écran
    pygame.draw.rect(screen, BLACK, display_rect)
    pygame.draw.rect(screen, RED, display_rect, 3)
    display_text = big_font.render(expression, True, PINK_FLUO)
    screen.blit(display_text, (display_rect.x + 15, display_rect.y + 15))
    
    # Affichage des boutons
    for button in buttons:
        text, rect, color, text_color, pressed = button
        button_color = PINK_FLUO if pressed else color
        pygame.draw.rect(screen, button_color, rect)
        pygame.draw.rect(screen, RED, rect, 3)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect.topleft)
    
    # Affichage du texte en bas
    bottom_text = small_font.render("-Yanis26x", True, PINK_FLUO)
    screen.blit(bottom_text, (20, HEIGHT - 60))
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                text, rect, _, _, _ = button
                if rect.collidepoint(event.pos):
                    button[4] = True  # Activer l'effet de clic
                    if text == "CLEAR":
                        expression = ""
                    elif text == "=":
                        try:
                            expression = str(eval(expression))
                        except:
                            expression = "Erreur"
                    else:
                        expression += text
        elif event.type == pygame.MOUSEBUTTONUP:
            for button in buttons:
                button[4] = False  # Désactiver l'effet de clic


    pygame.display.flip()

pygame.quit()
