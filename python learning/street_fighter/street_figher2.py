import pygame
import random
import time
pygame.init()

clock = pygame.time.Clock()
fps = 8
player_state = "idle"
enemy_state = "idle"
wait_time = None
enemy_ai_count = 0
countdown = 3
last_count = pygame.time.get_ticks()
game_over = False

# set screen
panel_height = 168
screen_width = 706
screen_height = 189 + panel_height


# Define game window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Street Fighter")

# panel = pygame.display.set_mode((screen_width,189))

# Load background image
bg_img = pygame.image.load("dogo1.jpg")
panel_img = pygame.image.load("button_panel.jpg")
fight_bt_img = pygame.image.load("fight_button.jpg")
# pygame.transform.scale(bg_img,(bg_img.get_width()*0.5,bg_img.get_height()*0.5))



# Define font
font = pygame.font.SysFont("Times New Roman", 26)
font2 = pygame.font.SysFont("Impact", 30)
font3 = pygame.font.SysFont("Segoe UI", 35)

# Define colours
red = (255,0,0)
green = (203,254,228)
black = (0,0,0)

top_txt = "Fight"

# function to load background image
def load_bg():
    screen.blit(bg_img,(0,0))

# function to draw text
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img, (x,y))

# function to load button panel
def load_panel():
    screen.blit(panel_img,(0,screen_height - panel_height))
    draw_text(top_txt, font, red, screen_width/2 - 20 , 20)




# Player class

class Player():
    def __init__(self,x,y,name,maxhealth):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.alive = True
        self.image = pygame.image.load(f".//karate_img//{name}1_idle.png")
        # img = pygame.image.load(f"{name}_idle.png")
        # self.image = pygame.transform.scale(img,(img.get_width()*1.5,img.get_height()*1.5))
        # self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def move(self,dir):
        if dir == "left" and self.rect.x > 48:
            self.rect.x -= 10
            self.image = pygame.image.load(".//karate_img//player1_walk.png")
        if dir == "right":       
        # if dir == "right" and self.rect.x < 320:
            self.image = pygame.image.load(".//karate_img//player1_walk.png")         
            self.rect.x += 10

    def block(self):
        global player_state
        pl.image = pygame.image.load(".//karate_img//player1_block.png")
        player_state = "defensive"

    def attack(self,attack_type):
        if attack_type == "punch":
            pl.image = pygame.image.load(".//karate_img//player1_punch.png")
        elif attack_type == "kick":
            pl.image = pygame.image.load(".//karate_img//player1_kick.png")
        elif attack_type == "fly":
            pl.image = pygame.image.load(".//karate_img//player1_fly.png")
            pl.rect.y -= 25
            pl.rect.x *= 1.2
        elif attack_type == "duck":
            pl.image = pygame.image.load(".//karate_img//player1_duck.png")            
            pl.rect.y += 25
                                 


    def draw(self):
        screen.blit(self.image,self.rect)

    

    def idle_state(self):
        global player_state
        self.image = pygame.image.load(".//karate_img//player1_idle.png")
        # self.image = pygame.transform.scale(img,(img.get_width()*1.5,img.get_height()*1.5))
        player_state = "idle"

    def en_idle_state(self):
        img = pygame.image.load("enemy_idle.png")
        en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))        

    # def enemy_fly(self):
    #     self.image = pygame.image.load(".//karate_img//enemy1_fly.png")
    #     pl.rect.y -= 25
    #     pl.rect.x *= (-1.2)
        
    
    def enemy_ai(self):
        global enemy_state
        global enemy_ai_count
        global top_txt
        if self.alive == True:
            if self.rect.x > 320 or self.rect.x < 550:
                # print(self.alive)
                print("within alive condition")
                move_list = [2,3,1,2,-3,-6,-5,-2,-1,-3]
                self.rect.x += int(random.choice(move_list))
                if enemy_ai_count % 4 == 0:
                    self.image = pygame.image.load(".//karate_img//enemy1_walk.png")
                else:
                    self.image = pygame.image.load(".//karate_img//enemy1_idle.png")

                print("Distance between player and enemy centerx:",self.rect.centerx - pl.rect.centerx)

                if self.rect.centerx - pl.rect.centerx  < 85:
                    if enemy_ai_count % 2 == 0:
                        enemy_action_list = [".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_block.png",".//karate_img//enemy1_idle.png"]
                    else:
                        enemy_action_list = [".//karate_img//enemy1_punch.png",".//karate_img//enemy1_kick.png",".//karate_img//enemy1_block.png"]
                    random_img = random.choice(enemy_action_list)
                    self.image = pygame.image.load(random_img)   
                    if random_img == "enemy1_block.png":
                        enemy_state = "defensive"
                    if random_img == "enemy1_idle.png":
                        enemy_state = "idle"
                    else:
                        enemy_state = "attack"

                # if self.rect.centerx - pl.rect.centerx  < 105:
                #     if enemy_ai_count % 2 == 0:
                #         enemy_action_list = [".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_block.png",".//karate_img//enemy1_idle.png"]
                #     else:
                #         enemy_action_list = [".//karate_img//enemy1_fly.png",".//karate_img//enemy1_fly.png",".//karate_img//enemy1_block.png",".//karate_img//enemy1_duck.png"]
                #     random_img = random.choice(enemy_action_list)
                #     self.image = pygame.image.load(random_img)   
                #     if random_img == "enemy1_block.png":
                #         enemy_state = "defensive"
                #     elif random_img == "enemy1_idle.png":
                #         enemy_state = "idle"
                #     elif random_img == "enemy1_fly.png":
                #         self.enemy_fly()
                #         self.rect.y += 25
                #         enemy_state = "fly"                        
                #     elif random_img == "enemy1_duck.png":
                #         enemy_state = "fly_defence"

                # if pygame.Rect.colliderect(self.rect, pl.rect) and player_state == "idle" and enemy_state in ("attack"):
                if self.rect.centerx - pl.rect.centerx  < 45 and player_state == "idle" and enemy_state in ("attack"):   
                    print("player hit collision")
                    top_txt = "Hit"               
                    pl.image = pygame.image.load(".//karate_img//player1_hit.png")
                    pl.health -= 10
                    self.rect.x += 20
                    pl.rect.x -= 50
                
                elif self.rect.centerx - pl.rect.centerx  < 45 and player_state in ("defensive"):
                    print("Player defend collision")
                    top_txt = "Block"
                    print(self.image)               
                    img = pygame.image.load(".//karate_img//enemy1_idle.png")
                    # self.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                    self.rect.x += 20
                    pl.rect.x -= 50
                    # enemy_state = "defenseless"
                    # print(enemy_state)                

                elif self.rect.centerx - pl.rect.centerx  < 45 and player_state in ("punch","kick") and enemy_state in ("defensive"):
                    print("defend collision")
                    top_txt = "Block"
                    print(self.image)               
                    img = pygame.image.load(".//karate_img//enemy1_idle.png")
                    # self.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                    self.rect.x += 20
                    pl.rect.x -= 50
                    enemy_state = "defenseless"
                # elif self.rect.centerx - pl.rect.centerx  < 40 and player_state in ("idle","punch") and enemy_state in ("fly"):
                #     print("player hit collision")
                #     print(self.image)               
                #     img = pygame.image.load(".//karate_img//enemy1_idle.png")
                #     # self.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                #     self.rect.x += 100
                #     pl.rect.x -= 50
                #     enemy_state = "defenseless"                    
                #     # print(enemy_state)
                      
                # elif self.rect.centerx - pl.rect.centerx  < 40 and player_state in ("duck","kick")  and enemy_state in ("fly_defence","kick"):
                #     print("enemy defend collision")
                #     print(self.image)               
                #     img = pygame.image.load(".//karate_img//enemy1_idle.png")
                    # self.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                    # self.rect.x += 100
                    # pl.rect.x -= 50

                # elif self.rect.centerx - pl.rect.centerx  < 40 and player_state in ("fly")  and enemy_state in ("defensive"):
                #     print("Player defend collision")
                #     print(self.image)               
                #     img = pygame.image.load(".//karate_img//enemy1_idle.png")
                #     # self.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                #     self.rect.x += 100
                #     pl.rect.x -= 50
                # for img in img_list:
                # self.image = pygame.image.load(img)
                # print(img)
                # # print(pl.rect.x)
                # if en.rect.x > 650:
                #     en.rect.x += -10
                # if pl.rect.x < 45:
                #     pl.rect.x += 5
                # print("above player collision condition")
                # print("enemy_state",enemy_state)
                # print("player_state",player_state)
                # print(pygame.Rect.colliderect(self.rect, pl.rect))           


                # img_list = [".//karate_img//enemy1_idle.png",".//karate_img//enemy1_punch.png",".//karate_img//enemy1_punch.png",".//karate_img//enemy1_kick.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_kick.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png",".//karate_img//enemy1_idle.png"]
                #         # img_list = ["enemy_block.png","enemy_block.png"]
                # random_img = random.choice(img_list)
                # # if random_img == "enemy1_block.png":
                # #     enemy_state = "defensive"
                # if random_img == "enemy1_idle.png":
                #     enemy_state = "idle"
                # else:
                #     enemy_state = "attack"            
                # self.image = pygame.image.load(random_img)
                # print(random_img)
                # print(enemy_state)

                # en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                # enemy_state = "defenseless"
                enemy_ai_count += 1                 
        else:
            print("within dead condition")                                      

class Healthbar():
    def __init__(self,x,y,health,maxhealth):
        self.x = x
        self.y = y
        self.health = health
        self.maxhealth = maxhealth

    def draw(self,health):
        self.health = health
        ratio = self.health/self.maxhealth
        pygame.draw.rect(screen,"red",(self.x,self.y,250,10))
        pygame.draw.rect(screen,"green",(self.x,self.y,250*ratio,10))

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse cursor is on button

        if self.rect.collidepoint(pos):
            # Mouse event for left click, 0 for left click 1 for right click
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        # draw button
        screen.blit(self.image, (self.rect.x,self.rect.y))

        return action

def reset_game():
    pl.alive = True
    en.alive = True
    pl.health = 100
    en.health = 100
    pl.rect.x = 100
    pl.rect.y = 115
    en.rect.x = 500
    en.rect.y = 115 
    pl.image = pygame.image.load(".//karate_img//player1_idle.png")
    en.image = pygame.image.load(".//karate_img//enemy1_idle.png")   

    
# instances

pl = Player(100, 150, "player", 100)
en = Player(500, 150, "enemy", 100)

pl_health = Healthbar(60, 20, pl.health, pl.maxhealth)
en_health = Healthbar(390, 20, en.health, en.maxhealth)

fight_bt = Button(screen_width //2 + 200, screen_height // 2 + 50, fight_bt_img)

run = True
while run:
    clock.tick(fps)
    # Load background
    load_bg()
    load_panel()

    # Load player
    pl.draw()
    en.draw()
    pl_health.draw(pl.health)
    en_health.draw(en.health)
    draw_text("Player", font2, green, 60, 25)
    draw_text("Computer", font2, green, 525, 25)
    if game_over == True:
        if fight_bt.draw() == True:
            print("Button Clicked")
            game_over == False
            reset_game()
            # fight_bt.draw() = True
    if countdown == 0:    
        en.enemy_ai()   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pl.move("left")
                if event.key == pygame.K_d:
                    pl.move("right")
                if event.key == pygame.K_SPACE:
                    
                    # pl.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))                
                    pl.block()
                if event.key == pygame.K_w:
                    pl.attack("punch")
                    player_state = "punch"                  
                if event.key == pygame.K_s:
                    pl.attack("kick")
                    player_state = "kick"
                if event.key == pygame.K_r:
                    pl.attack("fly")
                    player_state = "fly"
                if event.key == pygame.K_c:
                    pl.attack("duck")
                    player_state = "duck"                                
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    pl.idle_state()
                if event.key == pygame.K_d:
                    pl.idle_state()                                 
                    # pl.rect.y += 10            
                if event.key == pygame.K_SPACE:
                    pl.idle_state()                
                    # pl.rect.y += 10
                if event.key == pygame.K_w:                
                    pl.idle_state()
                    # pl.rect.y -= 50
                if event.key == pygame.K_s:                
                    pl.idle_state()
                if event.key == pygame.K_r:                
                    pl.idle_state()
                    pl.rect.y += 25
                if event.key == pygame.K_c:                
                    pl.idle_state()
                    pl.rect.y -= 25                               
        if pygame.Rect.colliderect(en.rect, pl.rect) and player_state in ("punch","kick"):
                    print("enemy collision")
                    top_txt = "Hit"
                    en.rect.x += 50
                    pl.rect.x -= 20
                    curr_time = pygame.time.get_ticks()
                    wait_time = curr_time + 1000
                    if curr_time < wait_time:
                        en.image = pygame.image.load(".//karate_img//enemy1_hit.png")
                        # en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                        en.health -= 10
        if en.rect.centerx - pl.rect.centerx  < 40 and player_state in ("fly"):
                    print("enemy collision")
                    top_txt = "Hit"
                    en.rect.x += 20
                    pl.rect.x -= 10
                    curr_time = pygame.time.get_ticks()
                    wait_time = curr_time + 1000
                    if curr_time < wait_time:
                        en.image = pygame.image.load(".//karate_img//enemy1_hit.png")
                        # en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                        en.health -= 10                    
        if en.health == 0:
            
            en.image = pygame.image.load(".//karate_img//enemy1_die.png")
            pl.image = pygame.image.load(".//karate_img//player1_win.png")
            # en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
            # en.rect.y += 10
            en.alive = False
            draw_text("You Win", font2, green, screen_width/2 - 40, screen_height - panel_height + 20)
            game_over = True

        if pl.health == 0:
            pl.image = pygame.image.load(".//karate_img//player1_die.png")
            en.image = pygame.image.load(".//karate_img//enemy1_win.png")
            # pl.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
            pl.rect.y = en.rect.y + 20
            pl.alive = False
            en.alive = False # stop enemy movement
            draw_text("You Lose", font2, green, screen_width/2 - 40, screen_height - panel_height + 20)
            game_over = True

    if countdown > 0:
        draw_text("GET READY", font2, black, screen_width/2 - 40, screen_height/2 - 70)
        draw_text(str(countdown), font2, black, screen_width/2 + 10, screen_height/2 - 30 ) 
        count_timer = pygame.time.get_ticks()
        if count_timer - last_count > 1000:
            countdown -= 1
            last_count = count_timer                                                                                                   
    pygame.display.update()
pygame.quit()
