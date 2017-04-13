import sys		
import PIL.Image		
sys.modules['Image'] = PIL.Image		
		
bind = '0.0.0.0:1331'		
		
workers = 4		
		
timeout = 30
