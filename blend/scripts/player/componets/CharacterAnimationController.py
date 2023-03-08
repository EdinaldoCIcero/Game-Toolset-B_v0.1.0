import bge
from collections import OrderedDict
from mathutils import Vector
#from random import randint



class Animator(bge.types.KX_PythonComponent):




    args = OrderedDict((

                        ( "_#SetActionsValues#_" , "_#SetActionsValues#_"),

                        ( "Action_Idle"         , ""   ),
                        ( "Action_Walk"         , ""   ),
                        ( "Action_Run"          , ""   ),
                        ( "Action_Jump"         , ""   ),
                        

                        ( "Idle_frame_start"   , 0   ),
                        ( "Idle_frame_end"     , 0   ),

                        ( "Walk_frame_start"   , 0   ),
                        ( "Walk_frame_end"     , 0   ),

                        ( "Run_frame_start"    , 0   ),
                        ( "Run_frame_end"      , 0   ),

                        ( "Jump_frame_start"   , 0   ),
                        ( "Jump_frame_end"     , 0   ),

                        ( "_#SetsValues#_" , "_#SetsValues#_"),

                        ( "activateJump"          , True  ),
                        ( "activateJRun"          , True  ),

                        ( "ActionsBlendin"        , 0   ),


                        ( "_#Get_Values#_" , "_#Get_Values#_"),

                        ("SetIdComponent"           , "ID_KEYS_ACTIONS"),

                        ("GetKeyboardsController"   , True ),
                        ("GetKeyboardsID"           , "ID_KEYS" ),
                        

                        ( "_#keyboards_Actions#_" , "_#keyboards_Actions#_"),

                        ( "keyboardMoveFront"     , "w"  ) ,
                        ( "keyboardMoveBack"      , "s"  ) ,
                        ( "keyboardMoveLeft"      , "d"  ) ,
                        ( "keyboardMoveRight"     , "a"  ) ,

                        ( "keyboardJump"          , "space" ),
                        ( "keyboardRun"           , "left_shift" ),



                        ))





    #---------------------------------------------------------------
    def keyboardDict(self):

        dictkeys = {    # Alphabet keys 
                        "a" :  bge.events.AKEY,
                        "b" :  bge.events.BKEY,
                        "c" :  bge.events.CKEY,
                        "d" :  bge.events.DKEY,
                        "e" :  bge.events.EKEY,
                        "f" :  bge.events.FKEY,
                        "g" :  bge.events.GKEY,
                        "h" :  bge.events.HKEY,
                        "i" :  bge.events.IKEY,
                        "j" :  bge.events.JKEY,
                        
                        "k" :  bge.events.KKEY,
                        "l" :  bge.events.LKEY,
                        "m" :  bge.events.MKEY,
                        "n" :  bge.events.NKEY,
                        "o" :  bge.events.OKEY,
                        "p" :  bge.events.PKEY,
                        "q" :  bge.events.QKEY,
                        "r" :  bge.events.RKEY,
                        "s" :  bge.events.SKEY,
                        "t" :  bge.events.TKEY,
                        "u" :  bge.events.UKEY,
                        "v" :  bge.events.VKEY,
                        "w" :  bge.events.WKEY,
                        "x" :  bge.events.XKEY,
                        "y" :  bge.events.YKEY,
                        "z" :  bge.events.ZKEY,

                        # Other Keys 
                        
                        "acent_grave"   : bge.events.ACCENTGRAVEKEY,
                        "back_slash"    : bge.events.BACKSLASHKEY ,
                        "back_space"    : bge.events.BACKSPACEKEY,
                        "comma"         : bge.events.COMMAKEY,
                        "del"           : bge.events.DELKEY,
                        "end"           : bge.events.ENDKEY,
                        "equal"         : bge.events.EQUALKEY,
                        "esc"           : bge.events.ESCKEY,
                        "home"          : bge.events.HOMEKEY,
                        "insert"        : bge.events.INSERTKEY,
                        "left_bracket"  : bge.events.LEFTBRACKETKEY,
                        "linefeed"      : bge.events.LINEFEEDKEY,
                        "minus"         : bge.events.MINUSKEY,
                        "page_down"     : bge.events.PAGEDOWNKEY,
                        "page_up"       : bge.events.PAGEUPKEY,
                        "pause"         : bge.events.PAUSEKEY,
                        "period"        : bge.events.PERIODKEY,
                        "quote"         : bge.events.QUOTEKEY,
                        "right_bracket" : bge.events.RIGHTBRACKETKEY,
                        "enter"         : bge.events.ENTERKEY,
                        "semicolon"     : bge.events.SEMICOLONKEY,
                        "slash"         : bge.events.SLASHKEY,
                        "space"         : bge.events.SPACEKEY,
                        "tab"           : bge.events.TABKEY,

                        # Modifiers Keys 
                        "caps_lock"     : bge.events.CAPSLOCKKEY,
                        "left_ctrl"     : bge.events.LEFTCTRLKEY,
                        "left_alt"      : bge.events.LEFTALTKEY,
                        "right_alt"     : bge.events.RIGHTALTKEY,
                        "right_ctrl"    : bge.events.RIGHTCTRLKEY,
                        "right_shift"   : bge.events.RIGHTSHIFTKEY,
                        "left_shift"    : bge.events.LEFTSHIFTKEY,


                        # Arrow Keys 

                        "left_arrow"    : bge.events.LEFTARROWKEY,
                        "down_arrow"    : bge.events.DOWNARROWKEY,
                        "right_arrow"   : bge.events.RIGHTARROWKEY,
                        "up_arrow"      : bge.events.UPARROWKEY,

                        # Number keys

                        "0"     : bge.events.ZEROKEY,
                        "1"     : bge.events.ONEKEY,
                        "2"     : bge.events.TWOKEY,
                        "3"     : bge.events.THREEKEY,
                        "4"     : bge.events.FOURKEY,
                        "5"     : bge.events.FIVEKEY,
                        "6"     : bge.events.SIXKEY,
                        "7"     : bge.events.SEVENKEY,
                        "8"     : bge.events.EIGHTKEY,
                        "9"     : bge.events.NINEKEY,

                        # Numberpad Keys

                        "pad_0" : bge.events.PAD0,
                        "pad_1" : bge.events.PAD1,
                        "pad_2" : bge.events.PAD2,
                        "pad_3" : bge.events.PAD3,
                        "pad_4" : bge.events.PAD4,
                        "pad_5" : bge.events.PAD5,
                        "pad_6" : bge.events.PAD6,
                        "pad_7" : bge.events.PAD7,
                        "pad_8" : bge.events.PAD8,
                        "pad_9" : bge.events.PAD9,
                        "pad_period" : bge.events.PADPERIOD,
                        "pad_slash"  : bge.events.PADSLASHKEY,
                        "pad_ster"   : bge.events.PADASTERKEY,
                        "pad_minus"  : bge.events.PADMINUS,
                        "pad_enter"  : bge.events.PADENTER,
                        "pad_plus"   : bge.events.PADPLUSKEY,

                        # Function Keys
                        "f1" : bge.events.F1KEY,
                        "f2" : bge.events.F2KEY,
                        "f3" : bge.events.F3KEY,
                        "f4" : bge.events.F4KEY,
                        "f5" : bge.events.F5KEY,
                        "f6" : bge.events.F6KEY,
                        "f7" : bge.events.F7KEY,
                        "f8" : bge.events.F8KEY,
                        "f9" : bge.events.F9KEY,
                        "f10" : bge.events.F10KEY,
                        "f11" : bge.events.F11KEY,
                        "f12" : bge.events.F12KEY,
                        "f13" : bge.events.F13KEY,
                        "f14" : bge.events.F14KEY,
                        "f15" : bge.events.F15KEY,
                        "f16" : bge.events.F16KEY,
                        "f17" : bge.events.F17KEY,
                        "f18" : bge.events.F18KEY,
                        "f19" : bge.events.F19KEY
                   }

         
        return dictkeys 
        pass



    #---------------------------------------------------------------
    def getKeys( self ):

        keysboards_out = { "True"  : [
                                        self.tc[ self.dict_keys[ self.get_keys_cont_comp[0]  ] ],
                                        self.tc[ self.dict_keys[ self.get_keys_cont_comp[1]  ] ],
                                        self.tc[ self.dict_keys[ self.get_keys_cont_comp[2]  ] ],
                                        self.tc[ self.dict_keys[ self.get_keys_cont_comp[3]  ] ],
                                        self.tc[ self.dict_keys[ self.get_keys_cont_comp[4]  ] ] ,
                                        self.tc[ self.dict_keys[ self.get_keys_cont_comp[5]  ] ]

                                        ] ,

                            "False"  : [
                                        self.tc[ self.dict_keys[ self.keyboardMoveFront ] ],
                                        self.tc[ self.dict_keys[ self.keyboardMoveBack  ] ],
                                        self.tc[ self.dict_keys[ self.keyboardMoveLeft  ] ],
                                        self.tc[ self.dict_keys[ self.keyboardMoveRight ] ],
                                        self.tc[ self.dict_keys[ self.keyboardRun ] ] ,
                                        self.tc[ self.dict_keys[ self.keyboardJump ] ]
                                        ]
                          
                          }

        return keysboards_out


    #-----------------------------------------------------

    def setValuesActions(self , keys_b ):
        valeus_t_f  = str( self.GetKeysContr ) 
        keys_or     = keys_b[ valeus_t_f ][0] or keys_b[ valeus_t_f ][1] or keys_b[ valeus_t_f ][2] or keys_b[ valeus_t_f ][3]

        
        if self.GetKeysContr == True:
            if self.object["GetConstraints"].onGround:

                #print( "Sim em chão")

                if keys_or:
                    if keys_b[ valeus_t_f ][4]:

                        self.object["ACTION_NAME_PROP"]         = self.List_actions_names[2]
                        self.object["ACTION_FRAME_START_PROP"]  = self.List_actions_frames[2][0]
                        self.object["ACTION_FRAME_END_PROP"]    = self.List_actions_frames[2][1]


                    else:
                        self.object["ACTION_NAME_PROP"]         = self.List_actions_names[1]
                        self.object["ACTION_FRAME_START_PROP"]  = self.List_actions_frames[1][0]
                        self.object["ACTION_FRAME_END_PROP"]    = self.List_actions_frames[1][1]





                else:
                    self.object["ACTION_NAME_PROP"]         = self.List_actions_names[0]
                    self.object["ACTION_FRAME_START_PROP"]  = self.List_actions_frames[0][0]
                    self.object["ACTION_FRAME_END_PROP"]    = self.List_actions_frames[0][1]



            else:
                #if keys_b[ valeus_t_f ][5] in [ 1,1 ]:
                self.object["ACTION_NAME_PROP"]         = self.List_actions_names[3]
                self.object["ACTION_FRAME_START_PROP"]  = self.List_actions_frames[3][0]
                self.object["ACTION_FRAME_END_PROP"]    = self.List_actions_frames[3][1]


            

        


            pass




    #---------------------------------------------------------------
    def setAnimations(self):

        self.object.playAction( self.object["ACTION_NAME_PROP"] , 
                                self.object["ACTION_FRAME_START_PROP"],
                                self.object["ACTION_FRAME_END_PROP"] ,

                                priority = 2 ,
                                blendin  = 6 ,
                                layer    = 1 

                                )



        #print( self.object["ACTION_NAME_PROP"] , self.object["ACTION_FRAME_START_PROP"], self.object["ACTION_FRAME_END_PROP"]  )
        pass



    #---------------------------------------------------------------
    def start(self, args):
        self.scene              = bge.logic.getCurrentScene()
        self.tc                 = bge.logic.keyboard.events
        self.GDict              = bge.logic.globalDict
        
        #---------------------------------------------------
        self.Action_Idle        = args["Action_Idle"]
        self.Action_Walk        = args["Action_Walk"]
        self.Action_Run         = args["Action_Run"]
        self.Action_Jump        = args["Action_Jump"]

        #---------------------------------------------------
        self.Idle_frame_start   = args["Idle_frame_start"]
        self.Idle_frame_end     = args["Idle_frame_end"]

        self.Walk_frame_start   = args["Walk_frame_start"]
        self.Walk_frame_end     = args["Walk_frame_end"]

        self.Run_frame_start    = args["Run_frame_start"]
        self.Run_frame_end      = args["Run_frame_end"]

        self.Jump_frame_start   = args["Jump_frame_start"]
        self.Jump_frame_end     = args["Jump_frame_end"]


        #---------------------------------------------------
        self.activateJump       = args["activateJump"]
        self.activateJRun       = args["activateJRun"]
        self.ActionsBlendin     = args["ActionsBlendin"] 

        #---------------------------------------------------

        self.SetIdComponent     = args["SetIdComponent"]
        self.GetKeysContr       = args["GetKeyboardsController"]
        self.GetKeyboardsID     = args["GetKeyboardsID"]


        #---------------------------------------------------
        self.keyboardMoveFront  = args["keyboardMoveFront"]
        self.keyboardMoveBack   = args["keyboardMoveBack" ]
        self.keyboardMoveLeft   = args["keyboardMoveLeft" ]
        self.keyboardMoveRight  = args["keyboardMoveRight"]

        self.keyboardJump       = args["keyboardJump"]
        self.keyboardRun        = args["keyboardRun"]





        #---------------------------------------------------
        self.List_actions_names  = [ self.Action_Idle ,self.Action_Walk , self.Action_Run , self.Action_Jump  ]

        self.List_actions_frames = [ [ self.Idle_frame_start  , self.Idle_frame_end ] , 
                                     [ self.Walk_frame_start  , self.Walk_frame_end ] , 
                                     [ self.Run_frame_start   , self.Run_frame_end  ] ,
                                     [ self.Jump_frame_start  , self.Jump_frame_end ] ,


                                    ]


        self.dict_keys          =  self.keyboardDict()
        self.get_keys_cont_comp = self.GDict[  self.GetKeyboardsID  ]

        self.actionsNames           = self.object["ACTION_NAME_PROP"]        = ""
        self.actionsFramesStart     = self.object["ACTION_FRAME_START_PROP"] = 0
        self.actionsFrameEnds       = self.object["ACTION_FRAME_END_PROP"]   = 0
        self.getConstraintsParent   = self.object["GET_CONSTRAINTS"]         = self.object


        self.trava_action_run       = self.GDict[ "ACTIONS_ACTIVATE" + self.GetKeyboardsID  ] = True  



        if self.GetKeysContr == True:
            self.parent_constraints = self.object["GetConstraints"] = self.GDict["CONSTRAINTS_" + str(self.GetKeyboardsID) ]


        #self.armture_player = [armtur for armtur in self.object.children if self.GetArmature_prop in armtur ][0]


       
        

    
    def update(self):
        tc       = bge.logic.keyboard.events
        m        = bge.logic.mouse.events
        #-----------------------------------


        #-----------------------------------
        self.keysboards         = self.getKeys()


        self.setValuesActions( keys_b = self.keysboards )

        #if 
        self.setAnimations()


        pass



class WalkAnimation(bge.types.KX_PythonComponent):

    args = OrderedDict((

                        ( "_#SetActValue#_" , "_#SetActValue#_"),

                        ( "Act_Idle"         , ""   ),
                        ( "Act_Walk"         , ""   ),
                        
                        

                        ( "Idle_f_start"   , 0   ),
                        ( "Idle_f_end"     , 0   ),

                        ( "Walk_f_start"   , 0   ),
                        ( "Walk_f_end"     , 0   ),

                       
                        ( "_#SetsValue#_" , "_#SetsValue#_"),

                        ( "ActBlendin"        , 0   ),


                        ( "_#Get_Value#_" , "_#Get_Value#_"),

                        ("SetIdComp"           , "ID_KEYS_ACTIS"),

                        ("GetKeyboardsCont"   , True ),
                        ("GetKeysID"           , "ID_KEYS" ),
                        

                        ( "_#keyboards_Action#_" , "_#keyboard_Action#_"),

                        ( "keyMoveFront"     , "w"  ) ,

                        ))



    def start(self, args):
        self.scene              = bge.logic.getCurrentScene()
        self.tc                 = bge.logic.keyboard.events
        self.GDict              = bge.logic.globalDict
        
        #---------------------------------------------------

        pass


    def update(self):

        tc       = bge.logic.keyboard.events
        m        = bge.logic.mouse.events
        #-----------------------------------


        #-----------------------------------

        pass
