from bge import logic , events , types
import bge 
#-------------------------
from mathutils import Vector


#-------------------------

#------------------------


class PlayerController(types.KX_GameObject):
    def __init__(self, object , get_player_armature = None ):


        self.fisic_constraints =  bge.constraints.getCharacter( self )
        self.player_armature   =  get_player_armature
   
   
    #-----------------------------------------------------------------------------------------
    def playerMovement(self , speed ):
        tc    = logic.keyboard.events
        w , s = tc[events.WKEY], tc[events.SKEY]
        a , d = tc[events.AKEY], tc[events.DKEY]
        #-----------------------------#
        x,y,z = 0,0,0

        y = w - s 
        x = d - a
        
        vec = Vector( [ x , y , z ] ).normalized() * speed
        self.fisic_constraints.walkDirection = self.worldOrientation * vec
        

        return { "X"      : x , 
                 "Y"      : y ,
                 "VECTOR" : vec

               }


    #-----------------------------------------------------------------------------------------
    def charDirection(self):
        direction = self.fisic_constraints.walkDirection
        #-----------------------------#

        if direction.length != 0:
            self.player_armature.alignAxisToVect(direction, 1,0.5)
            self.player_armature.alignAxisToVect([0,0,1], 2, 1)
    

    #-----------------------------------------------------------------------------------------
    def charJump(self , keyboard):
        space = keyboard[events.SPACEKEY]
        #-------------------------------#
        if space in [1,1]:
            self.fisic_constraints.jump()
            
