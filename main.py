from PIL import Image
import os

def resize_image(input_image_path, output_image_name, width, height, output_extension):
    Image.MAX_IMAGE_PIXELS = None

    try:
        with Image.open(input_image_path) as img:
            img = img.resize((width, height), resample=Image.LANCZOS)

            if output_extension.lower() == "jpg" or output_extension.lower() == "jpeg":
                img = img.convert("RGB")

            output_image_name += "." + output_extension
            output_image_path = os.path.join(os.getcwd(), output_image_name)
            img.save(output_image_path)
            print(f"The image has been compressed and saved as {output_image_path}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image_path = input("Enter the path of the image (use parentheses if needed): ")
    input_image_path = input_image_path.strip('"').strip()
    input_image_path = input_image_path.replace("\\", "/")
    
    output_image_name = input("Enter the output file name (default: output): ") or "output"
    output_extension = input("Output file extension (png, jpg, jpeg...): ")

    width = int(input("Enter the desired width of the image (in pixels): "))
    height = int(input("Enter the desired height of the image (in pixels): "))

    resize_image(input_image_path, output_image_name, width, height, output_extension)
