from cx_Freeze import setup, Executable
from multiprocessing import Queue
import os, sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {"packages": ["os", "idna", "sys"], "excludes": ["tkinter"], "include_files":["Resources/icons/fonero.ico"]}
setup( name = "Fonero GUI Wallet",
version = "1.3.0.1",
description = "Fonero GUI Wallet for Linux",
options = {"build_exe": build_exe_options},
executables = [Executable("wallet.py", base=base, icon='Resources/icons/fonero.ico')])
