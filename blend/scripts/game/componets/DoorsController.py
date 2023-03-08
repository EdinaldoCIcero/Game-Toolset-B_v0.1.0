import bge
from collections import OrderedDict





class Door(bge.types.KX_PythonComponent):
 
    args = OrderedDict((

                        ("@Set_Values",""),
                        
                        ("Player_obj_name"       , "" ) ,
                        ("Action_door_name"      , "" ) ,
                        ("Action_frame_start"    , 0  ),
                        ("Action_frame_end"      , 0  ),

                        ("Set_distance"          , 1.500  ),
                        ("Key_event_open"        , "e" ),

                        ("Open_door_iten"        , False ),
                        ("Item_collected_name"   , ""    ),
                        ("Delet_Item_in_player"  , True  ),

                        ))



    #---------------------------------------------------------------
    def eventsKeys(self):
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


    #-----------------------------------------------
    def start(self , args):

        self.Player_obj_name    = args["Player_obj_name"]
        self.Action_door_name   = args["Action_door_name"]
        self.Action_frame_start = args['Action_frame_start']
        self.Action_frame_end   = args['Action_frame_end']
        self.Set_distance       = args['Set_distance']
        self.Key_event_open     = args['Key_event_open']

        self.Open_door_iten         = args['Open_door_iten']
        self.Item_collected_name    = args['Item_collected_name']
        self.Delet_Item_in_player   = args['Delet_Item_in_player']

       



        #---------------------------------------------
        self.GDICT       = bge.logic.globalDict

        self.door_states_names  = [ "OPEN" ,"CLOSE" ]  
        self.door_state         = self.object["DOOR_STATE"] = "CLOSE"

        self.door_iten_colect   = self.object["DOOR_ITEM_COLECT"] = 0

        

         #------------------------------------
        self.global_bag_player = bge.logic.globalDict
        self.global_bag_player["SMALL_BAG_PLAYER"] = []






    
    def doorLogic(self , player_object , set_distance_to , event_key_name , action_dor_name , action_frame_start , action_frame_end ):
        keys_events = self.eventsKeys()    


        if self.object.getDistanceTo( player_object ) <= set_distance_to:

            if keys_events[ event_key_name ] in [1,1] and self.object["DOOR_STATE"] == self.door_states_names[1]:

                if self.Open_door_iten == True:
                    if self.Item_collected_name in self.global_bag_player["SMALL_BAG_PLAYER"]:
                        self.object["DOOR_ITEM_COLECT"] = 1
                        

                    if self.Open_door_iten == True and self.object["DOOR_ITEM_COLECT"] == 1:
                        self.object.playAction( action_dor_name  , action_frame_start , action_frame_end )
                        self.object["DOOR_STATE"] = self.door_states_names[0]

                        if self.Delet_Item_in_player == True and self.Item_collected_name in self.global_bag_player["SMALL_BAG_PLAYER"]:
                            self.global_bag_player["SMALL_BAG_PLAYER"].remove( self.Item_collected_name )



                else:
                    self.object.playAction( action_dor_name  , action_frame_start , action_frame_end )
                    self.object["DOOR_STATE"] = self.door_states_names[0]
                

            #-----------------------
            elif keys_events[ event_key_name ] in [1,1] and self.object["DOOR_STATE"] == self.door_states_names[0] :

                if self.Open_door_iten == True:
                    if self.Item_collected_name in self.global_bag_player["SMALL_BAG_PLAYER"]:
                        self.object["DOOR_ITEM_COLECT"] = 1
                        

                    if self.Open_door_iten == True and self.object["DOOR_ITEM_COLECT"] == 1:
                        self.object.playAction( action_dor_name  , action_frame_end , action_frame_start  )
                        self.object["DOOR_STATE"] = self.door_states_names[1]
                        

                        if self.Delet_Item_in_player == True and self.Item_collected_name in self.global_bag_player["SMALL_BAG_PLAYER"]:
                            self.global_bag_player["SMALL_BAG_PLAYER"].remove( self.Item_collected_name )

                        pass


                else:
                    self.object.playAction( action_dor_name  , action_frame_end , action_frame_start   )
                    self.object["DOOR_STATE"] = self.door_states_names[1]




        pass


    def update(self):
        keyboard    = bge.logic.keyboard.events
        #-----------------------------------------------
       

        self.doorLogic( 
                    player_object       = self.object.scene.objects[ self.Player_obj_name ], 
                    set_distance_to     = self.Set_distance ,  
                    event_key_name      = self.Key_event_open ,  
                    action_dor_name     = self.Action_door_name , 
                    action_frame_start  = self.Action_frame_start , 
                    action_frame_end    = self.Action_frame_end )

        




        pass


