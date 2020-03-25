import cx_Freeze

executables = [cx_Freeze.Executable("client.py")]

cx_Freeze.setup(
    name="Client",
    options={"build_exe": {"packages":["socket", "pygame", "threading", "os", "pygame.locals"],
             "include_files":["imagens/aguardando.png", "imagens/aguardandoAdversario.png", "imagens/branca.png", 
                              "imagens/brancaDama.png", "imagens/derrota.png", "imagens/icon.png", "imagens/inicio.png",
                              "imagens/preta.png", "imagens/pretaDama.png", "imagens/sobre.png", "imagens/SuaVez.png",
                              "imagens/vitoria.png"
                             ]
                           }
            },
    executables = executables

)