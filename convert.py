from PIL import Image
import os

def convert_jpg_to_png(directory="."):
    # List all files in the directory
    files = os.listdir(directory)

    # Filter for .jpg files
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]

    for jpg_file in jpg_files:
        # Open the jpg file
        img = Image.open(jpg_file)
        
        # Convert and save as png
        png_file = os.path.splitext(jpg_file)[0] + '.png'
        img.save(png_file)
        
        # Delete the original jpg file
        os.remove(jpg_file)

    print(f"Converted {len(jpg_files)} jpg files to png.")

if __name__ == "__main__":
    convert_jpg_to_png()
