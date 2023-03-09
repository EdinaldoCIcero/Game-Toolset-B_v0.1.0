from bge import logic,events, types
import bge


from scripts.player.libs.PlayerClass import PlayerController



# -----------------------
def getMouseAngleY( cont , own , sen_mouse_movement , act_mouse_y ):

    if sen_mouse_movement.positive:
        cont.activate( act_mouse_y ) 
        own["MOUSE_Y_ANGLE"] = act_mouse_y.angle[1] + 90
    pass


#--------------------------------
def setMouseAngleAction(cont , own , armature_player ):
    mouse   = logic.mouse.events
    tc      = logic.keyboard.events
    keys    = tc[events.WKEY] or tc[events.SKEY] or tc[events.AKEY] or tc[events.DKEY] 
    shift = tc[events.LEFTSHIFTKEY]
    #--------------------------------
    

    if mouse[events.RIGHTMOUSE]:
        armature_player.playAction( "Player_Pistola_AIM" , 5 , 5 , priority = 4 , layer = 2 )
        armature_player.playAction( "Player_AIM_Angle"  , own["MOUSE_Y_ANGLE"] , own["MOUSE_Y_ANGLE"] , layer = 3 )

        if keys:
            armature_player.playAction( "Player_WALK_Pernas" , 1 , 32 , layer = 4 )
            
        else:
            armature_player.playAction( "Player_WALK_Pernas" , 10 , 10 , priority = 2  , layer = 4 )


    elif keys:
        if shift:
            armature_player.playAction( "Player_Run" , 1 , 20 , layer = 1 )
        
        else:armature_player.playAction( "Player_WALK_Pistola" , 1 , 32 , layer = 1 )



    else:
        armature_player.playAction( "Player_WALK_Pistola" , 10 , 10 , priority = 2 , layer = 2 )


    pass



#--------------------------------------------
#-- Função que contém as propriedades de objetos e referentes a objetos
def properties(cont , own):
    name = "nada" 

    return { "Nome" : name ,
            "armature_player" : [armt for armt in own.children if "armature_player" in armt ][0]
           }
    pass


#--------------------------------------------
#--- Função start 
def start(cont):
    own   = cont.owner
    scene = logic.getCurrentScene()
    so    = scene.objects
    #------ SENSORS ---------
    #----- ACTUATORS -------- 
    #------ OBJECTS ---------
    #------------------------
    propertie   = properties(cont , own)

    player      = PlayerController( own , get_player_armature = propertie["armature_player"] )


    pass

#--------------------------------------------
#---- Função de update - 
def update(cont):
    own             = cont.owner
    scene           = logic.getCurrentScene()
    global_dict     = bge.logic.globalDict
    keyboard_events = logic.keyboard.events 
    mouse_events    = logic.mouse.events
    sen , act , so  = cont.sensors , cont.actuators , scene.objects

    #------ SENSORS ---------
    MouseMovement = sen["MouseMovement"]

    #----- ACTUATORS --------
    MouseX_Capsula  = act["MouseX_Capsula"]
    MouseX_Cam      = act["MouseX_Cam"]
    MouseY_Cam      = act["MouseY_Cam"]

    TrackTo_Capsula  = act["TrackTo_Capsula"]
    TrackTo_armature = act["TrackTo_armature"]
    
    #------ OBJECTS ---------
    EmptyPlayerFront = so["EmptyPlayerFront"]
    LookY            = so["LookY"]

    #------------------------
    propertie = properties(cont , own)
   

    #getMouseAngleY( cont , own , sen_mouse_movement = MouseMovement , act_mouse_y = MouseY_Cam )
    #setMouseAngleAction(cont , own , armature_player = propertie["armature_player"] )

    stat_movemtn = own.playerMovement(  cam_orientation = LookY , speed_walk = 0.040 , speed_run = 0.160 ,  activate_run = True  )


    tr = own.playerSetFrontAimDirecion(  cont,
                            act_cam_mouse_x         = MouseX_Cam,
                            object_direciton        = EmptyPlayerFront , 
                            act_track_to_capsula    = TrackTo_Capsula, 
                            act_track_to_armature   = TrackTo_armature 
                            )
                            

    if tr == False:
        own.playerDirection()