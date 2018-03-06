# StepUp file

from cx_Freeze import setup, Executable

base = None


executables = [Executable("Gomoku.pyw", base="Win32GUI")]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':['Tkinter', 'ttk', '__future__', 'PIL'], "include_files": [
    "game.gif"]
    },

}

setup(
    name = "Tic Tac Toe simple game",
    options = options,
    version = "1.0.0",
    description = '<any description>',
    executables = executables
)