import os

def write_text(boat_class: int, text_dir: str, id: str, boxes: list) -> None: 
    """
    Writes and saves the coordinates of the boats to a text file if at lease 1 boat is present in the image. 
    Writes and saves a blank text file, otherwise.
    
    Args: 
        boat class: 0 or -9999 indicating the classification of the bounding box ("boat" or "no boat", respectively)
        text_dir: directory to save the text file in 
        id: image ID/file name of the image corresponding to the textfile
        boxes: nested list of box coordinates to be written into the textfile
        
    Returns: 
        None
    """
    txt_id = id.replace(".jpg", ".txt")

    path = os.path.join(text_dir, txt_id)

    with open(path, "w") as file: 

        for box in boxes: 
            line = " ".join(str(coordinate) for coordinate in box)

            if boat_class == 0:
                file.write(f"{boat_class} {line}\n")
            else: 
                file.write("")