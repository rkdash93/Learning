import pygame
import csv
from pygame import mixer


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.64)


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario")

# set framerate
clock = pygame.time.Clock()
fps = 60

# Background
bg_img = pygame.image.load(".\\images\mario.png")

# Global variables
move_left = False
move_right = False
# tile_size = 60
rows = 16
cols = 150
level = 1
tile_size = SCREEN_HEIGHT // rows
tile_types = 21
gravity = 0.9
scroll_thresh = 100
shoot = False
screen_scroll = 0
bg_scroll = 0
pnt_brick_active = 1
mushroom_brick_active = 1
enemy_flg_count = 0
game_over = False

#load tile images
img_list = []
for x in range(tile_types):
    img = pygame.image.load(f".\\img\\tile\\{x}.png")
    img = pygame.transform.scale(img,(tile_size,tile_size))
    img_list.append(img)
#color
white = (255,255,255)
black = (0,0,0)


# Load sounds

jump_sound = pygame.mixer.Sound(".\\sound\\smb_jump-small.wav")
coin_sound = pygame.mixer.Sound(".\\sound\\smb_coin.wav")
break_sound = pygame.mixer.Sound(".\\sound\\smb_breakblock.wav")
fire_sound = pygame.mixer.Sound(".\\sound\\smb_fireball.wav")
transform_sound = pygame.mixer.Sound(".\\sound\\smb_powerup.wav")
die_sound = pygame.mixer.Sound(".\\sound\\smb_mariodie.wav")
flag_sound = pygame.mixer.Sound(".\\sound\\smb_flagpole.wav")
game_over_sound = pygame.mixer.Sound(".\\sound\\smb_stage_clear.wav")


mixer.music.load(".\\sound\\background.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

def load_bg():
    # screen.fill(bg_img)
    width = bg_img.get_width()
    for i in range(5):
        screen.blit(bg_img,((i * width) - bg_scroll,0))
    # temp
    # pygame.draw.line(screen,black,(0,350),(SCREEN_WIDTH,350))

# temporary code for drawing grid
#draw grid
# def draw_grid():
# 	#vertical lines
# 	for c in range(cols + 1):
# 		pygame.draw.line(screen, white, (c * tile_size - screen_scroll, 0), (c * tile_size - screen_scroll, SCREEN_HEIGHT))
# 	#horizontal lines
# 	for c in range(rows + 1):
# 		pygame.draw.line(screen, white, (0, c * tile_size), (SCREEN_WIDTH, c * tile_size))


def color_replace(surface, find_color, replace_color):
    for x in range(surface.get_size()[0]):
        for y in range(surface.get_size()[1]):
            if surface.get_at([x, y]) == find_color:
                surface.set_at([x, y], replace_color)
    return surface        

class Character(pygame.sprite.Sprite):
    def __init__(self,x,y,img,speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
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
        self.big = False
        self.power = False
        self.transform = False
        self.shrink = False
        self.name = img
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # 0:idle 1:run 2:jump 3:die 4:grow 5:big_idle 6:big_run 7:big_jump
        self.update_time = pygame.time.get_ticks()
        # if self.name == "mario":
        #     self.image = pygame.image.load(f".\\images\\{img}_small\\idle\\{img}_idle0.png")
        #     if self.grow == True:
        #         self.image = pygame.image.load(f".\\images\\{img}_big\\idle\\{img}_idle0.png")
        # else:
        #     self.image = pygame.image.load(f".\\images\\{img}\\idle\\{img}_idle0.png")
        self.image = pygame.image.load(f".\\images\\{img}\\idle\\{img}_idle0.png")
        # self.rect = self.image.get_rect()
        # self.rect.center = (x,y)
        if img in ("mario"): 
            #load images for idle state
            temp_list = self.load_img("idle")
            self.animation_list.append(temp_list)
            
            #load images for run state
            temp_list = self.load_img("run")            
            self.animation_list.append(temp_list)

            #load images for jump state
            temp_list = self.load_img("jump")            
            self.animation_list.append(temp_list)

            #load images for die state
            temp_list = self.load_img("die")            
            self.animation_list.append(temp_list)

            #load images for grow state
            temp_list = self.load_img("grow")            
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
        self.rect.center = (self.x,self.y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def load_img(self,action):
        temp_list = []
        max_index = 3
        if self.name == "mario" and self.action == 4:
            max_index = 7
        elif self.name in ("goomba","koopa") and self.action == 3:
            max_index = 5
        else:
            max_index = 3
        for i in range(max_index):
            img = pygame.image.load(f".\\images\\{self.name}\\{action}\\{self.name}_{action}{i}.png")
            if self.name == "mario" and self.action in (0,1,2):
                img = pygame.transform.scale(img,(img.get_width()*0.9,img.get_height() * 0.5))
            # if self.name in ("goomba","koopa"):
            #     img = pygame.image.load(f".\\images\\{self.name}\\{action}\\{self.name}_{action}{i}.png")
            # else:
            #     if self.grow == False:
            #         img = pygame.image.load(f".\\images\\{self.name}_small\\{action}\\{self.name}_{action}{i}.png")
            #     else:
            #         img = pygame.image.load(f".\\images\\{self.name}_big\\{action}\\{self.name}_{action}{i}.png")
            # # img = pygame.transform.scale(img, (img.get_width()*1.5,img.get_height()*1.5)) 
            if self.name == "koopa":
                img = pygame.transform.scale(img, (img.get_width()*0.85,img.get_height()*0.85))
            temp_list.append(img)
        return  temp_list

    def update_anim(self):
        animation_cooldown = 100
        # update image
        
        self.image = self.animation_list[self.action][self.frame_index]
        img2 = self.image
        x_pos = self.rect.centerx
        y_pos = self.rect.centery
        if self.grow == True:
            self.image = pygame.transform.scale(self.image, (self.image.get_width()*1.2,self.image.get_height()*1.5))
            if self.big == True:
                
                self.rect = self.image.get_rect()
                self.rect.center = (x_pos,y_pos)
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.big = False        
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (x_pos,y_pos)
            self.width = self.image.get_width()
            self.height = self.image.get_height()

        if self.power == True:
            # if self.transform == True:
                self.image = color_replace(self.image,(171,123,10),(255,255,255))
                self.image = color_replace(self.image,(247,56,3),(189,48,33))
                # self.image = color_replace(self.image,(247,54,2),(255,255,255))
                # self.image = color_replace(self.image,(246,55,2),(255,255,255))
                # self.image = color_replace(self.image,(232,66,4),(255,255,255))
                # self.image = color_replace(self.image,"red","white")
                # self.transform = False

        # if self.power == False and self.grow == False:
        #     self.image = img2
        #     self.rect = self.image.get_rect()
        #     self.rect.center = (x_pos,y_pos)
        #     self.width = self.image.get_width()
        #     self.height = self.image.get_height()            
        #     # if self.shrink == True:
        #         self.image = color_replace(self.image,(255,255,255),(171,123,10))
        #         self.image = color_replace(self.image,(189,48,33),(247,56,3))
        #         self.shrink = False                
        # # elif  self.name == "mario" and self.power == False:
        #     self.image = color_replace(self.image,(255,255,255),(171,123,10))
        #     self.image = color_replace(self.image,(189,48,33),(247,56,3))           

        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # reset frame index to 0 after all the images are iterated
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action in (3,4):
                self.frame_index = 0            
            else:
                self.idle()

    def idle(self):
        self.action = 0
        # if self.name == "mario":
        #     self.action = 5        
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()             


    def move(self,move_left,move_right):
        global pnt_brick_active
        global mushroom_brick_active
        screen_scroll = 0
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
            self.vel_y = -19
            self.jump = False
            self.on_land = True

        # player die action
        if self.alive == False:
            # self.action = 2
            self.vel_y = -15
            # self.Jump = False
            # self.on_land = True            
            
        # apply gravity
        self.vel_y += gravity
        if self.vel_y > 7:
            self.vel_y               
        dy += self.vel_y

        if self.rect.bottom + dy < 180 and self.alive == False:
            
            dy = 180 - self.rect.bottom
            self.vel_y = 0    

        # Check collision with floor
            # Check collision with floor
        for pipe in pipe_group:
            if pygame.sprite.spritecollide(self, pipe_group, False) and self.rect.bottom >= pipe.rect.top:
                if self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = pipe.rect.top - self.rect.bottom
        
        # generate coins from coin bricks

        for point_brick in point_brick_group:
            # if pygame.sprite.spritecollide(self, point_brick_group, False):
            if point_brick.rect.colliderect(self.rect.x + dx,self.rect.y,self.width,self.height) and self.alive:
                self.rect.x -=5 * self.direction             
            if point_brick.rect.colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:  
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = point_brick.rect.bottom - self.rect.top                   
                    point_brick.image = pygame.image.load(f".\\images\\empty_brick.png")
                    if point_brick.active == True:
                        coin = Coin(point_brick.rect.centerx, point_brick.rect.top - 5,1)
                        coin_group.add(coin)
                        coin_sound.play()
                        point_brick.active = False

                # falling down    
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = point_brick.rect.top - self.rect.bottom

        for plant_brick in plant_brick_group:
            # if pygame.sprite.spritecollide(self, plant_brick_group, False):
            if plant_brick.rect.colliderect(self.rect.x + dx,self.rect.y,self.width,self.height) and self.alive:
                self.rect.x -=5 * self.direction             
            if plant_brick.rect.colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:  
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = plant_brick.rect.bottom - self.rect.top                   
                    plant_brick.image = pygame.image.load(f".\\images\\empty_brick.png")
                    plant = Plant(plant_brick.rect.centerx, plant_brick.rect.top - 20)
                    plant_group.add(plant)

                # falling down    
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = point_brick.rect.top - self.rect.bottom  





        # generate mushroom from bricks

        for mushroom_brick in mushroom_brick_group:
            # if pygame.sprite.spritecollide(self, point_brick_group, False):
            if mushroom_brick.rect.colliderect(self.rect.x + dx,self.rect.y,self.width,self.height) and self.alive:
                self.rect.x -=5 * self.direction           
            if mushroom_brick.rect.colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:  
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = mushroom_brick.rect.bottom - self.rect.top                    
                    mushroom_brick.image = pygame.image.load(f".\\images\\empty_brick.png")
                    
                    if mushroom_brick_active == 1:
                        mushroom = Mushroom(mushroom_brick.rect.x, mushroom_brick.rect.top - 32)
                        mushroom_group.add(mushroom)
                    mushroom_brick_active = 0
                    
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = mushroom_brick.rect.top - self.rect.bottom                                                          

        for brick in brick_group:
            # if pygame.sprite.spritecollide(self, brick_group, False):
            if brick.rect.colliderect(self.rect.x + dx,self.rect.y,self.width,self.height) and self.alive:
                self.rect.x -=5 * self.direction
            if brick.rect.colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = brick.rect.bottom - self.rect.top
                    if self.grow == True:
                        brick.kill()
                        brick_break = Brick_break(brick.rect.x,brick.rect.y)
                        brick_break_group.add(brick_break)
                        break_sound.play()

                    
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = brick.rect.top - self.rect.bottom

        for flag in flag_group:
            # if pygame.sprite.spritecollide(self, brick_group, False):
            if flag.rect.colliderect(self.rect.x + dx,self.rect.y,self.width,self.height):
                dx = 0
                  

        for tile in world.obstacle_list:

            # horizontal collision with obstacles
            if tile[1].colliderect(self.rect.x + dx,self.rect.y,self.width,self.height) and self.alive:
                self.rect.x -=5 * self.direction
            # vertical collision with obstacles                
            if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                    
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = tile[1].top - self.rect.bottom
                    if self.grow == True:
                        dy = tile[1].top - self.rect.bottom
        
        self.rect.x += dx
        self.rect.y += dy        

        #update scroll based on player position
        if self.name == "mario":
            if self.rect.right > SCREEN_WIDTH - scroll_thresh or self.rect.left < scroll_thresh:
                self.rect.x -= dx # when player reaches the edge player should not move, screen should move
                screen_scroll = -dx
            
        return screen_scroll
    def enemy_ai(self):
        dx = 0
        dy = 0
               
        if self.alive:
            self.action = 1
            if pl.rect.x - self.rect.x <= 100 or self.rect.x - pl.rect.x <= 100:
                self.rect.x += self.direction * (-1)
            self.vel_y += 5 
            # apply gravity
            self.vel_y += gravity
            if self.vel_y > 5:
                self.vel_y               
            dy += self.vel_y
            # # self.rect.y += dy            
        else:
            # if self.rect.right > SCREEN_WIDTH:
            #     if self.name == "koopa":
            #         self.speed *= -1             
            self.rect.x += self.speed

        # jump action
        if self.action == 4:
            if self.jump == True and self.on_land == False:
                # self.action = 2
                self.vel_y = -5
                self.jump = False
                self.on_land = True

                
            # apply gravity
            self.vel_y += gravity
            if self.vel_y > 10:
                self.vel_y               
            dy += self.vel_y


        for brick in brick_group:
            # if pygame.sprite.spritecollide(self, brick_group, False):
            if brick.rect.colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = brick.rect.bottom - self.rect.top
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = brick.rect.top - self.rect.bottom + 2
                                      
                      
        for tile in world.obstacle_list:
            # horizontal collision with obstacles
            if tile[1].colliderect(self.rect.x + dx,self.rect.y,self.width,self.height) and self.name == "goomba" and self.alive:
                # self.rect.x -=5 * self.direction
                self.direction *= (-1)
                
            # vertical collison with obstacles
            if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                  
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = tile[1].top - self.rect.bottom 
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()
        self.rect.x += screen_scroll            

    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False), self.rect)               

class World():
    def __init__(self):
        self.obstacle_list = []
        # self.point_brick_list = []

    def process_data(self,data):
        # iterate through each value in level data
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * tile_size
                    img_rect.y = y * tile_size
                    tile_data = (img,img_rect)
                    if tile in (0,12,19):
                        self.obstacle_list.append(tile_data)
                    if tile == 1:
                        water = Water(x*tile_size,y*tile_size)
                        water_group.add(water)                                                                        
                    elif tile == 2:
                        brick = Brick(x*tile_size,y*tile_size)
                        brick_group.add(brick)
                    elif tile == 3:  # brick to generate coins
                        point_brick = Point_brick(x*tile_size,y*tile_size)
                        point_brick_group.add(point_brick)                        
                    elif tile == 4:
                        g_enemy = Character(x*tile_size,y*tile_size,"goomba",2) # goomba
                        g_enemy_group.add(g_enemy)
                    elif tile == 5:
                        k_enemy = Character(x*tile_size,y*tile_size,"koopa",3) # koopa
                        k_enemy_group.add(k_enemy)                                                
                    elif tile == 6:
                        pl = Character(x*tile_size,y*tile_size,"mario",5) # player
                    elif tile == 7:
                        pipe = Pipe(x*tile_size,y*tile_size-12)
                        pipe_group.add(pipe) # player
                    elif tile == 8:
                        coin = Coin(x*tile_size,y*tile_size-12,0)
                        coin_group.add(coin) # player                        
                    elif tile == 11:  #brick to generate mushrooms
                        mushroom_brick = Mushroom_brick(x*tile_size,y*tile_size)
                        mushroom_brick_group.add(mushroom_brick)
                    elif tile == 13:  #flag
                        flag = Flag(x*tile_size,y*tile_size)
                        flag_group.add(flag)
                    elif tile == 14:  #castle
                        castle = Castle(x*tile_size,y*tile_size)
                        castle_group.add(castle)
                    elif tile == 15:  #castle
                        enemy_flag = Enemy_flag(x*tile_size,y*tile_size)
                        enemy_flag_group.add(enemy_flag)
                    elif tile == 16:  #castle
                        flag_bottom = Flag_bottom(x*tile_size,y*tile_size)
                        flag_bottom_group.add(flag_bottom)
                    elif tile == 17:  #castle
                        plant = Plant(x*tile_size,y*tile_size)
                        plant_group.add(plant)
                    elif tile == 18:  #castle
                        plant_brick = Plant_brick(x*tile_size,y*tile_size)
                        plant_brick_group.add(plant_brick)                                                                                                                                                                                                   
                    else:
                        pass
        return pl

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])


class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\pipe.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        self.rect.x += screen_scroll

class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\brick.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.update_time = pygame.time.get_ticks()
        self.break_flg = False
    def update(self):      
        self.rect.x += screen_scroll

class Brick_break(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(4):
            img = pygame.image.load(f".\\images\\brick_break\\{i}.png")
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
    def update(self):
        break_speed = 2 
        self.counter += 1

        if self.counter >= break_speed:
            self.counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.frame_index = 0
                self.kill()
            self.image = self.images[self.frame_index]    
        self.rect.x += screen_scroll        

class Point_brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\pnt_brick.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.active = True
    def update(self):
        # if pnt_brick_active == 0:
        #     self.image = pygame.image.load(f".\\images\\empty_brick.png")        
        self.rect.x += screen_scroll

class Flag(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\flag.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
         
    def update(self):
        # if pnt_brick_active == 0:
        #     self.image = pygame.image.load(f".\\images\\empty_brick.png")        
        self.rect.x += screen_scroll

class Enemy_flag(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\en_flg.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
         
    def update(self):
        global enemy_flg_count
        for flag in flag_group:
            # if pygame.sprite.spritecollide(self, brick_group, False):
            if flag.rect.colliderect(pl.rect.x + 30,pl.rect.y,pl.width,pl.height) and pl.alive:
                enemy_flg_count += 1
                if enemy_flg_count == 1:
                    flag_sound.play()
                pl.vel_y = 5
                self.rect.y = pl.rect.y - pl.rect.height/2
                if self.rect.y < 50:
                     self.rect.y += 50 - self.rect.y     
        self.rect.x += screen_scroll        

class Castle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\castle.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
         
    def update(self):
        global game_over
        for castle in castle_group:
            # if pygame.sprite.spritecollide(self, brick_group, False):
            # if castle.rect.colliderect(pl.rect.x + 30,pl.rect.y,pl.width,pl.height) and pl.alive:
            if castle.rect.left < pl.rect.right and castle.rect.left > pl.rect.left and pl.alive:            
                game_over = True
                game_over_sound.play()       
        self.rect.x += screen_scroll

class Flag_bottom(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\flg_bottom.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
         
    def update(self):
        # if pnt_brick_active == 0:
        #     self.image = pygame.image.load(f".\\images\\empty_brick.png")        
        self.rect.x += screen_scroll

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y,gen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.gen = gen 
    def update(self):
        if self.gen == 1:
            self.rect.y -= 70
        self.rect.x += screen_scroll

class Plant(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\power_plant.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        self.rect.x += screen_scroll

class Water(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\water.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y) 
    def update(self):
        for water in water_group:
            # if pygame.sprite.spritecollide(self, brick_group, False):
            if water.rect.colliderect(pl.rect.x + 30,pl.rect.y,pl.width,pl.height) and pl.alive:
                pl.vely = -5
                pl.alive = False
                die_sound.play()        
        self.rect.x += screen_scroll                                                     

class Mushroom_brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\pnt_brick.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
         
    def update(self):      
        self.rect.x += screen_scroll

class Plant_brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\pnt_brick.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
         
    def update(self):    
        self.rect.x += screen_scroll                  

class Mushroom(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f".\\images\\mushroom.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()         
        self.vel_y = 0
        self.on_land = False
        self.direction = 1 # 1: right -1 left

    def update(self):
        # self.rect.x += -1
        dx = 2 * self.direction
        dy = 0
               
        self.vel_y += 5 
            # apply gravity
        self.vel_y += gravity
        if self.vel_y > 5:
            self.vel_y               
            dy += self.vel_y
            # # self.rect.y += dy            
        else:
            # if self.rect.right > SCREEN_WIDTH:
            #     if self.name == "koopa":
            #         self.speed *= -1             
            self.rect.x += self.speed

        # # jump action
        # if self.action == 4:
        #     if self.jump == True and self.on_land == False:
        #         # self.action = 2
        #         self.vel_y = -5
        #         self.jump = False
        #         self.on_land = True

                
        #     # apply gravity
        #     self.vel_y += gravity
        #     if self.vel_y > 10:
        #         self.vel_y               
        #     dy += self.vel_y

        for brick in brick_group:
            if pygame.sprite.spritecollide(self, brick_group, False) and self.alive:
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = brick.rect.bottom - self.rect.top
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = brick.rect.top - self.rect.bottom + 2
                      
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height) and self.alive:
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                  
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = tile[1].top - self.rect.bottom                  
            # if self.rect.bottom + dy > 470:
            #     dy = 470 - self.rect.bottom
            #     self.rect.x -= 5000
            #     # if self.action == 2:
            #     #     self.action = 0
            #     self.on_land = False
        self.rect.x += dx
        self.rect.y += dy
        # self.rect.x += screen_scroll * self.direction               
        self.rect.x += screen_scroll                                                           

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction
    def update(self):
        #bullet animation
        animation_cooldown = 50
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
        self.rect.x += (self.direction * self.speed) + screen_scroll
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        if self.jump == True and self.on_land == False:
        #     # self.action = 2
            self.vel_y = -15
            self.jump = False
            self.on_land = True

            # self.vel_y -= 3
            # self.vel_y += 2
            # # self.Jump = False
            # # self.on_land = True            
            
        # apply gravity
        self.vel_y += (gravity*0.8)
        if self.vel_y > 7:
            self.vel_y               
        dy += self.vel_y

        # if self.rect.bottom + dy < 350:
        #     dy = 350 - (self.rect.bottom + 50)  
        #     if self.action == 2:
        #         self.action = 0        
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height):
                # if jumping up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # falling down
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.on_land = False
                    dy = tile[1].top - self.rect.bottom  
            # if self.action == 2:
            #     self.action = 0
            self.on_land = False
        self.rect.x += dx
        self.rect.y += dy

        # bullet collision
        for g_enemy in g_enemy_group:
            if pygame.sprite.spritecollide(g_enemy, bullet_group, False):
                self.kill()
                g_enemy.bullet_die = True
                g_enemy.alive = False
                g_enemy.speed = 2
                # g_enemy.on_land = False
                g_enemy.jump = True
                
                g_enemy.action = 4 

        for k_enemy in k_enemy_group:
            if pygame.sprite.spritecollide(k_enemy, bullet_group, False):
                self.kill()
                k_enemy.bullet_die = True
                k_enemy.alive = False
                k_enemy.speed = 2
                # g_enemy.on_land = False
                k_enemy.jump = True
                
                k_enemy.action = 4
        
        for pipe in pipe_group:
            if pygame.sprite.spritecollide(pipe, bullet_group, False):
                self.kill()                                






# pl = Character(200,350,"mario",2)
# g_enemy = Character(400,325,"goomba",2)
# k_enemy = Character(600,320,"koopa",2)
# g_enemy_group.add(g_enemy)
# k_enemy_group.add(k_enemy)







# mushroom = Mushroom(400, 420)
# mushroom_group.add(mushroom)

world_data = []
for row in range(rows):
    r = [-1] * cols
    world_data.append(r)

with open(f"level{level}_data.csv",newline="") as csvfile:
    reader = csv.reader(csvfile,delimiter=",")
    for x,row in enumerate(reader):
        for y,tile in enumerate(row):
            world_data[x][y] = int(tile)


 
bullet_group = pygame.sprite.Group()

g_enemy_group = pygame.sprite.Group()

k_enemy_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
brick_group = pygame.sprite.Group()
point_brick_group = pygame.sprite.Group()
mushroom_group = pygame.sprite.Group()
mushroom_brick_group = pygame.sprite.Group()
brick_break_group = pygame.sprite.Group()
flag_group = pygame.sprite.Group()
castle_group = pygame.sprite.Group()
enemy_flag_group = pygame.sprite.Group()
flag_bottom_group = pygame.sprite.Group()
coin_group =  pygame.sprite.Group()
water_group = pygame.sprite.Group()
plant_group = pygame.sprite.Group()
plant_brick_group = pygame.sprite.Group()

world = World()
pl = world.process_data(world_data)


run = True
while run:
    clock.tick(fps)
    load_bg()
    # draw_grid()
    world.draw()
    pl.update_anim()
    if pl.shoot_cooldown > 0:
        pl.shoot_cooldown -= 1
    # for g_enemy in g_enemy_group:
    #     g_enemy.update_anim()
    # for k_enemy in k_enemy_group:
    #     k_enemy.update_anim()
   
    pl.draw()

    # goomba related actions/collisions

    for g_enemy in g_enemy_group:
        g_enemy.update_anim()        
        g_enemy.draw()
        g_enemy.enemy_ai()
        if g_enemy.alive == False:
            if g_enemy.rect.x - pl.rect.x > 100 or pl.rect.x - g_enemy.rect.x > 100:  
                g_enemy.kill()        
        # Check collision with pipes
        if pygame.sprite.spritecollide(g_enemy, pipe_group, False):
            if g_enemy.flip:
                g_enemy.flip = False
            else:
                g_enemy.flip = True
            g_enemy.direction *= -1
            g_enemy.speed *= -1
                     
        if pygame.Rect.colliderect(pl.rect, g_enemy.rect):
            if pl.action == 2: 
                g_enemy.action = 3
                g_enemy.rect.y += 10
                g_enemy.alive = False
                g_enemy.speed = 0

  
                
            # player hit by goomba
            elif g_enemy.action != 3:
                # pl.action = 3
                # pl.rect.x -= 10
                if pl.grow == True and g_enemy.rect.right >= pl.rect.left - 5:
                    pl.action = 4
                    pl.grow = False
                    pl.power = False
                    # pl.shrink = True
                    pl.image = color_replace(pl.image,(255,255,255),(171,123,10))
                    pl.image = color_replace(pl.image,(189,48,33),(247,56,3))                    
                    if pl.rect.x <= pl.width + screen_scroll:
                        pl.rect.x += pl.width + g_enemy.width + 1
                    else:
                        g_enemy.rect.x -= pl.width + g_enemy.width + 1
                    # pl.rect.x += screen_scroll                     
                else:    
                    pl.alive = False
                    die_sound.play()



    for k_enemy in k_enemy_group:
        k_enemy.update_anim()    
        k_enemy.draw()
        k_enemy.enemy_ai()

    # Kill koopa
    for k_enemy in k_enemy_group:       
        # Check collision with pipes
        if pygame.sprite.spritecollide(k_enemy, pipe_group, False):
            if k_enemy.flip:
                k_enemy.flip = False

            else:
                k_enemy.flip = True
            k_enemy.direction *= -1
            k_enemy.speed *= -1
        # check collision with player        
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
                # k_enemy.kill()                       
            elif k_enemy.action != 3:
                # pl.action = 3
                if pl.grow == True and k_enemy.rect.right >= pl.rect.left - 5:
                    pl.action = 4
                    pl.grow = False
                    pl.power = False
                    # pl.shrink = True
                    pl.image = color_replace(pl.image,(255,255,255),(171,123,10))
                    pl.image = color_replace(pl.image,(189,48,33),(247,56,3))  
                    if pl.rect.x <= pl.width + screen_scroll:
                        pl.rect.x += pl.width + k_enemy.width + 1
                    else:
                        k_enemy.rect.x -= pl.width + k_enemy.width + 1
                    # pl.rect.x += screen_scroll                 
                # pl.rect.x -= 10                
                else:
                    pl.alive = False
                    die_sound.play()
                    # k_enemy.kill()
            elif k_enemy.action == 3 and k_enemy.speed != 0 and pl.action != 2:
                # pl.action = 3
                if pl.grow == True and k_enemy.rect.right >= pl.rect.left - 5:
                    pl.action = 4
                    pl.grow = False
                    pl.power = False
                    pl.power = False
                    # pl.shrink = True
                    pl.image = color_replace(pl.image,(255,255,255),(171,123,10))
                    pl.image = color_replace(pl.image,(189,48,33),(247,56,3))  
                    if pl.rect.x <= pl.width + screen_scroll:
                        pl.rect.x += pl.width + k_enemy.width + 1
                    else:
                        k_enemy.rect.x -= pl.width + k_enemy.width + 1
                    # pl.rect.x += screen_scroll                   
                # pl.rect.x -= 10
                
                else:
                    pl.alive = False
                    die_sound.play()

        # Kill goomba with dead koopa shells

        for g_enemy in g_enemy_group:            
            if pygame.Rect.colliderect(g_enemy.rect, k_enemy.rect):    
                if k_enemy.action == 3 and k_enemy.speed != 0:
                    g_enemy.bullet_die = True
                    g_enemy.alive = False
                    g_enemy.speed = 2
                    
                    # g_enemy.on_land = False
                    g_enemy.jump = True
                    
                    g_enemy.action = 4         
          
    # for g_enemy in g_enemy_group:
    #     g_enemy.enemy_ai()
    # for k_enemy in k_enemy_group:
    #     k_enemy.enemy_ai()
# update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)
    pipe_group.update()
    pipe_group.draw(screen)
    brick_group.update()
    brick_group.draw(screen)
    point_brick_group.update()
    point_brick_group.draw(screen)
    mushroom_group.update()
    mushroom_group.draw(screen)    
    mushroom_brick_group.update()
    mushroom_brick_group.draw(screen)
    brick_break_group.update()
    brick_break_group.draw(screen)
    flag_group.update()
    flag_group.draw(screen)
    castle_group.update()
    castle_group.draw(screen)
    enemy_flag_group.update()
    enemy_flag_group.draw(screen)
    flag_bottom_group.update()
    flag_bottom_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    water_group.update()
    water_group.draw(screen)
    plant_group.update()
    plant_group.draw(screen)
    plant_brick_group.update()
    plant_brick_group.draw(screen) 

    if game_over == True:
        game_over_sound.play()
        game_over = False

    if pl.alive:
        if shoot:
            if pl.shoot_cooldown == 0:
                pl.shoot_cooldown = 20
                bullet = Bullet(pl.rect.centerx + (pl.rect.size[0] * pl.direction), pl.rect.centery, pl.direction)
                bullet_group.add(bullet)
                
        if pl.on_land:
            pl.action = 2
        # elif pl.die:
        #     pl.action = 3
            # pl.die = False        
        elif move_left or move_right:
            pl.action = 1
        else:
            pl.action = 0
    else:
        pl.action = 3
        pl.speed = 0
        
    screen_scroll = pl.move(move_left,move_right)
    bg_scroll -= screen_scroll
    
    for pipe in pipe_group:
        if pygame.sprite.spritecollide(pl, pipe_group, False) and pl.rect.bottom > pipe.rect.top + 10 and pl.on_land == False:
            # print("pipe top:",pipe.rect.top)
            # print("player bottom:",pl.rect.bottom)
            # print(pl.on_land)
            if pl.direction == 1:
                pl.rect.right -= pl.rect.width/2
            else:
                pl.rect.left += pl.rect.width/2


    # # Kill goomba
    # for g_enemy in g_enemy_group:
    #     if g_enemy.alive == False:
    #         if g_enemy.rect.x - pl.rect.x > 100 or pl.rect.x - g_enemy.rect.x > 100:  
    #             g_enemy.kill()        
    #     # Check collision with pipes
    #     if pygame.sprite.spritecollide(g_enemy, pipe_group, False):
    #         if g_enemy.flip:
    #             g_enemy.flip = False
    #         else:
    #             g_enemy.flip = True
    #         g_enemy.direction *= -1
    #         g_enemy.speed *= -1
                     
    #     if pygame.Rect.colliderect(pl.rect, g_enemy.rect):
    #         if pl.action == 2: 
    #             g_enemy.action = 3
    #             g_enemy.rect.y += 10
    #             g_enemy.alive = False
    #             g_enemy.speed = 0

  
                
    #         # player hit by goomba
    #         elif g_enemy.action != 3:
    #             # pl.action = 3
    #             # pl.rect.x -= 10
    #             if pl.grow == True and g_enemy.rect.right >= pl.rect.left - 5:
    #                 pl.action = 4
    #                 pl.grow = False
    #                 pl.power = False
    #                 # pl.shrink = True
    #                 pl.image = color_replace(pl.image,(255,255,255),(171,123,10))
    #                 pl.image = color_replace(pl.image,(189,48,33),(247,56,3))                    
    #                 if pl.rect.x <= pl.width + screen_scroll:
    #                     pl.rect.x += pl.width + g_enemy.width + 1
    #                 else:
    #                     g_enemy.rect.x -= pl.width + g_enemy.width + 1
    #                 # pl.rect.x += screen_scroll                     
    #             else:    
    #                 pl.alive = False
    #                 die_sound.play()
        # if pl.rect.x - g_enemy.rect.x == 100 or g_enemy.rect.x - pl.rect.x == 100:
        #     if g_enemy.alive == False:
        #         g_enemy.kill()                     
                # pl.grow = False


    # # Kill koopa
    # for k_enemy in k_enemy_group:       
    #     # Check collision with pipes
    #     if pygame.sprite.spritecollide(k_enemy, pipe_group, False):
    #         if k_enemy.flip:
    #             k_enemy.flip = False

    #         else:
    #             k_enemy.flip = True
    #         k_enemy.direction *= -1
    #         k_enemy.speed *= -1
    #     # check collision with player        
    #     if pygame.Rect.colliderect(pl.rect, k_enemy.rect):        
    #         if  pl.action == 1 and pl.jump == False and k_enemy.action == 3:
    #             if pl.rect.x < k_enemy.rect.x:
    #                 k_enemy.speed = 3
    #             else:
    #                 k_enemy.speed = -3
    #         elif pl.action == 2 and k_enemy.alive == True:
    #             k_enemy.action = 3
    #             pl.rect.x += 2
    #             pl.jump = True
    #             k_enemy.rect.y += 20
    #             k_enemy.speed = 0
    #             k_enemy.alive = False
    #             # k_enemy.kill()                       
    #         elif k_enemy.action != 3:
    #             # pl.action = 3
    #             if pl.grow == True and k_enemy.rect.right >= pl.rect.left - 5:
    #                 pl.action = 4
    #                 pl.grow = False
    #                 pl.power = False
    #                 # pl.shrink = True
    #                 pl.image = color_replace(pl.image,(255,255,255),(171,123,10))
    #                 pl.image = color_replace(pl.image,(189,48,33),(247,56,3))  
    #                 if pl.rect.x <= pl.width + screen_scroll:
    #                     pl.rect.x += pl.width + k_enemy.width + 1
    #                 else:
    #                     k_enemy.rect.x -= pl.width + k_enemy.width + 1
    #                 # pl.rect.x += screen_scroll                 
    #             # pl.rect.x -= 10                
    #             else:
    #                 pl.alive = False
    #                 die_sound.play()
    #                 # k_enemy.kill()
    #         elif k_enemy.action == 3 and k_enemy.speed != 0 and pl.action != 2:
    #             # pl.action = 3
    #             if pl.grow == True and k_enemy.rect.right >= pl.rect.left - 5:
    #                 pl.action = 4
    #                 pl.grow = False
    #                 pl.power = False
    #                 pl.power = False
    #                 # pl.shrink = True
    #                 pl.image = color_replace(pl.image,(255,255,255),(171,123,10))
    #                 pl.image = color_replace(pl.image,(189,48,33),(247,56,3))  
    #                 if pl.rect.x <= pl.width + screen_scroll:
    #                     pl.rect.x += pl.width + k_enemy.width + 1
    #                 else:
    #                     k_enemy.rect.x -= pl.width + k_enemy.width + 1
    #                 # pl.rect.x += screen_scroll                   
    #             # pl.rect.x -= 10
                
    #             else:
    #                 pl.alive = False
    #                 die_sound.play()

    #     for g_enemy in g_enemy_group:            
    #         if pygame.Rect.colliderect(g_enemy.rect, k_enemy.rect):    
    #             if k_enemy.action == 3 and k_enemy.speed != 0:
    #                 g_enemy.bullet_die = True
    #                 g_enemy.alive = False
    #                 g_enemy.speed = 2
                    
    #                 # g_enemy.on_land = False
    #                 g_enemy.jump = True
                    
    #                 g_enemy.action = 4 
                                                                             
    for mushroom in mushroom_group:
        # Check collision with pipes
        if pygame.sprite.spritecollide(mushroom, pipe_group, False):
            mushroom.direction *= -4         
        if pygame.sprite.spritecollide(pl, mushroom_group, False):
            print("player and mushroom collision")
            mushroom.kill()
            curr_time = pygame.time.get_ticks()
            wait_time = curr_time + 2000
            if curr_time <= wait_time:
                pl.action = 4
            pl.action = 0
            pl.grow = True
            pl.big = True
            transform_sound.play()
            # pl.update_anim()
                # curr_time = pygame.time.get_ticks() 
                # 

    for plant in plant_group:
            # if plant_brick.rect.colliderect(self.rect.x + dx,self.rect.y,self.width,self.height):
            if pygame.sprite.spritecollide(pl, plant_group, False):
                plant.kill()
                if pl.grow == True:
                    pl.power = True
                    pl.transform = True
                    transform_sound.play()
                else:
                    pl.grow = True
                    pl.big = True
                    transform_sound.play()
    for coin in coin_group:
        if pygame.sprite.spritecollide(pl, coin_group, False):
            coin.kill()
            coin_sound.play()
        if coin.rect.y < 0:
            coin.kill()                   

    # print("player grow", pl.grow)
    for event in pygame.event.get():
        if pl.alive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                    pl.action = 1
                if event.key == pygame.K_RIGHT:
                    move_right = True
                    pl.action = 1
                if event.key == pygame.K_UP:
                    # pl.action = 2
                    pl.jump = True
                    jump_sound.play()
                if event.key == pygame.K_SPACE:
                    if pl.power == True:
                        shoot = True
                        fire_sound.play()              
                                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                    pl.action = 0
                if event.key == pygame.K_RIGHT:
                    move_right = False
                    pl.action = 0
                if event.key == pygame.K_SPACE:
                    if pl.power == True:
                        shoot = False                                                                  
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

