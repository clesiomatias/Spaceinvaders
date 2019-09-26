from cx_Freeze import setup, Executable
import sys
import  os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None
if sys.platform == "win32":
    base = "Win32GUI"
   

executables = [Executable("space_invaders4.pyw", base=base)]

packages = ["idna",'pygame','turtle','math','random','tkinter']
includes      = []
include_files = [r"C:\Users\ClésioNotebook\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll", \
                 r"C:\Users\ClésioNotebook\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll",'amb.wav',
				'bg.gif','explosion.wav','foguete.gif','heart.gif','invader.gif','laser.wav','player.gif'
				]

options = {
    'build_exe': {    
        "includes": includes, "include_files": include_files},
    }    



setup(
    name = "Space Invaders",
    version = "1.0",
    description = "Joguinho clone no clássico",
    options = options,
    executables = executables
 )
