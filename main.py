import os
import sys


# Obtener la ruta donde se está ejecutando la App en Android
current_path = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_path, 'src')

# Añadir src al path solo si no está ya
if src_path not in sys.path:
    sys.path.append(src_path)


# Configuración de rutas para el ejecutable (.exe)
if hasattr(sys, '_MEIPASS'):
    # Carpeta temporal de PyInstaller
    base_path = sys._MEIPASS
    os.chdir(base_path)
else:
    # Carpeta normal de desarrollo
    base_path = os.path.abspath(".")

# Añadimos las rutas al sistema para que Python encuentre tus carpetas
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, 'src'))

# CORRIGE ESTO según dónde esté My_App:
try:
    from view.gui import My_App 
except ImportError:
    from view.gui import My_App # Intenta esta si gui está dentro de view

if __name__ == '__main__':
    # Asegúrate de que el nombre de la clase y el método sean correctos
    My_App.liquidador_nomina().run()