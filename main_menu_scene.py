# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from character_select_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add MT blue background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.start_button = SpriteNode('./assets/sprites/start.png',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.75)
                                       
        logo_position = Vector2()
        logo_position.x = self.screen_center_x
        logo_position.y = self.screen_center_y + 100
        self.logo = SpriteNode('./assets/sprites/DKM_dark.PNG',
                                      parent = self,
                                      position = logo_position,
                                      scale = 0.75)
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
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(CharacterSelectScene())
    
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
    
