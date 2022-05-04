import pygame


def scale_image(img, factor): #definicia na menenie velkosti obrazkov (zadavam cim chcem obrazok vysanobit)
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle): #definicia na rotaciu aut (hranatych obrazkov) 
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center) 
    #premiestnenie otacacieho bodu obrazku z laveho horneho rohu do stredu obrazka
    win.blit(rotated_image, new_rect.topleft) #najdenie spravneho uhlu na otacanie obrazka (auta)


def blit_text_center(win, font, text): #definicia na vykreslenie, velkost a znenie textu
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /2, win.get_height()/2 - render.get_height()/2))