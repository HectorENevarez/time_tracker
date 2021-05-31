import os
import kivy 
kivy.require("1.9.1") 
      
from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout 

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '200')

from clocking.clock_in import clock_in
from clocking.clock_out import clock_out
  
red = [1, 0, 0, 1] 
green = [0, 1, 0, 1] 
      
class Clocking(App): 
          
    def build(self): 
        rl = RelativeLayout(size =(300, 300)) 

        btn1 = Button(text ="Clock In",
                    background_color = green, 
                    font_size = 32,
                    pos_hint ={'center_x':0.25, 'center_y':0.5}, 
                    size_hint =(0.5, 1))
        btn1.bind(on_press = clock_in) 
  
        btn2 = Button(text ="Clock Out", 
                    background_color = red, 
                    font_size = 32,
                    pos_hint ={'center_x':0.75, 'center_y':0.5}, 
                    size_hint =(0.5, 1)) 
        btn2.bind(on_press = clock_out)

        rl.add_widget(btn1)
        rl.add_widget(btn2)

        os.system("clear")
        return rl 
  
if __name__ == '__main__':
    root = Clocking() 
    root.run() 