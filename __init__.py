import shutil
import folder_paths
import os, sys, subprocess

try:
   from pyclustering.cluster import kmeans
   import hqx
except ImportError:
   print(f"## PixelArtDetector: installing dependencies")
   my_path = os.path.dirname(__file__)
   requirements_path = os.path.join(my_path, "requirements.txt")
   try:
      subprocess.check_call([sys.executable, '-s', '-m', 'pip', 'install', '-r', requirements_path])
   except:
      try:
         subprocess.check_call([sys.executable, '-s', '-m', 'pip', 'install', '-r', requirements_path, '--use-pep517'])
      except:
         print(f"## [ERROR] PixelArtDetector: Could not install pyclustering library.")
   print(f"## PixelArtDetector: installing dependencies done.")
    
print("### Loading: PixelArtDetector")

comfy_path = os.path.dirname(folder_paths.__file__)

def setup_js():
   webp_path = os.path.dirname(__file__)
   js_dest_path = os.path.join(comfy_path, "web", "extensions", "pixelArtDetector")
   js_src_path = os.path.join (webp_path, "pixelArtDetector")
     
   print("Copying PixelArtDetector JS files for Workflow loading")
   shutil.copytree (js_src_path, js_dest_path, dirs_exist_ok=True)        

setup_js()

from .PixelArtDetector import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']