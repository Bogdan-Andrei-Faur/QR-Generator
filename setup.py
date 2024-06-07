from setuptools import setup

APP = ['generator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['qrcode', 'PIL'],
    'includes': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)