import bge
from collections import OrderedDict
from mathutils import Vector
#from random import randint


class MenuMainController(bge.types.KX_PythonComponent):

    args = OrderedDict((

                        ( "@ Background Colors" , ""),

                        ( "Alpha"           , 0.20   ),
                        ( "R_Color"         , 0.0    ),
                        ( "G_Color"         , 0.0    ),
                        ( "B_Color"         , 0.0    ),

                        ))



    def start(self, args):
        self.scene              = bge.logic.getCurrentScene()
        self.tc                 = bge.logic.keyboard.events
        self.global_Dict        = bge.logic.globalDict
        
        #---------------------------------------------------
        self.Alpha      = args["Alpha"]
        self.R_Color    = args["R_Color"]
        self.G_Color    = args["G_Color"]
        self.B_Color    = args["B_Color"]

        #---------------------------------------------------
        self.global_Dict["MENU_MAIN_R_COLOR"]   = self.R_Color
        self.global_Dict["MENU_MAIN_G_COLOR"]   = self.G_Color
        self.global_Dict["MENU_MAIN_B_COLOR"]   = self.B_Color
       

        pass




    def update(self):
        tc       = bge.logic.keyboard.events
        m        = bge.logic.mouse.events
        #-----------------------------------
        self.global_Dict["MENU_MAIN_ALPHA"]     = self.Alpha
        #-----------------------------------
        pass
