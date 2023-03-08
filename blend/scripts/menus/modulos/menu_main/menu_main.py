from bge import logic,events , types
import bgui
import bgui.bge_utils
import bge
import aud


#-----------------------------------------------------
from scripts.menus.libs.MenuMain import MenuMainLayoutOne

#-----------------------------------------------------







def start(cont):
    own         = cont.owner
    mouse       = bge.logic.mouse
    scene       = logic.getCurrentScene()
    global_dict = bge.logic.globalDict

    #---------------------------
    global_dict["INIT_GAME"] = False


    sy = own['sys'] = bgui.bge_utils.System('../../themes/default')
    own['sys'].load_layout( MenuMainLayoutOne , None )

    pass



def update(cont):
    own             = cont.owner
    scene           = logic.getCurrentScene()
    global_dict     = bge.logic.globalDict
    keyboard_events = logic.keyboard.events
    mouse_events    = logic.mouse.events 
    sen , act , so  = cont.sensors , cont.actuators , scene.objects

    #------ SENSORS ---------

    #----- ACTUATORS --------
    SetGameScene = act["SetGameScene"]

    #------ OBJECTS ---------

    #------------------------
    
    if global_dict["INIT_GAME"] == True:
        cont.activate( SetGameScene )


    #if not "sys" in own:
   # else:
    own['sys'].run()
 
