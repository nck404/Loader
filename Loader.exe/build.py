from distutils.core import setup
import py2exe

setup(
    name='CyberY',
    description='python to exe payload',
    version='1.0',
    windows=[{
        'script': "logo-main.py",
        'icon_resources': [(0, './logo.ico')]
    }],
    options={'py2exe': {'bundle_files': 1, 'packages': 'ctypes',
                        'includes': 'base64,sys,socket,struct,time,code,platform,getpass,shutil'}},
    zipfile=None,
)
