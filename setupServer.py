import cx_Freeze

executables = [cx_Freeze.Executable("server.py")]

cx_Freeze.setup(
    name="Server",
    options={"build_exe": {"packages":["socket", "queue", "threading"]                           
                           }
            },
    executables = executables

)