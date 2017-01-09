# coding: utf-8

from scene import *
import ui

from connor_game import *
from john_game import *
from sheldon_game import *
from kyle_game import *
from margie_game import *

class CharacterSelectScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.background = SpriteNode(position = self.size / 2,
                                     color = 'white',
                                     parent = self,
                                     size = self.size)
        
        blue_block_button_position = self.size/2
        blue_block_button_position.y = blue_block_button_position.y - 80
        self.blue_block_button = SpriteNode('./assets/sprites/blue_block.PNG',
                                            parent = self,
                                            position = blue_block_button_position,
                                            scale = 0.30)
        
        frog_button_position = self.size/2
        frog_button_position.y = frog_button_position.y - 200
        frog_button_position.x = frog_button_position.x - 150
        self.frog_button = SpriteNode('./assets/sprites/CHR.PNG',
                                      parent = self,
                                      position = frog_button_position,
                                      scale = 0.30)
        
        snake_button_position = self.size/2
        snake_button_position.y = snake_button_position.y - 200
        snake_button_position.x = snake_button_position.x + 150
        self.snake_button = SpriteNode('./assets/sprites/snake.PNG',
                                       parent = self,
                                       position = snake_button_position,
                                       scale = 0.30)
        
        back_button_position = self.size/2
        back_button_position.y = back_button_position.y - 335
        back_button_position.x = back_button_position.x - 470
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                      parent = self,
                                      position = back_button_position,
                                      scale = 0.50)
        
        tim_button_position = self.size/2
        tim_button_position.y = tim_button_position.y - 80
        tim_button_position.x = tim_button_position.x + 300
        self.tim_button = SpriteNode('./assets/sprites/tim.PNG',
                                     parent = self,
                                     position = tim_button_position,
                                     scale = 0.30)
        
        girl_button_position = self.size/2
        girl_button_position.y = girl_button_position.y - 80
        girl_button_position.x = girl_button_position.x - 300
        self.girl_button = SpriteNode('./assets/sprites/girl.PNG',
                                      parent = self,
                                      position = girl_button_position,
                                      scale = 0.30)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        if self.blue_block_button.frame.contains_point(touch.location):
            self.present_modal_scene(JohnGame())
        
        if self.frog_button.frame.contains_point(touch.location):
            self.present_modal_scene(ConnorGame())
        
        if self.snake_button.frame.contains_point(touch.location):
            self.present_modal_scene(SheldonGame())
        
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        
        if self.tim_button.frame.contains_point(touch.location):
            self.present_modal_scene(KyleGame())
        
        if self.girl_button.frame.contains_point(touch.location):
            self.present_modal_scene(MargieGame())
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
