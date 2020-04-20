from cx_Freeze import setup, Executable

base = None

executables = [Executable("gui.py", base=base)]

packages = ["idna","tkinter","encrypt","numpy","time"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Hill Cipher GUI",
    options = options,
    version = "3.8",
    description = 'Launches the Hill Cipher GUI',
    executables = executables
)
