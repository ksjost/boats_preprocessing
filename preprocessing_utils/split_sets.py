import os 
import random
import shutil 

def split(source_im: str, source_txt: str, train_im: str, train_txt: str, val_im: str, val_txt: str, seed=123) -> None: 
    """
    Randomly split files from source directory into train and validation sets. 
    Creates and copies files to respective directories.
    
    Args: 
        source_im: directory of images to be split
        source_txt: directory of text files corresponding to source_im
        train_im: directory name for training set images
        train_txt: directory name for training set labels
        val_im: directory name for validation set images
        val_txt: directory name for validation set labels
    
    Returns: 
        None
    """
    source_list = os.listdir(source_im)
    split_index = int(len(source_list) * .2)

    random.seed(seed)
    random.shuffle(source_list)

    for k, image in enumerate(source_list):
        text = image.replace(".jpg", ".txt")
        source_image_path = os.path.join(source_im, image)
        source_text_path = os.path.join(source_txt, text)
        destination_image_path = os.path.join(train_im, image)
        destination_text_path = os.path.join(train_txt, text)
        if k < split_index:
            destination_image_path = os.path.join(val_im, image)
            destination_text_path = os.path.join(val_txt, text)
        shutil.copy(source_image_path, destination_image_path)
        shutil.copy(source_text_path, destination_text_path)