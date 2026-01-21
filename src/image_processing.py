import os
import logging
from datetime import datetime

from PIL import Image
import imagehash

logger = logging.getLogger(__name__)

def extract_image_metadata(image_path: str) -> dict:
    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)
    
    filesize = os.path.getsize(image_path)

    with Image.open(image_path) as img:
        width, height = img.size
        fmt = img.format
        phash = str(imagehash.phash(img))

    return {
        "image_metadata": {
            "width": width,
            "height": height,
            "format": fmt,
            "filesize_bytes": filesize,
            "phash": phash,
            "processed_at": datetime.utcnow(),
        }
    }