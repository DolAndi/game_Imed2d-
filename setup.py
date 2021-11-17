import cx_Freeze
executables = [cx_Freeze.Executable(
    script="game_principal.py", icon="assets/pikachu.ico")]

cx_Freeze.setup(
    name="Iron Man Dead",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables=executables
)