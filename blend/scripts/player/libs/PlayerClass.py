from bge import logic , events , types
from mathutils import Vector
import bge 

#-----------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------
class PlayerController(types.KX_GameObject):
    def __init__(self, object , get_player_armature = None ):
        
        self.fisic_constraints           = bge.constraints.getCharacter( self )
        self.player_armature             =  get_player_armature
   
        self.trav_front_player           = self["TR_FRONT"] = False 

        self.mov_state                   = [ "IS_WALK" , "IS_RUN" , "IS_IDLE"]
        self.mouse_state_names           = [ "MOUSE_UP" , "MOUSE_DOWN" ]

        self.speed_movement              = 0.100
        self.in_movement                 = False
        self.movement_states             = ""

        self.mouse_state_pressed         = False
        self.mouse_state_pressed_inverse = True
        self.mouse_state                 = ""

        self.delay_blendin_return        = 0
        self.delay_tr_blendin            = False
       

    #-----------------------------------------------------------------------------------------
    def delayTimer(self , delay ):
        self.delay_blendin_return += 1

        if self.delay_blendin_return >= delay :
            self.delay_tr_blendin   = True
            self.delay_blendin_return = 0

        else:
            self.delay_tr_blendin = False

        return self.delay_tr_blendin

        pass


    #------------------------------------------------------------------------------------
    def cameraColision( self , obj_focus , obj_root , obj_cam , prop_name_colision):
        m       = logic.mouse.events
        ray     = obj_focus.rayCast( obj_root , obj_focus , obj_focus.getDistanceTo(obj_root), prop_name_colision )
        #------------------------------

        if ray[0] != None:
            obj_cam.worldPosition = ray[1]
            

        if ray[0] == None:
            obj_cam.worldPosition = obj_root.worldPosition
    
        pass
    

    #-----------------------------------------------------------------------------------------
    def setNewValuesActionsDict(self , name_state , dict_new_actions = { "name" : [ "name" , 1 , 2 ] }  ):
        return dict_new_actions[ name_state ]
        pass


    #-----------------------------------------------------------------------------------------
    def setNewValuesActionsList(self , numb_state , list_new_actions ):
        return list_new_actions[ numb_state ]
        pass


    #-----------------------------------------------------------------------------------------
    def setMouseStateName(self , new_name = [ "MOUSE_UP" , "MOUSE_DOWN" ] , numb_return = 0 ):
        self.mouse_state_names = new_name
        return self.mouse_state_names , numb_return
        pass


    def rayCastPoint( self , point_raycast , vect_x = 0 , vect_y = 0 , vect_z = 0  ):
        scene   = logic.getCurrentScene()
        m       = logic.mouse.events
        #-----------------------------------------------------
        vec_cam = point_raycast.worldOrientation * Vector([  vect_x , vect_y , vect_z  ])
        cam_pos = point_raycast.worldPosition
        target  = cam_pos + vec_cam
        
        obj, hit_pos, normal = point_raycast.rayCast( target ,  point_raycast.worldPosition   )


        return obj, hit_pos, normal
        pass
    

    #-----------------------------------------------------------------------------------------
    def aimingMouseState(self , mouse_key_type = "NO_TAB" ,  mouse_key = "left" ):
        mouse = logic.mouse.events
        #--------------------------
        mouse_keys = {  "IN_TAB" : { "left" : mouse[events.LEFTMOUSE] in [1,1] , "right" : mouse[events.RIGHTMOUSE] in [1,1] },
                        "NO_TAB" : { "left" : mouse[events.LEFTMOUSE] , "right" : mouse[events.RIGHTMOUSE] },
                     }


        if mouse_keys[ mouse_key_type ][ mouse_key ]:
            self.mouse_state_pressed         = True
            self.mouse_state_pressed_inverse = False
            self.mouse_state                 = self.mouse_state_names[1]

        else:
            self.mouse_state_pressed         = False
            self.mouse_state_pressed_inverse = True 
            self.mouse_state                 = self.mouse_state_names[0]





        return { "MOUSE_EVENT"       : mouse_keys[ mouse_key_type ][ mouse_key ] , # event em si 
                 "MOUSE_STATE_DOWN"  : [ self.mouse_state_pressed,  self.mouse_state_pressed_inverse  ] , # = True or False <---> False or True 
                 "MOUSE_STATE_NAMES" : self.mouse_state 
               }



        pass


    #----------------------------------------------------------------------------------------
    def playerMovement(self , cam_orientation , speed_walk = 0.050 , speed_run = 0.160 ,  activate_run = True ):
        tc    = logic.keyboard.events
        w , s = tc[events.WKEY], tc[events.SKEY]
        a , d = tc[events.AKEY], tc[events.DKEY]
        shift = tc[events.LEFTSHIFTKEY]
        #-----------------------------#
        x,y,z = 0 , 0 , 0
        

        y = w - s 
        x = d - a

        if shift and activate_run == True :
            self.speed_movement = speed_run
            self.movement_states = self.mov_state[1]
        else:
            self.speed_movement = speed_walk
            self.movement_states = self.mov_state[0]

        #----
        if x != 0 or y != 0:
            self.in_movement = True
        else:
            self.in_movement = False
            self.movement_states = self.mov_state[2]


        vec = Vector([x,y,z]).normalized() * self.speed_movement
        self.fisic_constraints.walkDirection =  cam_orientation.worldOrientation * vec  #self.worldOrientation * vec

        return  { "X" : x , "Y" : y ,

                  "W" : w , 
                  "S" : s , 
                  "A" : a , 
                  "D" : d ,

                  "VECTOR"          : vec,
                  "IN_MOVE"         : self.in_movement,
                  "STATE_MOVEMENT"  : self.movement_states

                  }


    #-----------------------------------------------------------------------------------------
    def playerDirection(self):
        direction = self.fisic_constraints.walkDirection
        #-----------------------------#
        if self.player_armature != None:
            if direction.length != 0:
                self.player_armature.alignAxisToVect(direction, 1,0.5)
                self.player_armature.alignAxisToVect([0,0,1], 2, 1)
        else:
            #print("Not armature")
            pass

        return [ direction , direction.length ]


    #-----------------------------------------------------------------------------------------
    def playerSetFrontAimDirecion( self , cont , act_cam_mouse_x , object_direciton , act_track_to_capsula , act_track_to_armature ):
        mouse_events    = logic.mouse.events
        tc    = logic.keyboard.events
        w , s = tc[events.WKEY], tc[events.SKEY]
        
        #-----------------------------#
        cont.activate( act_cam_mouse_x )

        if w :
            cont.activate(act_track_to_capsula)
            act_track_to_capsula.object = object_direciton


        if mouse_events[events.RIGHTMOUSE]:
            self["TR_FRONT"] = True
            cont.activate(act_track_to_capsula)
            cont.activate(act_track_to_armature)
            act_track_to_capsula.object = object_direciton
            act_track_to_armature.object = object_direciton

        else:
            self["TR_FRONT"] = False
            cont.deactivate(act_track_to_capsula)
            cont.deactivate(act_track_to_armature)

        pass


        return self["TR_FRONT"]


    #-----------------------------------------------------------------------------------------
    def fpsMouseLook( self , cont , sensor_movement , act_mouse_x , act_mouse_y ):
        if sensor_movement.positive:
            cont.activate( act_mouse_x )
            cont.activate( act_mouse_y )

        pass
    
    #-----------------------------------------------------------------------------------------
    def charJump(self ):
        keyboard    = logic.keyboard.events
        space       = keyboard[events.SPACEKEY]
        #-------------------------------#
        if space in [1,1]:
            self.fisic_constraints.jump()
    
        pass
    
    #-----------------------------------------------------------------------------------------
