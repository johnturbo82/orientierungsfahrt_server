import os

SVG_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'symbols')

def replace_fill_black_with_white(svg_path):
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content_new = content.replace('#000000', '#ffffff')
    content_new = content_new.replace('"#000"', '"#ffffff"')
    if content != content_new:
        base, ext = os.path.splitext(svg_path)
        new_path = f"{base}_dark{ext}"
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print(f"Geändert und gespeichert als: {new_path}")

if __name__ == "__main__":
    for filename in os.listdir(SVG_DIR):
        if filename.lower().endswith('.svg'):
            replace_fill_black_with_white(os.path.join(SVG_DIR, filename))