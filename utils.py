from PIL import Image
import os
from datetime import datetime
import time

def save_image(file):
    upload_folder = os.path.join('static', 'uploads')
    
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    filename = f"{int(time.time())}.jpg"  
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    
    return filename

def extract_metadata(image_filename):
    metadata = {
        'filename': image_filename,
        'camera_model': 'Canon EOS 5D',
        'exposure': '1/200s',
        'location': 'Lat: 40.748817, Lon: -73.985428'
    }
    return metadata
