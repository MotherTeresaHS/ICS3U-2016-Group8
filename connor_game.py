# coding: utf-8

from scene import *
import ui
from numpy import random


class ConnorGame(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        self.left_button_down = False
        self.right_button_down = False
        self.down_button_down = False
        self.up_button_down = False
        self.chr_move_speed = 20.0
        self.daggers = []
        self.dagger_throw_rate = 1
        self.attack_speed = 20.0
        self.scale_size = 0.75
        self.score = 0
        self.dead = False
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/grass.JPG',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        chr_position = Vector2()
        chr_position.x = self.screen_center_x
        chr_position.y = self.screen_center_y
        self.chr = SpriteNode('./assets/sprites/CHR.PNG',
                                    parent = self,
                                    position = chr_position,
                                    scale = self.scale_size / 2)
                                       
        left_button_position = Vector2()
        left_button_position.x = 750
        left_button_position.y = 150
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5,
                                      scale = self.scale_size)
                                       
        right_button_position = Vector2()
        right_button_position.x = 950
        right_button_position.y = 150
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5,
                                       scale = self.scale_size)
                                       
        down_button_position = Vector2()
        down_button_position.x = 850
        down_button_position.y = 50
        self.down_button = SpriteNode('./assets/sprites/down_button.png',
                                       parent = self,
                                       position = down_button_position,
                                       alpha = 0.5,
                                       scale = self.scale_size)
                                       
        up_button_position = Vector2()
        up_button_position.x = 850
        up_button_position.y = 250
        self.up_button = SpriteNode('./assets/sprites/up_button.png',
                                     parent = self,
                                     position = up_button_position,
                                     alpha = 0.5,
                                     scale = self.scale_size)
        
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Helvetica', 40),
                                     parent = self, 
                                     position = self.score_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # move spaceship if button down
        
        if self.left_button_down == True:
            chrMove = Action.move_by(-self.chr_move_speed, 
                                           0.0, 
                                           0.1)
            self.chr.run_action(chrMove)
        
        if self.right_button_down == True:
            chrMove = Action.move_by(self.chr_move_speed,
                                          0.0, 
                                          0.1)
            self.chr.run_action(chrMove)
    
        if self.down_button_down == True:
            chrMove = Action.move_by(0.0, -self.chr_move_speed, 0.0)
            
            self.chr.run_action(chrMove)
        
        if self.up_button_down == True:
            chrMove = Action.move_by(0.0, self.chr_move_speed, 0.0)
            
            self.chr.run_action(chrMove)
            
        # create more knives when there is none on the screen
        
        dagger_throw_chance = random.randint(1,120)
        if dagger_throw_chance <= dagger_throw_rate:
            self.throw_dagger()
        
        # when a dagger leaves the screen, remove it from the array
        for dagger in self.daggers:
            if dagger.position.y < -50:
                dagger.remove_from_parent()
                self.daggers.remove(dagger)
        
        # If a dagger touches the character.
        if len(self.daggers) > 0:
            for dagger_hit in self.daggers:
                if dagger_hit.frame.intersects(self.chr.frame):
                    self.chr.remove_from_parent()
                    dagger_hit.remove_from_parent()
                    self.daggers.remove(dagger_hit)
                
                # game over, show button that takes you back to character select.
                
                    self.dead = True
                    self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                                  parent = self,
                                                  position = Vector2(self.screen_center_x,
                                                                     self.screen_center_y),
                                                  alpha = 1.0,
                                                  scale = self.scale_size)
        else:
            pass
        
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if left, right, down, or up buttons are down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        
        if self.down_button.frame.contains_point(touch.location):
            self.down_button_down = True
        
        if self.up_button.frame.contains_point(touch.location):
            self.up_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        self.left_button_down = False
        self.right_button_down = False
        self.down_button_down = False
        self.up_button_down = False
    
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
    
    def throw_dagger(self):
        # dagger spawns and moves across the screen.
        
        dagger_start_position = Vector2()
        dagger_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        dagger_start_position.y = self.size_of_screen_y + 100
        
        dagger_end_position = Vector2()
        dagger_end_position.x = self.size_of_screen_x
        
        dagger_end_position.y = -100
        
        self.attacks.append(SpriteNode('./assets/sprites/knife.PNG',
                             position = dagger_start_position,
                             parent = self))
        
        # make missile move forward
        daggerMoveAction = Action.move_to(dagger_end_position.x, 
                                         dagger_end_position.y, 
                                         self.attack_speed,
                                         TIMING_SINODIAL)
        self.attacks[len(self.attacks)-1].run_action(daggerMoveAction)
