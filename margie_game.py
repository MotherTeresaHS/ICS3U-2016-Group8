# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui
from numpy import random


class MargieGame(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2()
        self.down_button_down = False
        self.up_button_down = False
        self.left_button_down = False
        self.right_button_down = False
        self.chr_move_speed = 20.0
        self.missiles = []
        self.daggers = []
        self.dagger_attack_rate = 1 
        self.dagger_attack_speed = 20.0
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
        self.chr = SpriteNode('./assets/sprites/margie.PNG',
                                    parent = self,
                                    position = chr_position,
                                    scale = self.scale_size / 3)
                                    
                                       
        left_button_position = Vector2()
        left_button_position.x = self.screen_center_x + 235
        left_button_position.y = self.screen_center_y - 235
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5,
                                      scale = self.scale_size)
                                       
        right_button_position = Vector2()
        right_button_position.x = self.screen_center_x + 435
        right_button_position.y = self.screen_center_y - 235
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5,
                                       scale = self.scale_size)
                                       
        
        up_button_position = Vector2()
        up_button_position.x = self.screen_center_x + 335
        up_button_position.y = self.screen_center_y - 135
        self.up_button = SpriteNode('./assets/sprites/up_button.png',
                                     parent = self,
                                     position = up_button_position,
                                     alpha = 0.5,
                                     scale = self.scale_size)
        
        down_button_position = Vector2()
        down_button_position.x = self.screen_center_x + 335
        down_button_position.y = self.screen_center_y - 335
        self.down_button = SpriteNode('./assets/sprites/down_button.png',
                                       parent = self,
                                       position = down_button_position,
                                       alpha = 0.5,
                                       scale = self.scale_size)
        
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)
        
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # move connor if the left button is down, if he is at the edge of the screen, stop.
        if self.chr.position.x <= self.screen_center_x - 450:
            self.left_button_down = False
        
        if self.left_button_down == True:
            chrMove = Action.move_by(-self.chr_move_speed, 
                                           0.0, 
                                           0.1)
            self.chr.run_action(chrMove)
        
        # move connor if the right button is down, if he is at the edge of the screen, stop.
        if self.chr.position.x >= self.screen_center_x + 450:
                self.right_button_down = False
            
        if self.right_button_down == True:
            chrMove = Action.move_by(self.chr_move_speed,
                                          0.0, 
                                          0.1)
            self.chr.run_action(chrMove)
            
        # move connor if down button is down, if connor is at the edge of the screen, stop.
        if self.chr.position.y <= self.screen_center_y - 320:
                self.down_button_down = False
    
        if self.down_button_down == True:
            chrMove = Action.move_by(0.0, -self.chr_move_speed, 0.0)
            
            self.chr.run_action(chrMove)
        
        # move connor if up button is down, if connor is off the screen, stop.
        if self.chr.position.y >= self.screen_center_y + 320:
                self.up_button_down = False
                
        if self.up_button_down == True:
            chrMove = Action.move_by(0.0, self.chr_move_speed, 0.0)
            
            self.chr.run_action(chrMove)
        
        # every update, randomly check if a new dagger should be created
        dagger_create_chance = random.randint(1, 25)
        if dagger_create_chance <= self.dagger_attack_rate:
            self.add_dagger()
            
            if self.dead == True:
                pass
            
        # check every update if an dagger is off screen
        
        for dagger in self.daggers:
            if dagger.position.y > self.size_of_screen_y + 100:
                dagger.remove_from_parent()
                self.daggers.remove(dagger)
                # only subtract points if you are still alive
                if self.dead == False:
                    self.score = self.score + 1
            
            if dagger.position.y < self.size_of_screen_y - 800:
                dagger.remove_from_parent()
                self.daggers.remove(dagger)
                # only subtract points if you are still alive
                if self.dead == False:
                    self.score = self.score + 1
            
        

        # check every update to see dagger touches connor
        if len(self.daggers) > 1:
            for dagger_hit in self.daggers:
                if dagger_hit.frame.intersects(self.chr.frame):
                    self.chr.remove_from_parent()
                    dagger_hit.remove_from_parent()
                    self.daggers.remove(dagger_hit)
                    # since game over, move to next scene
                    self.dead = True
                    self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, 
                                                         self.screen_center_y),
                                      alpha = 1.0,
                                      scale = self.scale_size)
        else:
            pass
            #print(len(self.daggers))
        
        # update every frame the current score
        self.score_label.text = 'Score: ' + str(self.score)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if left or right button is down
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
        
        self.left_button_down = False
        self.right_button_down = False
        self.down_button_down = False
        self.up_button_down = False
        
        # if game over, check to go back to character select
        if self.dead == True:
            # if start button is pressed, goto game scene
            if self.back_button.frame.contains_point(touch.location):
                self.dismiss_modal_scene()
    
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
        
        
    def add_dagger(self):
        # add a new dagger to come down
        
        dagger_start_position = Vector2()
        dagger_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        dagger_start_position.y = self.size_of_screen_y + 100
        
        dagger_end_position = Vector2()
        dagger_end_position.x = dagger_start_position.x
        dagger_end_position.y = - 110
        
        self.daggers.append(SpriteNode('./assets/sprites/knife_down.PNG',
                             position = dagger_start_position,
                             parent = self))
        
        # make missile move forward
        daggerMoveAction = Action.move_to(dagger_end_position.x, 
                                         dagger_end_position.y, 
                                         self.dagger_attack_speed,
                                         TIMING_SINODIAL)
        self.daggers[len(self.daggers)-1].run_action(daggerMoveAction)
        
        # add a new dagger to go up.

        dagger_start_position = Vector2()
        dagger_start_position.x = random.randint(100, 
                                         self.size_of_screen_x - 100)
        dagger_start_position.y = self.size_of_screen_y - 800
        
        dagger_end_position = Vector2()
        dagger_end_position.x = dagger_start_position.x
        dagger_end_position.y = self.size_of_screen_y + 110
        
        self.daggers.append(SpriteNode('./assets/sprites/knife_up.PNG',
                             position = dagger_start_position,
                             parent = self))
        
        # make missile move forward
        daggerMoveAction = Action.move_to(dagger_end_position.x, 
                                         dagger_end_position.y, 
                                         self.dagger_attack_speed,
                                         TIMING_SINODIAL)
        self.daggers[len(self.daggers)-1].run_action(daggerMoveAction)
