# Game-Toolset-B

>  É um framewolk simples com uma estrutura de pastas para a criação de jogos com o Blender-Game-Engine 2.79b.

------

### Estrutura de pastas para o projeto

    > Projeto/
        @> audio/
        @> blend/
            > scripts/

                -------------------------
                > enimy/
                    > components/
                    > libs/
                        - classes.py
                    > modulos/
                        - main.py
                -------------------------
                > game/
                    > components/
                    > libs/
                        - classes.py
                    > modulos/
                        - main.py
                ------------------------- 
                > menus/
                    > components/
                    > database/
                    > image
                        - imagens.png , jpg , psd 
                    > libs/
                        - classes.py
                    > modulos/
                        - main.py
                -------------------------
                > player/
                    > components/
                    > libs/
                        - classes.py
                    > modulos/
                        - main.py

            <-> main.blend

        
        @> files
            - txt
            - XML
            - ...

        @> modelo_3d/
            > assets_game/
                > textures/
                    - imagens.png , jpg , psd 
                
                > Props
                    - OBJs , FBX , assets.blend
            > Player/
                > animations/
                    - Action.fbx

                > Textures/
                    - imagens.png , jpg , psd 

                > Obj/
                    - model.obj , model.fbx

            > Enimes/
                > enimes_01/
                    > animations/
                        - Action.fbx

                    > Textures/
                        - imagens.png , jpg , psd 

                    > Obj/
                        - model.obj , model.fbx
