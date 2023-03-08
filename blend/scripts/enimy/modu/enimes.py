from bge import logic,events, types
import bge


#--------------------------------------------
from scripts.enimy.libs.EnimesClass import EnimesAIBasic



#scripts.enimy.modu.enimes.start

#--------------------------------------------
tc    = logic.keyboard.events
m     = logic.mouse.events
scene = logic.getCurrentScene()



#--------------------------------------------
#-- Função que contém as propriedades de objetos e referentes a objetos
def properties(cont , own):

    aramture = own["armature"]  = [armature for armature in own.children if "armature" in armature ][0],

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
    properties( cont , own )

    emimes    = EnimesAIBasic( own , get_armature = so["EnimeSuzanne"] )


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
    own.randomMovement( speed = 0.050 )


    pass