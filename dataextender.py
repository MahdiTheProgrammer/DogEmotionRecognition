import os
import cv2
import numpy as np
from skimage.transform import rotate, rescale

# Input and output paths
input_folder = "D:\\Projects\\Python\\Dog_Emotion\\dataset\\final"
output_folder = "D:\\Projects\\Python\\Dog_Emotion\\dataset\\moredata"

# Augmentation parameters
rotation_range = (-30, 30)  # Range of rotation angles in degrees
translation_range = (-20, 20)  # Range of translation in pixels
zoom_range = (0.8, 1.2)  # Range of zoom factors

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through each class folder
class_folders = os.listdir(input_folder)
for class_folder in class_folders:
    class_folder_path = os.path.join(input_folder, class_folder)
    if os.path.isdir(class_folder_path):
        output_class_folder = os.path.join(output_folder, class_folder)
        if not os.path.exists(output_class_folder):
            os.makedirs(output_class_folder)
        
        image_files = os.listdir(class_folder_path)
        for image_file in image_files:
            image_path = os.path.join(class_folder_path, image_file)
            image = cv2.imread(image_path)
            
            # Perform image augmentation
            augmented_images = []
            for i in range(10):  # Expand dataset 10 times
                # Random rotation
                angle = np.random.uniform(rotation_range[0], rotation_range[1])
                rotated_image = rotate(image, angle, mode='reflect', preserve_range=True).astype(np.uint8)
                
                # Random translation
                tx = np.random.uniform(translation_range[0], translation_range[1])
                ty = np.random.uniform(translation_range[0], translation_range[1])
                translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
                translated_image = cv2.warpAffine(rotated_image, translation_matrix, (image.shape[1], image.shape[0]))
                
                # Random zoom
                zoom_factor = np.random.uniform(zoom_range[0], zoom_range[1])
                zoomed_image = rescale(translated_image, zoom_factor, mode='reflect', preserve_range=True).astype(np.uint8)
                
                augmented_images.append(zoomed_image)
            
            # Save augmented images
            filename = os.path.splitext(image_file)[0]
            for i, augmented_image in enumerate(augmented_images):
                output_path = os.path.join(output_class_folder, f"{filename}_augmented_{i}.jpg")
                cv2.imwrite(output_path, augmented_image)
