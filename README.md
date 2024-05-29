# HEIC-to-PNG-Converter
Convert HEIC images to PNG format using this Python script. Leveraging the pillow and pillow-heif libraries, it processes multiple images concurrently. Simply place your HEIC files in a folder, run the script, and get PNGs in a new png subfolder. Perfect for batch processing on any system with Python.

## Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

You will also need to install the required Python libraries. You can do this using `pip`:
```
pip install pillow pillow-heif
```
## Usage

1. **Clone the repository**:
```
git clone https://github.com/JordiSpranger/HEIC-to-PNG-Converter.git
cd heic-to-png-converter
```

2. **Place your HEIC images in a folder**.

3. **Run the script**:
```
python convert_heic_2_png.py
```

4. **Enter the path to the folder containing HEIC images** when prompted.

The script will convert all HEIC images in the specified folder to PNG format and save them in a subfolder named `png`.

## Script Details

The script `convert_heic_2_png.py` performs the following steps:

1. **Imports necessary libraries**.
2. **Registers HEIF opener** to handle HEIC files.
3. **Defines a function to convert a single HEIC file to PNG**.
4. **Defines a function to convert all HEIC files in the specified folder**.
5. **Prints the conversion status for each file**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
