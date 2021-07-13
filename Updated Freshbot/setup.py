
import sys
from cx_Freeze import setup, Executable
import os

PYTHON_INSTALL_DIR=os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')

include_files=[(os.path.join(PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),os.path.join('lib','tk86.dll')),
               (os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll'),os.path.join('lib','tcl86.dll'))]

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables=[Executable('Jarvis_v2.0.py',base=base,icon="robot.ico",shortcutName='J.A.R.V.I.S',shortcutDir="DesktopFolder")]

setup(  name = "J.A.R.V.I.S",
        version = "2.0",
        description = "My GUI application!",
        options = {"build_exe": {"packages":{"tkinter","pyttsx3","speech_recognition","pywhatkit","requests","threading","pynput","pyautogui","selenium","difflib","zipfile"},"include_files":include_files}},
        executables = executables  )