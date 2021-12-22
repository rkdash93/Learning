import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.65)


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario")

# set framerate
clock = pygame.time.Clock()
fps = 60

# Global variables
move_left = False
move_right = False
gravity = 0.75
shoot = False

#color
white = (255,255,255)
black = (0,0,0)

def load_bg():
    screen.fill(white)
    # temp
    pygame.draw.line(screen,black,(0,350),(SCREEN_WIDTH,350))

class Character(pygame.sprite.Sprite):
    def __init__(self,x,y,img,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1 # 1 for right -1 for left
        self.jump = False
        self.alive = True
        self.bullet_die = False
        self.on_land = True
        self.vel_y = 0
        self.shoot_cooldown = 0
        self.flip = False
        self.grow = False
        self.name = img
        self.animation_list = []
        self.frame_index = 0        
        self.action = 0 # 0:idle 1:run 2:jump
        # if self.name == "mario":
        #     self.action = 5        
        self.update_time = pygame.time.get_ticks()

        self.image = pygame.image.load(f".\\images\\{img}\\idle\\{img}_idle0.png")
        # self.rect = self.image.get_rect()
        # self.rect.center = (x,y)
        if img in ("mario"):
            #load images for idle state
            temp_list = self.load_img("idle")
            self.animation_list.append(temp_list)
            
            #load images for walk state
            temp_list = self.load_img("run")            
            self.animation_list.append(temp_list)

            #load images for walk state
            temp_list = self.load_img("jump")            
            self.animation_list.append(temp_list)

            #load images for walk state
            temp_list = self.load_img("die")            
            self.animation_list.append(temp_list)

            # #load images for big_idle state
            # temp_list = self.load_img("big_idle")            
            # self.animation_list.append(temp_list)


            # #load images for big_run state
            # temp_list = self.load_img("big_run")            
            # self.animation_list.append(temp_list)


            # #load images for big_idle state
            # temp_list = self.load_img("big_jump")            
            # self.animation_list.append(temp_list)                 

        elif img in ("goomba","koopa"):
            #load images for idle state
            temp_list = self.load_img("idle")
            self.animation_list.append(temp_list)
            
            #load images for walk state
            temp_list = self.load_img("run")            
            self.animation_list.append(temp_list)

            #load images for walk state
            temp_list = self.load_img("jump")            
            self.animation_list.append(temp_list)

            #load images for walk state
            temp_list = self.load_img("die")            
            self.animation_list.append(temp_list)

            #load images for walk state
            temp_list = self.load_img("bulletdie")            
            self.animation_list.append(temp_list)                          
        
               

        
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def load_img(self,action):
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f".\\images\\{self.name}\\{action}\\{self.name}_{action}{i}.png")
            temp_list.append(img)
        return  temp_list

    def update_anim(self):
        animation_cooldown = 100
        # update image
        self.image = self.animation_list[self.action][self.frame_index] 
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # reset frame index to 0 after all the images are iterated
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action in (3,) or self.grow == True:
                self.frame_index = 0
            else:
                self.idle()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()             


    def move(self,move_left,move_right):
        dx = 0
        dy = 0
        if move_left == True:
            dx = -self.speed
            self.direction = -1 # 1 for right -1 for left
            self.flip = True            
        if move_right == True:
            dx = self.speed
            self.direction = 1 # 1 for right -1 for left
            self.flip = False

        # jump action
        if self.jump == True and self.on_land == False:
            # self.action = 2
            self.vel_y = -17
            self.jump = False
            self.on_land = True

        # player die action
        if self.alive == False:
            # self.action = 2
            self.vel_y = -12
            # self.Jump = False
            # self.on_land = True            
            
        # apply gravity
        self.vel_y += gravity
        if self.vel_y > 10:
            self.vel_y               
        dy += self.vel_y

        if self.rect.bottom + dy < 150:
            dy = 150 - self.rect.bottom
            # if self.action == 2:
            #     self.action = 0        

        # Check collision with floor
        if self.rect.bottom + dy > 350:
            dy = 350 - self.rect.bottom
            # if self.action == 2:
            #     self.action = 0
            self.on_land = False
        self.rect.x += dx
        self.rect.y += dy

    def enemy_ai(self):
        dx = 0
        dy = 0        
        if self.alive:
            self.action = 1
            self.rect.x -= 1
        else:
            if self.rect.right > SCREEN_WIDTH:
                if self.name == "koopa":
                    self.speed *= -1             
            self.rect.x += self.speed

        # jump action
        if self.action == 4:
            if self.jump == True and self.on_land == False:
                # self.action = 2
                self.vel_y = -20
                self.jump = False
                self.on_land = True

                
            # apply gravity
            self.vel_y += gravity
            if self.vel_y > 10:
                self.vel_y               
            dy += self.vel_y

       

            # Check collision with floor
            if self.rect.bottom + dy > 470:
                dy = 470 - self.rect.bottom
                self.rect.x -= 5000
                # if self.action == 2:
                #     self.action = 0
                self.on_land = False
            self.rect.x += dx
            self.rect.y += dy            

    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False), self.rect)               


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        self.vel_y = 0
        self.jump = False
        self.on_land = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0:idle 1:run 2:jump
        self.update_time = pygame.time.get_ticks()

        self.image = pygame.image.load(f".\\images\\bullet\\bullet0.png")
        # self.rect = self.image.get_rect()
        # self.rect.center = (x,y)
        temp_list = []
        for i in range(2):
            img = pygame.image.load(f".\\images\\bullet\\bullet{i}.png")
            temp_list.append(img)
            self.animation_list.append(temp_list)        
        # img = pygame.image.load(".\\images\\bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    def update(self):
        #bullet animation
        animation_cooldown = 100
        # update image
        self.image = self.animation_list[self.action][self.frame_index] 
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # reset frame index to 0 after all the images are iterated
        if self.frame_index >= len(self.animation_list[self.action]):
             self.frame_index = 0

        # bullet tragectory
        dx = 0
        dy = 0
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        if self.jump == True and self.on_land == False:
        #     # self.action = 2
            self.vel_y = -17
            self.jump = False
            self.on_land = True

            self.vel_y -= 3
            self.vel_y += 2
            # self.Jump = False
            # self.on_land = True            
            
        # apply gravity
        self.vel_y += (gravity*0.12)
        if self.vel_y > 5:
            self.vel_y               
        dy += self.vel_y

        # if self.rect.bottom + dy < 350:
        #     dy = 350 - (self.rect.bottom + 50)  
            # if self.action == 2:
                # self.action = 0        

        # Check collision with floor
        if self.rect.bottom + dy > 340:
            dy = 340 - self.rect.bottom 
            # if self.action == 2:
            #     self.action = 0
            self.on_land = False
        self.rect.x += dx
        self.rect.y += dy

        # bullet collision
        if pygame.sprite.spritecollide(g_enemy, bullet_group, False):
            self.kill()
            g_enemy.bullet_die = True
            g_enemy.alive = False
            g_enemy.speed = 7
            # g_enemy.on_land = False
            g_enemy.jump = True
            
            g_enemy.action = 4 

        if pygame.sprite.spritecollide(k_enemy, bullet_group, False):
            self.kill()
            k_enemy.bullet_die = True
            k_enemy.alive = False
            k_enemy.speed = 7
            # g_enemy.on_land = False
            k_enemy.jump = True
            
            k_enemy.action = 4                         

bullet_group = pygame.sprite.Group()



# mushroom_group = pygame.sprite.Group()

pl = Character(200,350,"mario",2)
g_enemy = Character(400,325,"goomba",2)
k_enemy = Character(600,320,"koopa",2)
# mushroom = Object(600,320,"mushroom",2)




run = True
while run:
    clock.tick(fps)
    load_bg()
    pl.update_anim()
    if pl.shoot_cooldown > 0:
        pl.shoot_cooldown -= 1
    # g_enemy.update_anim()
    # k_enemy.update_anim()
   
    pl.draw()
    # g_enemy.draw()
    # k_enemy.draw()
    # g_enemy.enemy_ai()
    # k_enemy.enemy_ai()
# update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)       
    if pl.alive:
        if shoot:
            if pl.shoot_cooldown == 0:
                pl.shoot_cooldown = 20
                bullet = Bullet(pl.rect.centerx + (pl.rect.size[0] * pl.direction), pl.rect.centery, pl.direction)
                bullet_group.add(bullet)
                
        if pl.on_land:
            pl.action = 0
        # elif pl.die:
        #     pl.action = 3
            # pl.die = False        
        elif move_left or move_right:
            pl.action = 1
        else:
            pl.action = 0
    else:
        pl.action = 3
    pl.move(move_left,move_right)
    # Kill goomba
    if pygame.Rect.colliderect(pl.rect, g_enemy.rect):
        if pl.action == 2: 
            g_enemy.action = 3
            g_enemy.rect.y += 10
            g_enemy.alive = False
            curr_time = pygame.time.get_ticks()
            wait_time = curr_time + 1000
            g_enemy.speed = 0    
            

        elif g_enemy.action != 3:
            # pl.action = 3
            pl.rect.x -= 10
            pl.alive = False



    # Kill koopa
    if pygame.Rect.colliderect(pl.rect, k_enemy.rect):        
        if  pl.action == 1 and pl.jump == False and k_enemy.action == 3:
            if pl.rect.x < k_enemy.rect.x:
                k_enemy.speed = 3
            else:
                k_enemy.speed = -3
        elif pl.action == 2 and k_enemy.alive == True:
            k_enemy.action = 3
            pl.rect.x += 2
            pl.jump = True
            k_enemy.rect.y += 20
            k_enemy.speed = 0
            k_enemy.alive = False                       
        elif k_enemy.action != 3:
            # pl.action = 3
            pl.rect.x -= 10
            pl.alive = False
        elif k_enemy.action == 3 and k_enemy.speed != 0 and pl.action != 2:
            # pl.action = 3
            pl.rect.x -= 10
            pl.alive = False   


    # killed enemy should dissappear
    if (pl.rect.right - g_enemy.rect.right == 100) or  (g_enemy.rect.left - pl.rect.left) == 100 and g_enemy.alive == False:
        g_enemy.rect.x = -500
        g_enemy.kill()

    if (pl.rect.right - k_enemy.rect.right == 300) or (k_enemy.rect.left - pl.rect.left == 300) and k_enemy.alive == False:
        if  k_enemy.speed == 0:
            k_enemy.rect.x = -500
            k_enemy.kill()                      

                   

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
                pl.action = 0
            if event.key == pygame.K_RIGHT:
                move_right = True
                pl.action = 0
            if event.key == pygame.K_UP:
                # pl.action = 2
                pl.jump = True
            if event.key == pygame.K_SPACE:
                shoot = True
                                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
                pl.action = 0
            if event.key == pygame.K_RIGHT:
                move_right = False
                pl.action = 0
            if event.key == pygame.K_SPACE:
                shoot = False                                                  
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

