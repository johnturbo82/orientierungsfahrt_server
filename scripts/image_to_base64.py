import os
import base64
import sys

from scour import scour

# Import database functions
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from app.database import get_db_connection, init_db, write_images_to_db

ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'symbols')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'images.py')

def create_dark_svg(svg_content):
    """Create dark version of SVG by replacing black colors with white"""
    content_new = svg_content.replace('#000000', '#ffffff')
    content_new = content_new.replace('"#000"', '"#ffffff"')
    content_new = content_new.replace('#000;', '#ffffff;')
    content_new = content_new.replace('stroke:#000', 'stroke:#ffffff')
    content_new = content_new.replace('fill:#000', 'fill:#ffffff')
    return content_new

def encode_images_to_base64(directory):
    images = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        key = os.path.splitext(filename)[0]
        if filename.lower().startswith('saveas') or filename.lower().startswith('template'):
            continue
        if filename.lower().endswith('.svg'):
            with open(path, "r", encoding="utf-8") as svg_file:
                svg_content = svg_file.read()
                # Normal version
                minimized = scour.scourString(svg_content)
                b64_string = base64.b64encode(minimized.encode('utf-8')).decode('utf-8')
                images[key] = b64_string
                # Dark version
                dark_svg = create_dark_svg(svg_content)
                dark_minimized = scour.scourString(dark_svg)
                dark_b64_string = base64.b64encode(dark_minimized.encode('utf-8')).decode('utf-8')
                images[f"{key}_dark"] = dark_b64_string
        elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            with open(path, "rb") as img_file:
                b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                images[key] = b64_string
    return images

if __name__ == "__main__":
    images = encode_images_to_base64(ASSETS_DIR)
    write_images_to_db(images)
    print(f"Done! {len(images)} images processed.")
