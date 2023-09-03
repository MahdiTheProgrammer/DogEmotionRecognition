import os
import cv2

def convert_to_grayscale(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the list of subfolders (classes) in the input folder
    classes = os.listdir(input_folder)

    for class_name in classes:
        class_folder = os.path.join(input_folder, class_name)
        output_class_folder = os.path.join(output_folder, class_name)

        # Create the class folder in the output directory
        if not os.path.exists(output_class_folder):
            os.makedirs(output_class_folder)

        # Process each image in the class folder
        for image_name in os.listdir(class_folder):
            image_path = os.path.join(class_folder, image_name)
            output_image_path = os.path.join(output_class_folder, image_name)

            # Read the image in color
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Save the grayscale image
            cv2.imwrite(output_image_path, gray_image)

        print(f"Converted images in '{class_name}' folder to grayscale.")

# Example usage
input_folder = "D:\\Projects\\Python\\paintings\\dataset\\images\\images"
output_folder ="D:\\Projects\\Python\\paintings\\dataset\\images-Gray-scale"

convert_to_grayscale(input_folder, output_folder)
