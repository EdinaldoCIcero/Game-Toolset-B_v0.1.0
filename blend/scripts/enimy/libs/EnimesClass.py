from bge import logic , events , types
import bge

#-------------------------
from mathutils import Vector
from random import randint 

#-------------------------



#--------#------#------#-------#------#------#------#------#------#------#------#------#------#
class EnimesAIBasic(types.KX_GameObject):
    def __init__(self , object , get_armature = None ):

        self.armature               = get_armature
        self.life_enimes            = 100
        self.cont_time_directions   = 0
        self.randin                 = 0
        self.x , self.y , self.z    = 0, 0, 0
        self.prop_distantenc_bool   = self["DISTENCE_ENI_TO_PLAYER"] = False


     #----------------------------------------------------------------------------------------
     #------- Ray Cast | Soltar um raio de um ponto ao outro ---------------------------------
    def rayCastCam( self ,  point_raycast , vect_x = 0 , vect_y = 0 , vect_z = 0  ):
        scene   = logic.getCurrentScene()
        m       = logic.mouse.events

        #-----------------------------------------------------
        vec_cam = point_raycast.worldOrientation * Vector([ vect_x , vect_y , vect_z ])
        cam_pos = point_raycast.worldPosition
        target  = cam_pos + vec_cam
        
        obj, hit_pos, normal = point_raycast.rayCast( target ,  point_raycast.worldPosition   )

        return obj, hit_pos, normal
        pass

    #-----------------------------------------------------------------------------------------
    #-------- Movimentação randomica simples em 4 direções -----------------------------------
    def randomMovement(self , speed = 0.100 ):
        
        dirctions         = [ "IDLE" , "FRONT"  , "BACK" , "LEFT" , "RIGHT" ]
        directions_state  = {   "IDLE"  : [ 0 , 0 ]  , 
                                "FRONT" : [ 0 , speed ] , 
                                "BACK"  : [ 0 , -speed ] , 
                                "LEFT"  : [-speed , 0 ] , 
                                "RIGHT" : [ speed , 0 ] 
                            }

        #-----------------------------#
        self.cont_time_directions += 1


        if self.cont_time_directions >= 60:
            self.randin  = randint( 0 , 4 )

            self.x , self.y = directions_state[ dirctions[ self.randin ] ] 

            self.cont_time_directions = 0

        if (self.x , self.y ) != ( 0 , 0 ) :
            vec_direction = Vector( [ self.x , self.y , self.z ] ).normalized() * speed

            self.armature.alignAxisToVect( vec_direction , 1 , 0.5 )
            self.armature.alignAxisToVect([ 0 , 0 , 1 ] , 2 , 1)
       
        self.applyMovement([ self.x , self.y , self.z ] , True )


        return {
            "DIRECTIONS_NAME"   : dirctions[ self.randin ] ,
            "DIRECTIONS_VALUES" : directions_state[ dirctions[ self.randin ] ],
            "RANDOM_NUMB"       : self.randin,
            "XYZ"               : [ self.x , self.y , self.z ],

        }

        pass
        
    #-----------------------------------------------------------------------------------------
    #------- Função para seguir o player com base e uma NavegationMesh -----------------------
    def followPlayer(self , cont , object_follow , steering_navMesh , act_track_to_armature ):
        x , y , z = object_follow.worldPosition.x , object_follow.worldPosition.y , object_follow.worldPosition.z
        vec_direction = Vector( [ x , y , z ] ).normalized() * 0.100

        if self["FOLLOW_PLAYER"] == True:

            if self.getDistanceTo( object_follow ) >= 1.150:
                self["DISTENCE_ENI_TO_PLAYER"] = True
                
                cont.activate(steering_navMesh)
                cont.activate( act_track_to_armature )
                self.applyMovement([ 0, 0.050 , 0 ] , True )

            else:
                self["DISTENCE_ENI_TO_PLAYER"] = False
                
            pass


    #-----------------------------------------------------------------------------------------
    #------- Função responsavel em adicionar atack do inimigo no player ----------------------
    def atackInPlayer( self , prop_timer_daley , delay_value , point_add_obj_atack , atack_time_end ):
        scene           = logic.getCurrentScene()
        global_dict     = bge.logic.globalDict
        #--------------------------------------

        if prop_timer_daley >= delay_value:
            new_bullet = scene.addObject( "Zombie_AtackColision" , point_add_obj_atack , atack_time_end  )
            prop_timer_daley = 0
                
        pass

    #-----------------------------------------------------------------------------------------
   
            
            
