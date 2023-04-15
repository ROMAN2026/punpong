import pygame

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image,get_rect()
        self.rect.x =player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x self.rect.y))

class Player(GameSprite):

     def update_r(self):
         keys = key.get_pressed()
        if keys[K_UP] and self.speed
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y +=self.speed

    def update_1(self):
        keys = key.get.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
            

back = (200,255,255)
window = display.set_mode((600,500))
window.fill(back)
display.set_caption("PING-PONG")

racket1 = Player('racket.png', 30,200,4,50,150)
racket2 = Player('racket.png', 520,200,4,50,150)



speed_x = 3
speed_y = 3

game = True
finish = False

clock = time.Clock()


while game:
    for e in event.get():
        if e.type == quit
            game = False

    if not finish:
        windows.fill(back)
        racket1.update_1() 
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_y += -1

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y += -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))


        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200,200))

    display.update()
    clock.tick(50)                                    
                       
