from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty,StringProperty
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.uix.label import Label
from kivy.core.audio import Sound, SoundLoader
from kivy.config import Config
 
class Holeobs(Widget):    
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos   


class Barrobs(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Birdobs(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos        

class Player(Image):
    
    pl = ObjectProperty(None)
    #hole_obs = ObjectProperty(None)
    #  
    def on_touch_up(self, touch):
        self.y = self.y - 90
        super(Player,self).on_touch_up(touch)    
   

    def on_touch_down(self, touch):
        self.y = self.y + 90
        super(Player,self).on_touch_down(touch)    





       
    

class Background(Widget):
    pl = ObjectProperty(0)
    score = NumericProperty(0)    
    hole_obs = ObjectProperty(0)
    bar_obs = ObjectProperty(0)
    bird_obs = ObjectProperty(0)   
    bg_texture = ObjectProperty(None)

    def move_obs(self):
        self.hole_obs.velocity = Vector(-6,0)
        self.bar_obs.velocity = Vector(-6,0)
        self.bird_obs.velocity = Vector(-6,0)

        


    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.bg_texture = Image(source='road_bg.jpg').texture
        self.bg_texture.wrap = 'repeat'
        self.bg_texture.uvsize = (Window.width/self.bg_texture.width,-1)
        





    def update(self,time):
        self.hole_obs.move()
        self.bar_obs.move()
        self.bird_obs.move()
        self.bg_texture.uvpos = ((self.bg_texture.uvpos[0] + time/6)%Window.width,self.bg_texture.uvpos[1])
        
        texture = self.property('bg_texture')
        texture.dispatch(self)

        if self.hole_obs.x < 0:
            self.hole_obs.x = self.width + 50
            self.score += 10

        if self.bar_obs.x < 0:
            self.bar_obs.x = self.width + 50            
            self.score += 10
        if self.bird_obs.x < 0:
            self.bird_obs.x = self.width + 50

        if self.hole_obs.collide_widget(self.pl):
            
            self.game_over()

        if self.bar_obs.collide_widget(self.pl):
            self.game_over()
        
        if self.bird_obs.collide_widget(self.pl):
            self.game_over()                    

             


    def pause(self):
        self.pl.y = self.pl.y + 90
        self.clk.cancel()

    def resume(self):
        self.pl.y = self.pl.y + 90
        self.clk.cancel()    
            

    def load_game(self):
        self.clk = Clock.schedule_interval(self.update,1.0/60.0)

    def game_over(self):
        self.clk.cancel()
        self.govr_txt = Label(text='GAME OVER', pos = (Window.width/2,Window.height/2),font_size=40,size_hint=(None,None))
        self.add_widget(self.govr_txt)
        self.hole_obs.x = self.hole_obs.x + 1300
        self.bird_obs.x = self.bird_obs.x + 1300
        self.bar_obs.x = self.bar_obs.x + 1300
        self.pl.x = self.pl.x  - 100
        self.pl.y = self.pl.y + 90

    def restart(self):
        self.pl.x = self.pl.x  + 100
        self.remove_widget(self.govr_txt)
        self.score = 0
        self.load_game()




class FoxJumpApp(App):
    def start_game(self):
        Config.set ('kivy', 'window_icon', 'fox_skate.png')
        Window.fullscreen = 'auto'
        game = Background()
        self.root.ids.Background.move_obs()
        #self.clk = Clock.schedule_interval(self.root.ids.Background.update,1.0/60.0)
        self.root.ids.Background.load_game()
        self.game_sound()
    def game_sound(self):
        self.sound = SoundLoader.load("flourish.wav")
        self.sound.play()        

      









FoxJumpApp().run()

