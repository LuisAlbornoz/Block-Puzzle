import pygame


class Bootom():
    def __init__(self, x_pos, y_pos, width, height, fg, bg,content, fontsize):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.rect_x = self.x_pos
        self.rect_y = self.y_pos

        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.content = content 
        self.font = pygame.font.SysFont("Arial",fontsize, italic=True)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text , self.text_rect)


    def is_pressed (self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False




