import os, sys


def clamp(value, min, max):
    """Limita el valor 
    """
    if value < min:
        return min
    if value > max:
        return max
    return value

def map(value, leftMin, leftMax, rightMin, rightMax):
    """Mapea el valor dado al rango indicado
    
    Argumentos:
        value (int or float): valor a mapear
        leftMin (int or float): minimo valor original
        leftMax (int or float): maximo valor original
        rightMin (int or float ): minimo valor a mapear
        rightMax (int or flot): maximo valor a mapear
    
    Returns:
        float: valor mapeado al rango indicado
    """
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def resource_path(relative_path):
    """ Da el destino de los assets cuando se use Pyinstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)



def collisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)



