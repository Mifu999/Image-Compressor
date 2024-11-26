# Image Compressor

This repository contains a Python script that resizes and compresses images to a specified width and height, with the option to change the file format and extension. It includes a Python script (`main.py`) for resizing the image and a batch file (`Compressor.bat`) for easily running the script on Windows.

## Features

- Resize images to custom dimensions (width and height in pixels).
- Convert images to different formats (e.g., PNG, JPG, JPEG).
- The output image is saved in the same folder as the script with the specified extension.

## Requirements

Before using the script, make sure you have the following installed:

- Python 3.x
- Pillow library (Python Imaging Library Fork)

You can install Pillow using pip:

```
pip install Pillow
```

## How to Use

1. **Clone or download the repository** to your local machine.
   
2. **Install Pillow** (if you haven't already):
   ```
   pip install Pillow
   ```

3. **Run the script**:
   - **Using the Batch File (Windows)**:
     Simply double-click `Compressor.bat` to launch the Python script. This will open a command prompt window and ask for the necessary inputs.
   - **Using Python (cross-platform)**:
     Run the following command in your terminal or command prompt:
     ```
     python main.py
     ```

4. The script will prompt you to:
   - Enter the path of the image you want to resize and compress.
   - Enter the desired output file name (the default is `output`).
   - Specify the output file extension (e.g., `png`, `jpg`, `jpeg`).
   - Provide the new image width and height in pixels.

5. **View the result**:
   The resized and compressed image will be saved in the same directory as the script with the specified file extension.

## Example

1. When prompted for the image path:
   ```
   Enter the path of the image (use parentheses if needed): "C:\Users\YourUsername\Pictures\image.png"
   ```

2. For the output file name:
   ```
   Enter the output file name (default: output): resized_image
   ```

3. For the output file extension:
   ```
   Output file extension (png, jpg, jpeg...): jpg
   ```

4. For the dimensions:
   ```
   Enter the desired width of the image (in pixels): 800
   Enter the desired height of the image (in pixels): 600
   ```

5. After the script runs, you will find the resized and compressed image saved as `resized_image.jpg` in the same folder as the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
