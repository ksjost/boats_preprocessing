import cv2
import os

def resize_cv(source_dir: str, id: str, new_dir, width=640, height=640) -> None: 
    """
    Resizes the images to the required 640x640 size
    
    Args: 
        source_dir: current directory containing the image
        id: image ID/filename of the image to be resized
        new_dir: directory to store the resized image
        
    Returns: 
        None
    """
    source_path = os.path.join(source_dir, id)
    img = cv2.imread(source_path)
    desired_size = (width, height)
    resized_img = cv2.resize(img, desired_size, interpolation=cv2.INTER_LINEAR)
    new_path = os.path.join(new_dir, id)
    cv2.imwrite(new_path, resized_img)