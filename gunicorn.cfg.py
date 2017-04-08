import sys		
import PIL.Image		
sys.modules['Image'] = PIL.Image		
		
bind = '0.0.0.0:8000'		
		
workers = 4		
		
timeout = 30
