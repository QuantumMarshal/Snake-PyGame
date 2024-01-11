import pygame
import os
# Class Button
class Button:    
    def __init__(self, x, y, image, scale):
        self.sprite = self.find_img(image, scale)
        self.current_state = 0
        self.image = self.sprite[self.current_state]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, window):
        window.blit(self.image, self.rect.topleft)

    def on_click(self):
        pos = pygame.mouse.get_pos()
        action = False
        
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
                self.change_state(2)
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked:
                self.change_state(2)
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.change_state(1)
        else: 
            self.change_state(0)
        return action
    
    def find_img(self, img, scale):
        dir_list = os.listdir(img)

        for i in range(len(dir_list)):
            dir_list[i] = pygame.image.load(f"{img}\{dir_list[i]}").convert_alpha()
            w = dir_list[i].get_width()
            h = dir_list[i].get_height()
            dir_list[i] = pygame.transform.scale(dir_list[i], (int(w * scale), int(h * scale)))

        return dir_list
    
    def change_state(self, state):
        self.current_state = state        
        self.image = self.sprite[self.current_state]