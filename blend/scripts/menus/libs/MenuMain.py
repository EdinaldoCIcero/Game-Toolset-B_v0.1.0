from bge import logic,events , types
import bgui
import bgui.bge_utils
import bge
import aud

#-----------------------------------------------------
from scripts.menus.libs.ElementsUIMain import MenuMainElements

#-----------------------------------------------------



scene       = logic.getCurrentScene()
tc          = logic.keyboard.events
global_dict = bge.logic.globalDict



path    = bge.logic.expandPath("//scripts/Uis/imagens_ui/")
opsion  = bgui.BGUI_DEFAULT | bgui.BGUI_DEFAULT


#----------------
global_dict["INIT_GAME"] = False

#---------------




class MenuMainLayoutOne(bgui.bge_utils.Layout):
    def __init__( self, sys , data ):
        super().__init__( sys , data)
        #################################

        #--------------------------------
        
        #------- OBJETOS PROPS ---------#

        self.MainFrame          = bgui.Frame( self , border = 0 , size = ( 1 , 1 ), pos = ( 0 , 0 )  )
        self.MainFrame.colors   = [( 0.0 , 0.0 , 0.0 , 0.0 ) for i in range(4)]

        #--------------------------------
        self.elements_ui_one = MenuMainElements()


        #----- Menu start simples --------------------
        self.button_start   = self.elements_ui_one.menuStart( frame_parent = self.MainFrame )
        #self.button_start["FRAME"].visible = False
        
        self.manu_main      = self.elements_ui_one.menuMain( frame_parent = self.MainFrame )
        self.manu_main["FRAME"].visible = False

        self.menu_loads_game = self.elements_ui_one.menuLoadsGame( frame_parent = self.MainFrame )
        self.menu_loads_game["FRAME"].visible = False
        



        

        #----- ClickEvents Menu Buttons ----------------------------------------------
        self.button_start["button_start_img"].on_click  = self.buttonStartMain
        self.manu_main["button_start"].on_click         = self.button_init_game_click
        self.manu_main["button_load_game"].on_click     = self.button_load_game_click


        #-------- Buttuns Voltar ------------------------------------------------------
        self.menu_loads_game["button_voltar"].on_click     = self.button_load_game_voltar_click
            


        #---- MouseOvers buttons-------------------------------------------------------
        self.manu_main["button_start"].on_hover         = self.startMouseOverButton
        self.manu_main["button_start"].on_mouse_exit    = self.exitStartMouseOverButton
        self.manu_main["button_load_game"].on_hover     = self.buttonLoadGameOver
        self.manu_main["button_opisões"].on_hover       = self.buttonOpisoesMouseOver
        self.manu_main["button_sair"].on_hover          = self.buttonSairMouseOver

        


    #--------- BUTTONS CALL BACKS MENUS ----------------------

    def buttonStartMain( self , widget ):#Button start
        print( "button start confirmations ")
        self.button_start["FRAME"].visible  = False
        self.manu_main["FRAME"].visible     = True
        
        pass
    

    def button_init_game_click( self , widget ):
        global_dict["INIT_GAME"] = True

        pass


    def button_load_game_click( self , widget ):
        self.manu_main["FRAME"].visible         = False
        self.menu_loads_game["FRAME"].visible   = True

        pass

    def button_load_game_voltar_click( self , widget ):
        self.manu_main["FRAME"].visible         = True
        self.menu_loads_game["FRAME"].visible   = False

        pass





        #logic.endGame()











    #--- -CalBacks Mouse overs menu principal ----------------------
    def startMouseOverButton( self , widget):
        self.manu_main["Text_descritions_buttons"].text = "inicia um novo jogo"
        pass

    def exitStartMouseOverButton( self , widget):
        self.manu_main["Text_descritions_buttons"].text = ""
        pass


    def buttonLoadGameOver( self , widget):
        self.manu_main["Text_descritions_buttons"].text = "carregar um jogo salvo"
        pass
    

    def buttonOpisoesMouseOver( self , widget):
        self.manu_main["Text_descritions_buttons"].text = "Ver configurações do jogo "
        pass


    def buttonSairMouseOver( self , widget):
        self.manu_main["Text_descritions_buttons"].text = "inicia um novo jogo"
        pass
    
  