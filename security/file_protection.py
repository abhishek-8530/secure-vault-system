import os

def hide_file(path):
    os.system(f'attrib +h "{path}"')

def unhide_file(path):
    os.system(f'attrib -h "{path}"')

def open_file(path):
    os.startfile(path)