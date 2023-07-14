import os
from PIL import Image

def is_image(dir: str, id: str) -> bool:
    """
    Verify that an image name exists in a directory
    
    Args: 
        dir: directory in which to check
        id: image ID/filename to check for
        
    Returns: 
        True/False
    """
    path = os.path.join(dir, id)
    try: 
        img = Image.open(path)
        img.verify()
        return True
    except (IOError, SyntaxError) as e: 
        return False