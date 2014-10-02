import sys
import PIL.Image
sys.modules['Image'] = PIL.Image

bind = '127.0.0.1:8000'

workers = 4

timeout = 30
