from distutils.core import setup
import py2exe

# Define the path to your icon file
icon_path = '/icon.ico'

# Specify the main module (replace 'main' with your actual main module)
main_module = 'main-app.py'

# pywin32 COM pulls in a lot of stuff which we don't want or need.
excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list", "win32com.server"]

options = {
    "bundle_files": 1,  # create singlefile exe
    "compressed": 1,  # compress the library archive
    "excludes": excludes,
    "dll_excludes": ["w9xpopen.exe", "mswsock.dll", "powrprof.dll"],
    "icon_resources": [(1, icon_path)]  # Add the icon to the executable
}

setup(options={"py2exe": options},
      zipfile=None,
      console=[{'script': main_module, 'icon_resources': [(1, icon_path)]}]
      )
