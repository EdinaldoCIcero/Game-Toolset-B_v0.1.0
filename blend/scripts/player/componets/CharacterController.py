import bge
from collections import OrderedDict
from mathutils import Vector
#from random import randint



class Controller(bge.types.KX_PythonComponent):


    args = OrderedDict((
                        ( "@ConfigsValues#_" , ""),

                        ( "CameraObjRotation_X"   , "None"      ),
                        ( "SpeedMovement"         , 0.100   ),
                        ( "SpeedRun"              , 0.160   ),
                        ( "activateJump"          , True  ),
                        ( "activateJRun"          , True  ),
                        ( "Armature"              , True  ),
                        ( "GetArmature_prop"      , ""   ),


                        ( "@Camera_Colision" , ""),

                        ( "Activate_camera_colision"    , True ),
                        ( "Camera_obj_name"             , ""   ),
                        ( "Point_obj_fucos"             , ""   ),
                        ( "Point_obj_root"              , ""   ),
                        ( "Propriet_name_colision"      , ""   ),
                        


                        ( "@keyboards_Movements#_" , ""),

                        ( "keyboardMoveFront"     , "w"  ),
                        ( "keyboardMoveBack"      , "s"  ),
                        ( "keyboardMoveLeft"      , "d"  ),
                        ( "keyboardMoveRight"     , "a"  ),
                        ( "keyboardJump"          , "space" ),
                        ( "keyboardRun"           , "left_shift" ),

                        ( "@Outinputs_Values#_" , ""),
                        ( "ID_KeyboardsController" , "ID_KEYS" ),

                        ))



    #---------------------------------------------------------------
    def keyboardDict(self):
        keyboard = bge.logic.keyboard.events
        mouse    = bge.logic.mouse.events
        #---------------------------------------------


        dictkeys = {    # Alphabet keys 
                        "a" :  keyboard[bge.events.AKEY],
                        "b" :  keyboard[bge.events.BKEY],
                        "c" :  keyboard[bge.events.CKEY],
                        "d" :  keyboard[bge.events.DKEY],
                        "e" :  keyboard[bge.events.EKEY],
                        "f" :  keyboard[bge.events.FKEY],
                        "g" :  keyboard[bge.events.GKEY],
                        "h" :  keyboard[bge.events.HKEY],
                        "i" :  keyboard[bge.events.IKEY],
                        "j" :  keyboard[bge.events.JKEY],
                        
                        "k" :  keyboard[bge.events.KKEY],
                        "l" :  keyboard[bge.events.LKEY],
                        "m" :  keyboard[bge.events.MKEY],
                        "n" :  keyboard[bge.events.NKEY],
                        "o" :  keyboard[bge.events.OKEY],
                        "p" :  keyboard[bge.events.PKEY],
                        "q" :  keyboard[bge.events.QKEY],
                        "r" :  keyboard[bge.events.RKEY],
                        "s" :  keyboard[bge.events.SKEY],
                        "t" :  keyboard[bge.events.TKEY],
                        "u" :  keyboard[bge.events.UKEY],
                        "v" :  keyboard[bge.events.VKEY],
                        "w" :  keyboard[bge.events.WKEY],
                        "x" :  keyboard[bge.events.XKEY],
                        "y" :  keyboard[bge.events.YKEY],
                        "z" :  keyboard[bge.events.ZKEY],

                        # Other Keys 
                        
                        "acent_grave"   : keyboard[bge.events.ACCENTGRAVEKEY],
                        "back_slash"    : keyboard[bge.events.BACKSLASHKEY ],
                        "back_space"    : keyboard[bge.events.BACKSPACEKEY],
                        "comma"         : keyboard[bge.events.COMMAKEY],
                        "del"           : keyboard[bge.events.DELKEY],
                        "end"           : keyboard[bge.events.ENDKEY],
                        "equal"         : keyboard[bge.events.EQUALKEY],
                        "esc"           : keyboard[bge.events.ESCKEY],
                        "home"          : keyboard[bge.events.HOMEKEY],
                        "insert"        : keyboard[bge.events.INSERTKEY],
                        "left_bracket"  : keyboard[bge.events.LEFTBRACKETKEY],
                        "linefeed"      : keyboard[bge.events.LINEFEEDKEY],
                        "minus"         : keyboard[bge.events.MINUSKEY],
                        "page_down"     : keyboard[bge.events.PAGEDOWNKEY],
                        "page_up"       : keyboard[bge.events.PAGEUPKEY],
                        "pause"         : keyboard[bge.events.PAUSEKEY],
                        "period"        : keyboard[bge.events.PERIODKEY],
                        "quote"         : keyboard[bge.events.QUOTEKEY],
                        "right_bracket" : keyboard[bge.events.RIGHTBRACKETKEY],
                        "enter"         : keyboard[bge.events.ENTERKEY],
                        "semicolon"     : keyboard[bge.events.SEMICOLONKEY],
                        "slash"         : keyboard[bge.events.SLASHKEY],
                        "space"         : keyboard[bge.events.SPACEKEY],
                        "tab"           : keyboard[bge.events.TABKEY],

                        # Modifiers Keys 
                        "caps_lock"     : keyboard[bge.events.CAPSLOCKKEY],
                        "left_ctrl"     : keyboard[bge.events.LEFTCTRLKEY],
                        "left_alt"      : keyboard[bge.events.LEFTALTKEY],
                        "right_alt"     : keyboard[bge.events.RIGHTALTKEY],
                        "right_ctrl"    : keyboard[bge.events.RIGHTCTRLKEY],
                        "right_shift"   : keyboard[bge.events.RIGHTSHIFTKEY],
                        "left_shift"    : keyboard[bge.events.LEFTSHIFTKEY],


                        # Arrow Keys 

                        "left_arrow"    : keyboard[bge.events.LEFTARROWKEY],
                        "down_arrow"    : keyboard[bge.events.DOWNARROWKEY],
                        "right_arrow"   : keyboard[bge.events.RIGHTARROWKEY],
                        "up_arrow"      : keyboard[bge.events.UPARROWKEY],

                        # Number keys

                        "0"     : keyboard[bge.events.ZEROKEY],
                        "1"     : keyboard[bge.events.ONEKEY],
                        "2"     : keyboard[bge.events.TWOKEY],
                        "3"     : keyboard[bge.events.THREEKEY],
                        "4"     : keyboard[bge.events.FOURKEY],
                        "5"     : keyboard[bge.events.FIVEKEY],
                        "6"     : keyboard[bge.events.SIXKEY],
                        "7"     : keyboard[bge.events.SEVENKEY],
                        "8"     : keyboard[bge.events.EIGHTKEY],
                        "9"     : keyboard[bge.events.NINEKEY],

                        # Numberpad Keys

                        "pad_0" : keyboard[bge.events.PAD0],
                        "pad_1" : keyboard[bge.events.PAD1],
                        "pad_2" : keyboard[bge.events.PAD2],
                        "pad_3" : keyboard[bge.events.PAD3],
                        "pad_4" : keyboard[bge.events.PAD4],
                        "pad_5" : keyboard[bge.events.PAD5],
                        "pad_6" : keyboard[bge.events.PAD6],
                        "pad_7" : keyboard[bge.events.PAD7],
                        "pad_8" : keyboard[bge.events.PAD8],
                        "pad_9" : keyboard[bge.events.PAD9],
                        "pad_period" : keyboard[bge.events.PADPERIOD],
                        "pad_slash"  : keyboard[bge.events.PADSLASHKEY],
                        "pad_ster"   : keyboard[bge.events.PADASTERKEY],
                        "pad_minus"  : keyboard[bge.events.PADMINUS],
                        "pad_enter"  : keyboard[bge.events.PADENTER],
                        "pad_plus"   : keyboard[bge.events.PADPLUSKEY],

                        # Function Keys
                        "f1" : keyboard[bge.events.F1KEY],
                        "f2" : keyboard[ bge.events.F2KEY],
                        "f3" : keyboard[bge.events.F3KEY],
                        "f4" : keyboard[bge.events.F4KEY],
                        "f5" : keyboard[bge.events.F5KEY],
                        "f6" : keyboard[bge.events.F6KEY],
                        "f7" : keyboard[bge.events.F7KEY],
                        "f8" : keyboard[bge.events.F8KEY],
                        "f9" : keyboard[bge.events.F9KEY],
                        "f10" : keyboard[bge.events.F10KEY],
                        "f11" : keyboard[bge.events.F11KEY],
                        "f12" : keyboard[bge.events.F12KEY],
                        "f13" : keyboard[bge.events.F13KEY],
                        "f14" : keyboard[bge.events.F14KEY],
                        "f15" : keyboard[bge.events.F15KEY],
                        "f16" : keyboard[bge.events.F16KEY],
                        "f17" : keyboard[bge.events.F17KEY],
                        "f18" : keyboard[bge.events.F18KEY],
                        "f19" : keyboard[bge.events.F19KEY],

                        "left_mouse"        : mouse[bge.events.LEFTMOUSE],
                        "middle_mouse"      : mouse[bge.events.MIDDLEMOUSE],
                        "right_mouse"       : mouse[bge.events.RIGHTMOUSE],
                        "wheelup_mouse"     : mouse[bge.events.WHEELUPMOUSE],
                        "weeldown_mouse"    : mouse[bge.events.WHEELDOWNMOUSE],
                        "mouse_x"           : mouse[bge.events.MOUSEX],
                        "mouse_y"           : mouse[bge.events.MOUSEY],

                   }

         
        return dictkeys


    #---------------------------------------------------------------
    def charMove( self , list_keys ,  speed ,  cam_orientation  ):

        #-----------------------------#
        x,y,z = 0,0,0

        y =  list_keys[0] - list_keys[1]
        x =  list_keys[2] - list_keys[3]

        
        vec = Vector([x,y,z]).normalized() * speed

        
        if self .CameraObjRotation != "None":
            self.constraints.walkDirection =  cam_orientation.worldOrientation * vec # self.worldOrientation * vec
        
        else:
            self.constraints.walkDirection =  self.object.worldOrientation * vec
            


    #---------------------------------------------------------------
    def charJump(self , key_space ):
        
        #-----------------------------#
        if self.activateJump == True:
            if key_space in [1,1] :
                self.constraints.jump()



    #----------------------------------------
    def charRun(self , list_keys ):

        keys_moves = list_keys[0] or list_keys[1] or list_keys[2] or list_keys[3]

        if self.activateJRun == True:
            if list_keys[ 4 ] and keys_moves :
                self.char_speed =  self.SpeedRun

            else:
                self.char_speed = self.char_speed_defaut



    #---------------------------------------------------------------
    def charDirection(self , armature_children , constraints ):
        direction = constraints.walkDirection
        #-----------------------------#

        if self.Armature == True:
            if direction.length != 0:
                armature_children.alignAxisToVect(direction, 1,0.5)
                armature_children.alignAxisToVect([0,0,1], 2, 1)


    #---------------------------------------------------------------

    def setGruopKeyboards( self ):
        self.GDict  = bge.logic.globalDict


        self.GDict[  self.ID_KeyboardsController  ] = [   
                                                        self.keyboardMoveFront ,
                                                        self.keyboardMoveBack ,
                                                        self.keyboardMoveLeft ,
                                                        self.keyboardMoveRight,

                                                        self.keyboardRun ,
                                                        self.keyboardJump 

                                                       ]


        pass


    #---------------------------------------------------------------
    def cameraColision( self , obj_focus , obj_root , obj_cam , prop_name_colision):
        ray = self.object.rayCast( obj_root , obj_focus , obj_focus.getDistanceTo(obj_root) , prop_name_colision  )
        #------------------------------

        if ray[0] != None:
            obj_cam.worldPosition = ray[1]

        if ray[0] == None:
            obj_cam.worldPosition = obj_root.worldPosition


    #---------------------------------------------------------------
    def start(self, args):
        self.scene              = bge.logic.getCurrentScene()
        self.tc                 = bge.logic.keyboard.events
        self.GDict              = bge.logic.globalDict
        

        self.CameraObjRotation  = args["CameraObjRotation_X"]
        self.speedMovement      = args["SpeedMovement"]
        self.SpeedRun           = args["SpeedRun"]

        self.activateJump       = args["activateJump"]
        self.activateJRun       = args["activateJRun"]

        self.Armature           = args["Armature"]
        self.GetArmature_prop   = args["GetArmature_prop"]



        self.Activate_camera_colision   = args["Activate_camera_colision"]
        self.Camera_obj_name            = args["Camera_obj_name"]

        self.Point_obj_fucos            = args["Point_obj_fucos"]
        self.Point_obj_root             = args["Point_obj_root"]
        self.Propriet_name_colision     = args["Propriet_name_colision"]



        self.keyboardMoveFront  = args["keyboardMoveFront"]
        self.keyboardMoveBack   = args["keyboardMoveBack" ]
        self.keyboardMoveLeft   = args["keyboardMoveLeft" ]
        self.keyboardMoveRight  = args["keyboardMoveRight"]

        self.keyboardJump       = args["keyboardJump"]
        self.keyboardRun        = args["keyboardRun"]


        self.ID_KeyboardsController = args["ID_KeyboardsController"]


        #---------------------------------------------------
        self.char_speed_defaut  = self.speedMovement
        self.char_speed         = self.speedMovement
        self.armture_player     = None
        self.cam_rot_obj        = None
        
        if self.Armature == True:
            self.armture_player = [armtur for armtur in self.object.children if self.GetArmature_prop in armtur ][0]


        if self.CameraObjRotation != "None":
            self.cam_rot_obj = self.scene.objects[ self.CameraObjRotation ]


        self.constraints    = bge.constraints.getCharacter( self.object )
        
        

        self.setGruopKeyboards()
        
        self.ditc_constraints_gd = self.GDict["CONSTRAINTS_" + str( self.ID_KeyboardsController ) ] = self.constraints 

        self.player_small_bag    = self.GDict["SMALL_BAG_PLAYER"] = []





    def update(self):
        self.scene      = bge.logic.getCurrentScene()
        tc              = bge.logic.keyboard.events
        m               = bge.logic.mouse.events
        GDict           = bge.logic.globalDict
        self.dict_keys  = self.keyboardDict()
        #-----------------------------------
        
        #-----------------------------------
       

        if self.Activate_camera_colision == True:
            self.cameraColision(    obj_focus           = self.object.scene.objects[ self.Point_obj_fucos ] , 
                                    obj_root            = self.object.scene.objects[ self.Point_obj_root ] , 
                                    obj_cam             = self.object.scene.objects[ self.Camera_obj_name ] , 
                                    prop_name_colision  = self.Propriet_name_colision  )

        

        if self.Armature == True:
            self.charDirection( armature_children  = self.armture_player  , constraints =  self.constraints  )


        #if self.activateJump == True:
        self.charJump( key_space = self.dict_keys[ self.keyboardJump ] )


        #if self.activateJRun == True:
        self.charRun( list_keys = [   
                                    self.dict_keys[ self.keyboardMoveFront ] ,
                                    self.dict_keys[ self.keyboardMoveBack  ] ,
                                    self.dict_keys[ self.keyboardMoveLeft  ] ,
                                    self.dict_keys[ self.keyboardMoveRight ] ,
                                    self.dict_keys[ self.keyboardRun ] 

                                ])

        self.charMove(  list_keys = [   
                                        self.dict_keys[ self.keyboardMoveFront ] ,
                                        self.dict_keys[ self.keyboardMoveBack  ] ,
                                        self.dict_keys[ self.keyboardMoveLeft  ] ,
                                        self.dict_keys[ self.keyboardMoveRight ] 
                                    ]
                                    , 

                                    speed            = self.char_speed ,  
                                    cam_orientation  = self.cam_rot_obj  )






    #---------------------------------------------------------------
class Animator(bge.types.KX_PythonComponent):

    args = OrderedDict((

                        ( "@SetActionsValues#_" , ""),

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

                        ( "@SetsValues#_" , ""),

                        ( "activateJump"          , True  ),
                        ( "activateJRun"          , True  ),

                        ( "ActionsBlendin"        , 0   ),


                        ( "@Get_Values#_" , ""),
                        ("SetIdComponent"           , "ID_KEYS_ACTIONS"),
                        ("GetKeyboardsController"   , True ),
                        ("GetKeyboardsID"           , "ID_KEYS" ),
                        
                        ( "@keyboards_Actions#_" , ""),
                        ( "keyboardMoveFront"     , "w"  ) ,
                        ( "keyboardMoveBack"      , "s"  ) ,
                        ( "keyboardMoveLeft"      , "d"  ) ,
                        ( "keyboardMoveRight"     , "a"  ) ,

                        ( "keyboardJump"          , "space" ),
                        ( "keyboardRun"           , "left_shift" ),



                        ))





    #---------------------------------------------------------------
    def keyboardDict(self):
        keyboard = bge.logic.keyboard.events
        mouse    = bge.logic.mouse.events
        #---------------------------------------------


        dictkeys = {    # Alphabet keys 
                        "a" :  keyboard[bge.events.AKEY],
                        "b" :  keyboard[bge.events.BKEY],
                        "c" :  keyboard[bge.events.CKEY],
                        "d" :  keyboard[bge.events.DKEY],
                        "e" :  keyboard[bge.events.EKEY],
                        "f" :  keyboard[bge.events.FKEY],
                        "g" :  keyboard[bge.events.GKEY],
                        "h" :  keyboard[bge.events.HKEY],
                        "i" :  keyboard[bge.events.IKEY],
                        "j" :  keyboard[bge.events.JKEY],
                        
                        "k" :  keyboard[bge.events.KKEY],
                        "l" :  keyboard[bge.events.LKEY],
                        "m" :  keyboard[bge.events.MKEY],
                        "n" :  keyboard[bge.events.NKEY],
                        "o" :  keyboard[bge.events.OKEY],
                        "p" :  keyboard[bge.events.PKEY],
                        "q" :  keyboard[bge.events.QKEY],
                        "r" :  keyboard[bge.events.RKEY],
                        "s" :  keyboard[bge.events.SKEY],
                        "t" :  keyboard[bge.events.TKEY],
                        "u" :  keyboard[bge.events.UKEY],
                        "v" :  keyboard[bge.events.VKEY],
                        "w" :  keyboard[bge.events.WKEY],
                        "x" :  keyboard[bge.events.XKEY],
                        "y" :  keyboard[bge.events.YKEY],
                        "z" :  keyboard[bge.events.ZKEY],

                        # Other Keys 
                        
                        "acent_grave"   : keyboard[bge.events.ACCENTGRAVEKEY],
                        "back_slash"    : keyboard[bge.events.BACKSLASHKEY ],
                        "back_space"    : keyboard[bge.events.BACKSPACEKEY],
                        "comma"         : keyboard[bge.events.COMMAKEY],
                        "del"           : keyboard[bge.events.DELKEY],
                        "end"           : keyboard[bge.events.ENDKEY],
                        "equal"         : keyboard[bge.events.EQUALKEY],
                        "esc"           : keyboard[bge.events.ESCKEY],
                        "home"          : keyboard[bge.events.HOMEKEY],
                        "insert"        : keyboard[bge.events.INSERTKEY],
                        "left_bracket"  : keyboard[bge.events.LEFTBRACKETKEY],
                        "linefeed"      : keyboard[bge.events.LINEFEEDKEY],
                        "minus"         : keyboard[bge.events.MINUSKEY],
                        "page_down"     : keyboard[bge.events.PAGEDOWNKEY],
                        "page_up"       : keyboard[bge.events.PAGEUPKEY],
                        "pause"         : keyboard[bge.events.PAUSEKEY],
                        "period"        : keyboard[bge.events.PERIODKEY],
                        "quote"         : keyboard[bge.events.QUOTEKEY],
                        "right_bracket" : keyboard[bge.events.RIGHTBRACKETKEY],
                        "enter"         : keyboard[bge.events.ENTERKEY],
                        "semicolon"     : keyboard[bge.events.SEMICOLONKEY],
                        "slash"         : keyboard[bge.events.SLASHKEY],
                        "space"         : keyboard[bge.events.SPACEKEY],
                        "tab"           : keyboard[bge.events.TABKEY],

                        # Modifiers Keys 
                        "caps_lock"     : keyboard[bge.events.CAPSLOCKKEY],
                        "left_ctrl"     : keyboard[bge.events.LEFTCTRLKEY],
                        "left_alt"      : keyboard[bge.events.LEFTALTKEY],
                        "right_alt"     : keyboard[bge.events.RIGHTALTKEY],
                        "right_ctrl"    : keyboard[bge.events.RIGHTCTRLKEY],
                        "right_shift"   : keyboard[bge.events.RIGHTSHIFTKEY],
                        "left_shift"    : keyboard[bge.events.LEFTSHIFTKEY],


                        # Arrow Keys 

                        "left_arrow"    : keyboard[bge.events.LEFTARROWKEY],
                        "down_arrow"    : keyboard[bge.events.DOWNARROWKEY],
                        "right_arrow"   : keyboard[bge.events.RIGHTARROWKEY],
                        "up_arrow"      : keyboard[bge.events.UPARROWKEY],

                        # Number keys

                        "0"     : keyboard[bge.events.ZEROKEY],
                        "1"     : keyboard[bge.events.ONEKEY],
                        "2"     : keyboard[bge.events.TWOKEY],
                        "3"     : keyboard[bge.events.THREEKEY],
                        "4"     : keyboard[bge.events.FOURKEY],
                        "5"     : keyboard[bge.events.FIVEKEY],
                        "6"     : keyboard[bge.events.SIXKEY],
                        "7"     : keyboard[bge.events.SEVENKEY],
                        "8"     : keyboard[bge.events.EIGHTKEY],
                        "9"     : keyboard[bge.events.NINEKEY],

                        # Numberpad Keys

                        "pad_0" : keyboard[bge.events.PAD0],
                        "pad_1" : keyboard[bge.events.PAD1],
                        "pad_2" : keyboard[bge.events.PAD2],
                        "pad_3" : keyboard[bge.events.PAD3],
                        "pad_4" : keyboard[bge.events.PAD4],
                        "pad_5" : keyboard[bge.events.PAD5],
                        "pad_6" : keyboard[bge.events.PAD6],
                        "pad_7" : keyboard[bge.events.PAD7],
                        "pad_8" : keyboard[bge.events.PAD8],
                        "pad_9" : keyboard[bge.events.PAD9],
                        "pad_period" : keyboard[bge.events.PADPERIOD],
                        "pad_slash"  : keyboard[bge.events.PADSLASHKEY],
                        "pad_ster"   : keyboard[bge.events.PADASTERKEY],
                        "pad_minus"  : keyboard[bge.events.PADMINUS],
                        "pad_enter"  : keyboard[bge.events.PADENTER],
                        "pad_plus"   : keyboard[bge.events.PADPLUSKEY],

                        # Function Keys
                        "f1" : keyboard[bge.events.F1KEY],
                        "f2" : keyboard[ bge.events.F2KEY],
                        "f3" : keyboard[bge.events.F3KEY],
                        "f4" : keyboard[bge.events.F4KEY],
                        "f5" : keyboard[bge.events.F5KEY],
                        "f6" : keyboard[bge.events.F6KEY],
                        "f7" : keyboard[bge.events.F7KEY],
                        "f8" : keyboard[bge.events.F8KEY],
                        "f9" : keyboard[bge.events.F9KEY],
                        "f10" : keyboard[bge.events.F10KEY],
                        "f11" : keyboard[bge.events.F11KEY],
                        "f12" : keyboard[bge.events.F12KEY],
                        "f13" : keyboard[bge.events.F13KEY],
                        "f14" : keyboard[bge.events.F14KEY],
                        "f15" : keyboard[bge.events.F15KEY],
                        "f16" : keyboard[bge.events.F16KEY],
                        "f17" : keyboard[bge.events.F17KEY],
                        "f18" : keyboard[bge.events.F18KEY],
                        "f19" : keyboard[bge.events.F19KEY],

                        "left_mouse"        : mouse[bge.events.LEFTMOUSE],
                        "middle_mouse"      : mouse[bge.events.MIDDLEMOUSE],
                        "right_mouse"       : mouse[bge.events.RIGHTMOUSE],
                        "wheelup_mouse"     : mouse[bge.events.WHEELUPMOUSE],
                        "weeldown_mouse"    : mouse[bge.events.WHEELDOWNMOUSE],
                        "mouse_x"           : mouse[bge.events.MOUSEX],
                        "mouse_y"           : mouse[bge.events.MOUSEY],

                   }

         
        return dictkeys



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




    def update(self):
        tc       = bge.logic.keyboard.events
        m        = bge.logic.mouse.events
        #-----------------------------------
        self.keysboards         = self.getKeys()

        self.setValuesActions( keys_b = self.keysboards )
        self.setAnimations()




        pass
