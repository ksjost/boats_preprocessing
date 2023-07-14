import numpy as np
import pandas as pd
import os
from PIL import Image, ImageDraw
import time 
import cv2
import argparse
from preprocessing_utils import bounding_boxes, image_exists, resize_image, split_sets, write_file

def main():
    # Main program

    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("labels_path", help="Name of .csv containing labels")
    args = parser.parse_args()

    im_df = pd.read_csv(args.labels_path)
    im_df_fast = im_df.set_index("ImageId", inplace=False)

    # Initialize directory names for required directories
    source_dir = "split"
    resized_source = "resized_split"
    source_text = "text_files"
    train_image = "train_image"
    train_text = "train_text"
    validation_image = "val_image"
    validation_text = "val_text"
    test_source = "test"
    resized_test = "resized_test"

    # Make required directories
    os.makedirs(resized_source, exist_ok=True)
    os.makedirs(source_text, exist_ok=True)
    os.makedirs(train_image, exist_ok=True)
    os.makedirs(train_text, exist_ok=True)
    os.makedirs(validation_image, exist_ok=True)
    os.makedirs(validation_text, exist_ok=True)
    os.makedirs(resized_test, exist_ok=True)

    # Resize test images to 640x640 pixels
    test_images = os.listdir(test_source)
    for j, image in enumerate(test_images):
        resize_image.resize_cv(test_source, image, resized_test)
    
    # Convert image ID series to list
    img_IDs = im_df["ImageId"].to_list()

    # Remove duplicate image IDs
    img_IDs = list(set(img_IDs))

    # Iterate through the :no duplicate" list
    for i, id in enumerate(img_IDs):

        if image_exists.is_image(source_dir, id):

            # Resize training/validation images to 640x640 pixels
            resize_image.resize_cv(source_dir, id, resized_source)

            # Get boxes from each image
            boxes = bounding_boxes.get_image_boxes(id, im_df_fast)

            # Classify images
            if len(boxes) > 0:
                boat_class = 0
            else: 
                boat_class = -9999
            
            # Write textfile
            write_file.write_text(boat_class, source_text, id, boxes)
            if i % 10000 == 0:
                end_time = time.time()
                print(f"{i} images in {end_time - start_time} seconds")
        
        else:
            continue

    # Split validation set
    split_sets.split(resized_source, source_text, train_image, train_text, validation_image, validation_text)

if __name__ == "__main__":
    main()