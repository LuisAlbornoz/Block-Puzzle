from .constants import  BRICK_BEGANE_X, BRICK_BEGANE_Y, BRICK_ROWS, BRICK_COLMS
import pygame 


bricks = ["assets/bloque.png","assets/bloque1.png","assets/bloque2.png",
"assets/bloque3.png", "assets/bloque4.png", "assets/bloque5.png"]


class Bricks: 
    def __init__(self, all_sprite):
        self.all_sprite = all_sprite
        self.all_bricks = pygame.sprite.Group()

        for r in range (BRICK_ROWS):
            for c in range (BRICK_COLMS):
                brick = Brick(r , c)
                self.all_sprite.add(brick)
                self.all_bricks.add(brick)

    def check_collision(self, ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce()
            brick.kill()




class Brick(pygame.sprite.Sprite):
    def __init__(self, row, colm):
        super().__init__()
        self.pos_x = BRICK_BEGANE_X + (colm * 64) + 32
        self.pos_y = BRICK_BEGANE_Y + (row * 32) + 16
        self.image = pygame.image.load(bricks[row])
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)






