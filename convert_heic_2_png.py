import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(input_folder):
    # Create the output folder if it doesn't exist
    output_folder = os.path.join(input_folder, 'png')
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.heic'):
            heic_file_path = os.path.join(input_folder, filename)
            png_file_name = os.path.splitext(filename)[0] + '.png'
            png_file_path = os.path.join(output_folder, png_file_name)

            try:
                # Open HEIC file using pillow_heif
                heif_file = pillow_heif.open_heif(heic_file_path)
                
                # Convert HEIC to PIL Image
                heif_image = heif_file[0]
                image_data = heif_image.data
                image = Image.frombytes(
                    heif_image.mode, 
                    heif_image.size, 
                    image_data, 
                    "raw", 
                    heif_image.mode, 
                    heif_image.stride
                )

                # Save as PNG
                image.save(png_file_path, "PNG")
                
                print(f"Converted {filename} to {png_file_name}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing HEIC images: ")
    convert_heic_to_png(input_folder)
