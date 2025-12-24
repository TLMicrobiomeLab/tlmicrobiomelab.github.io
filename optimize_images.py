import os
from PIL import Image

def optimize_images(folder_path):
    # Maximum dimension for team photos (400px is plenty for a 150px circle)
    MAX_SIZE = (400, 400) 
    
    # Loop through all files in the images folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, filename)
            
            try:
                with Image.open(file_path) as img:
                    # distinct logic for the Logo (keep it crisp, don't resize if small)
                    if "logo" in filename.lower():
                        continue 
                        
                    # Calculate new size maintaining aspect ratio
                    img.thumbnail(MAX_SIZE)
                    
                    # Save it back over the original file
                    # optimize=True reduces file size without losing quality
                    img.save(file_path, optimize=True, quality=85)
                    print(f"Optimized: {filename}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    optimize_images("images")
