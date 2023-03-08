from bge import logic,events , types
import bgui
import bgui.bge_utils
import bge
import aud


#-----------------------------------------------------
from scripts.menus.libs.JSON import JsonClass


#-----------------------------------------------------

scene   = logic.getCurrentScene()
tc      = logic.keyboard.events
gd      = bge.logic.globalDict
#-----------------------------------------------------

Jason_read      = JsonClass()

BUTTON_START_DATE     = Jason_read.json_read( name_file = "scripts/menus/database/button_start" )

BUTTONS_MAIN_DATA     = Jason_read.json_read( name_file = "scripts/menus/database/buttons_main" )


#-----------------------------------------------------

class MenuMainElements():
    def __init__( self ):
        #################################

        #--------------------------------
        
        #------- OBJETOS PROPS ---------#
        self.path    = bge.logic.expandPath("//scripts/menus/image/imgs_main/")
        self.opsion  = bgui.BGUI_DEFAULT | bgui.BGUI_DEFAULT


        pass

        
    def cardsLoadGame( self , frame_parent , text_index , position  ):
        frame_main          = bgui.Frame( frame_parent , border = 0 , size = ( 0.90 , 0.20 ), pos = position )
        frame_main.colors   = [( 0.0 , 0.0 , 0.0 , 0.40 ) for i in range(4)]
        

        frame_quad          = bgui.Frame( frame_main , border = 0 , size = ( 0.20 , 0.80 ), pos = ( 0.04 , 0.10 ) )
        frame_quad.colors   = [( 0.0 , 0.0 , 0.0 , 0.60 ) for i in range(4)]


        return {  "Text_descritions_buttons"  : bgui.Label( 
                                                parent     = frame_main ,   
                                                text       = "Loads Game", 
                                                pt_size    = 50 , 
                                                pos        = [ 0.70 , 0.40 ] ,
                                                sub_theme  = 'Large', 
                                                options    =  self.opsion ),

                "Text_index_test"  : bgui.Label( 
                                                parent     = frame_main ,   
                                                text       = str( text_index ), 
                                                pt_size    = 30 , 
                                                pos        = [ 0.02 , 0.5 ] ,
                                                sub_theme  = 'Large', 
                                                options    =  self.opsion ),

                                                }
        pass



    def buttonsImg( self , parent , sizes , positions , back_img , over_img , click_img = None ):

        button_image   = bgui.ImageButton(  parent , 
                                            #name            = "ButonImg", 
                                            default_image   = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                            default2_image  = ( self.path + back_img    , 1 , 1  , 1 , 1  ) ,
                                            hover_image     = ( self.path + over_img    , 1 , 1  , 1 , 1  ) ,
                                            #click_image     = ( self.path + click_img   , 1 , 1  , 1 , 1  ) ,
                                            size            = sizes , 
                                            pos             = positions ,
                                            options         = self.opsion )
        
        return button_image


    #----- Menu start simples --------------------
    def menuStart( self , frame_parent ):
        frame          = bgui.Frame( frame_parent , border = 0 , size = ( 1.00 , 1.00 ), pos = ( 0.0 , 0.0 )  )
        frame.colors   = [( 0.0 , 0.0 , 0.0 , 0.00 ) for i in range(4)]

        return {
            "FRAME"             : frame ,

            "Game_Logo"         : bgui.Image( frame , self.path + "title_img.png", 
                                                size    = ( 0.38 , 0.38 ) , 
                                                pos     = ( 0.32 , 0.50 ), 
                                                options = self.opsion
                                                ),


            "Text_01"           : bgui.Label(   parent     = frame ,
                                            text       = "MENU PRINCIPAL AQUI ", 
                                            pt_size    = 40 , 
                                            pos        = [ 0.05 , 0.92 ] ,
                                            sub_theme  = 'Large', 
                                            options    =  self.opsion ),


            "button_start_img"  : self.buttonsImg( parent       = frame  , 
                                                    sizes       = [ 0.12 , 0.05] , 
                                                    positions   = [ 0.45 , 0.20] , 
                                                    back_img    = BUTTON_START_DATE["button_start_img"][0], 
                                                    over_img    = BUTTON_START_DATE["button_start_img"][1]
                                                )
            }

        
        pass


    #---------------------------------------------------
    def menuMain( self , frame_parent ):
        frame_main          = bgui.Frame( frame_parent , border = 0 , size = ( 1.0 , 1.0 ), pos = ( 0.0 , 0.0 )  )
        frame_main.colors   = [( 0.0 , 0.0 , 0.0 , 0.20 ) for i in range(4)]

        frame_base_faixa         = bgui.Frame( frame_main , border = 0 , size = ( 1.0 , 0.08 ), pos = ( 0.0 , 0.0 )  )
        frame_base_faixa.colors  = [( 0.0 , 0.0 , 0.0 , 0.50 ) for i in range(4)]

        #------------------------------------------------------------------------

        return {
            
            "FRAME"             : frame_main ,

            "Text_descritions_buttons"  : bgui.Label( 
                                                parent     = frame_base_faixa ,
                                                text       = "T", 
                                                pt_size    = 20 , 
                                                pos        = [ 0.35 , 0.45 ] ,
                                                sub_theme  = 'Large', 
                                                options    =  self.opsion ),


            "Game_Logo"         : bgui.Image( frame_main , self.path + "title_img.png", 
                                                size    = ( 0.30 , 0.30 ) , 
                                                pos     = ( 0.04 , 0.65 ), 
                                                options = self.opsion
                                                ),



            "button_start"  : self.buttonsImg( parent       = frame_main  , 
                                                    sizes       = [ 0.12 , 0.05] , 
                                                    positions   = [ 0.45 , 0.30] , 
                                                    back_img    = BUTTONS_MAIN_DATA["button_start"][0], 
                                                    over_img    = BUTTONS_MAIN_DATA["button_start"][1],
                                                    ),


            "button_load_game"  : self.buttonsImg( parent      = frame_main  , 
                                                    sizes       = [ 0.12 , 0.05] , 
                                                    positions   = [ 0.45 , 0.24] , 
                                                    back_img    = BUTTONS_MAIN_DATA["button_load_game"][0], 
                                                    over_img    = BUTTONS_MAIN_DATA["button_load_game"][1],
                                                    ),


            "button_opisões"  : self.buttonsImg( parent       = frame_main  , 
                                                    sizes       = [ 0.12 , 0.05] , 
                                                    positions   = [ 0.45 , 0.18] , 
                                                    back_img    = BUTTONS_MAIN_DATA["button_opisões"][0] ,
                                                    over_img    = BUTTONS_MAIN_DATA["button_opisões"][1],
                                                    ),


            "button_sair"  : self.buttonsImg( parent       = frame_main  , 
                                                    sizes       = [ 0.12 , 0.05] , 
                                                    positions   = [ 0.45 , 0.12] , 
                                                    back_img    = BUTTONS_MAIN_DATA["button_sair"][0], 
                                                    over_img    = BUTTONS_MAIN_DATA["button_sair"][1],
                                                    ),                                                   

            }

        
        pass
    


    #---------------------------------------------------
    def menuLoadsGame( self , frame_parent ):
        frame_main          = bgui.Frame( frame_parent , border = 0 , size = ( 0.80 , 0.80 ), pos = ( 0.10 , 0.10 )  )
        frame_main.colors   = [( 0.0 , 0.0 , 0.0 , 0.50 ) for i in range(4)]

        list_pos_y  = [ 0.66 ,  0.45 , 0.24 , 0.03 ]
        numb_rg     = 2

        #frame_base_faixa         = bgui.Frame( frame_main , border = 0 , size = ( 0.08 , 0.08 ), pos = ( 0.10 , 0.10 )  )
        #frame_base_faixa.colors  = [( 0.0 , 0.0 , 0.0 , 0.60 ) for i in range(4)]

        #------------------------------------------------------------------------

        for index , numb_pos in enumerate( list_pos_y ):
            self.cardsLoadGame( frame_parent = frame_main , text_index = index ,  position = ( 0.05 , numb_pos  ) )


            

        return {
            
            "FRAME"             : frame_main ,

            "Text_descritions_buttons"  : bgui.Label( 
                                                parent     = frame_main ,
                                                text       = "Loads Game", 
                                                pt_size    = 40 , 
                                                pos        = [ 0.12 , 0.90 ] ,
                                                sub_theme  = 'Large', 
                                                options    =  self.opsion ),


            "button_voltar"  : self.buttonsImg( parent      = frame_main  , 
                                                sizes       = [ 0.05 , 0.05 ] , 
                                                positions   = [ 0.05 , 0.90 ] , 
                                                back_img    = BUTTONS_MAIN_DATA["button_start"][0], 
                                                over_img    = BUTTONS_MAIN_DATA["button_start"][1],
                                                ),


                                                           

            }

        
        pass
