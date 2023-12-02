import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="main.py",
    # base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Cheatcl",
    version = "1.0",
    description = "download app & cheat etc",
    author = "necakco",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)