# coding: utf-8

from scene import *
import ui

from connor_game_b import *
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
        
        john_button_position = self.size/2
        john_button_position.y = john_button_position.y - 80
        self.john_button = SpriteNode('./assets/sprites/blue_block.PNG',
                                            parent = self,
                                            position = john_button_position,
                                            scale = 0.30)
        
        connor_button_position = self.size/2
        connor_button_position.y = connor_button_position.y - 200
        connor_button_position.x = connor_button_position.x - 150
        self.connor_button = SpriteNode('./assets/sprites/connor.PNG',
                                      parent = self,
                                      position = connor_button_position,
                                      scale = 0.30)
        
        sheldon_button_position = self.size/2
        sheldon_button_position.y = sheldon_button_position.y - 200
        sheldon_button_position.x = sheldon_button_position.x + 150
        self.sheldon_button = SpriteNode('./assets/sprites/sheldon.PNG',
                                       parent = self,
                                       position = sheldon_button_position,
                                       scale = 0.30)
        
        back_button_position = self.size/2
        back_button_position.y = back_button_position.y - 335
        back_button_position.x = back_button_position.x - 470
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                      parent = self,
                                      position = back_button_position,
                                      scale = 0.50)
        
        kyle_button_position = self.size/2
        kyle_button_position.y = kyle_button_position.y - 80
        kyle_button_position.x = kyle_button_position.x + 300
        self.kyle_button = SpriteNode('./assets/sprites/kyle.PNG',
                                     parent = self,
                                     position = kyle_button_position,
                                     scale = 0.30)
        
        margie_button_position = self.size/2
        margie_button_position.y = margie_button_position.y - 80
        margie_button_position.x = margie_button_position.x - 300
        self.margie_button = SpriteNode('./assets/sprites/margie.PNG',
                                      parent = self,
                                      position = margie_button_position,
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
        if self.john_button.frame.contains_point(touch.location):
            self.present_modal_scene(JohnGame())
        
        if self.connor_button.frame.contains_point(touch.location):
            self.present_modal_scene(ConnorGame())
        
        if self.sheldon_button.frame.contains_point(touch.location):
            self.present_modal_scene(SheldonGame())
        
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        
        if self.kyle_button.frame.contains_point(touch.location):
            self.present_modal_scene(KyleGame())
        
        if self.margie_button.frame.contains_point(touch.location):
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
