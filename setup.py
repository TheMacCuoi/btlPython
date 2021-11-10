import sys
from cx_Freeze import setup, Executable

build_exe_options = {'include_files': ['level', 'img']}


setup(
    name ='Tomb of the mark',
    author='Ngoc-Tuan-Tung',
    version = '1.0',
    options={'build_exe': build_exe_options},
    executables = [Executable('main.py', base = None)])



