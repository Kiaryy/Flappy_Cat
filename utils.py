import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def collisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    if a_x + a_width >= b_x and a_x <= b_x + b_width:
        if a_y + a_height >= b_y and a_y <= b_x + b_height:
            return True
        else:
            return False



