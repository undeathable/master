# StepUp file

from cx_Freeze import setup, Executable

base = None


executables = [Executable("Calc.pyw", base="Win32GUI")]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':['Tkinter', 'ttk', '__future__'],
    },

}

setup(
    name = "<any name>",
    options = options,
    version = "1.0.0",
    description = '<any description>',
    executables = executables
)