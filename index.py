from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('Ping pong')
background = transform.scale(image.load('1643224102_new_preview_5d31c52bc865c16c0a6a332d.png'),(win_width,win_height))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_width,player_height):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y<win_height-80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
racket1 = Player("3439779.png",30,200,4,50,150)
racket2 = Player("3439779.png",620,200,4,50,150)
ball = GameSprite('png-clipart-tennis-balls-sphere-green-ball-sports-equipment-sphere-thumbnail-transformed.png',200,200,4,50,50)
font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE',True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE',True,(180,0,0))


game  = True
finish = False
FPS = 60
speed_x = 3
speed_y = 3
timer = 3600

points1 = 0
points2 = 0

score_text1 =font.render('Счет: '+ str(points1),1,(0,0,0))
score_text2 =font.render('Счет: '+ str(points2),1,(0,0,0))


while game:
    if timer <= 0:
        game = False
    else:
        timer -= 1

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *=-1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < -50:
            points2 += 1
            score_text2 =font.render('Счет: '+ str(points2),1,(0,0,0))
            time.delay(300)
            ball = GameSprite('png-clipart-tennis-balls-sphere-green-ball-sports-equipment-sphere-thumbnail-transformed.png',200,200,4,50,50)


        if ball.rect.x > win_width:
            points1 += 1
            score_text1 =font.render('Счет: '+ str(points1),1,(0,0,0))
            time.delay(300)
            ball = GameSprite('png-clipart-tennis-balls-sphere-green-ball-sports-equipment-sphere-thumbnail-transformed.png',200,200,4,50,50)
            

        window.blit(score_text1, (20, 20))
        window.blit(score_text2, (620, 20))

        racket1.reset()
        racket2.reset()
        ball.reset()
        if points1 >= 10:
            window.blit(lose2,(200,200))
            finish = True
        if points2 >= 10:
            window.blit(lose1,(200,200))
            finish = True
  

    display.update()
    clock.tick(FPS)





