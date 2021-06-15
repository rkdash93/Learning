#1 create an app
#2 create the game
#3 build the app
#4 run the game



from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty,StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import Sound, SoundLoader


class Obstacle_cloud(Widget):
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Obstacle_ball(Widget):
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        

class Obstacle_bird(Widget):
    score = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos    


class Player(Widget):   
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)
    #Latest postiton = current velocity + current position

    def jump(self):
        self.pos = Vector(*self.velocity) + self.pos
    def obs_collide(self,ball):
        if self.collide_widget(ball):
            quit()
            #game_over()
            #pass             
 

        


class FoxJumpGame(Widget):
    bg_texture=ObjectProperty(None)
    pl=ObjectProperty(0)
    obs_ball = ObjectProperty(0)
    obs_cloud = ObjectProperty(0)
    obs_bird = ObjectProperty(0) 

    def load_bg(self):
        
        self.bg_texture = Image(source='background.jpg').texture
        self.bg_texture.wrap = 'repeat'
        self.bg_texture.uvsize = (Window.width/self.bg_texture.width,-1)        
        self.sound = SoundLoader.load("flourish.wav")
        self.sound.play()
        


    def move_ball(self):
        self.obs_ball.velocity = Vector(0,0)
        self.obs_cloud.velocity = Vector(-7,0)
        self.obs_bird.velocity = Vector(-4,0)

    def update(self,time):
        self.obs_ball.move()
        self.obs_cloud.move()
        self.obs_bird.move()
        self.bg_texture.uvpos = ((self.bg_texture.uvpos[0] + time/6)%Window.width,self.bg_texture.uvpos[1])
        #redraw on canvas
        texture = self.property('bg_texture')
        texture.dispatch(self)

        #self.pl.obs_collide(self.obs_ball)
        #self.pl.obs_collide(self.obs_cloud)

        if self.pl.collide_widget(self.obs_ball):
            self.game_over()

        if self.obs_ball.x < 0:
            self.obs_ball.x = self.width + 50
            self.obs_ball.score += 10

        if self.obs_cloud.x < 0:
            self.obs_cloud.x = self.width + 50

        if self.obs_bird.x < 0:
            self.obs_bird.x = self.width + 50            


                
        

    def on_touch_up(self, touch):
        self.pl.y = self.pl.y - 200
        super(FoxJumpGame,self).on_touch_up(touch)        

    def on_touch_down(self, touch):
        self.pl.y = self.pl.y + 200
        self.sound = SoundLoader.load("Jump.wav")
        self.sound.play()    
        super(FoxJumpGame,self).on_touch_down(touch)

       
    def game_over(self):
        #self.frames = Clock.schedule_interval(self.update,1.0/60.0)
        self.frames.cancel()
        govr_txt = Label(text='GAME OVER', pos = (350,350),font_size=30)
        self.add_widget(govr_txt)
        #self.remove_widget(Pl)
    
    def load_game(self,obj):
        self.frames = Clock.schedule_interval(self.update,1.0/60.0)

    def quit_game(self,obj):
        quit()

       

class FoxJumpApp(App):
    def build(self):
        self.icon = 'fox_skate.png'
        game = FoxJumpGame()
        #game.load_bg()
        game.move_ball()
        quit_bt=Button(text='X',size=(30,30),pos=(750,550))
        quit_bt.bind(on_release=game.quit_game)
        restart_bt=Button(text='Restart',size=(100,30),pos=(600,550))
        restart_bt.bind(on_release=game.load_game)              
        game.add_widget(quit_bt)
        #Window.borderless = True
        return game


FoxJumpApp().run()       

