from bge import logic,events, types
import bge


from scripts.player.libs.PlayerClass import PlayerController


tc    = logic.keyboard.events
m     = logic.mouse.events
scene = logic.getCurrentScene()



#--------------------------------------------
#-- Função que contém as propriedades de objetos e referentes a objetos
def properties(cont , own):
    name = "nada" 

    return { "Nome" : name      
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
    propertie = properties(cont , own)

    print( propertie )

    
    player = PlayerController( own , get_player_armature = None )



    pass

#--------------------------------------------
#---- Função de update - 
def update(cont):
    own             = cont.owner
    scene           = logic.getCurrentScene()
    global_dict     = bge.logic.globalDict
    keyboard_events = logic.keyboard.events , 
    mouse_events    = logic.mouse.events 
    sen , act , so  = cont.sensors , cont.actuators , scene.objects

    #------ SENSORS ---------
    #----- ACTUATORS --------
    #------ OBJECTS ---------
    #------------------------
    own.playerMovement( speed = 0.100)

   
    
    pass