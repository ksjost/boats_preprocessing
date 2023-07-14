import pandas as pd 

def get_image_boxes(id: str, df: pd.DataFrame, im_width=768, im_height=768) -> list:
    """
    Given image ID, creates a nested list of coordinates for each box in the image by decoding the 
    run-length encoding of the pixels which are labeled in the training set as containing boats.
    
    Args: 
        id: image ID/filename to be processed
        df: dataframe containing the image IDs and their corresponding encoded pixels
        im_width: width of the image being processed
        im_height: height of the image being processed
        
    Returns: 
        A nested list of normalized coordinates for each box in the image
    """
    boxes = []

    image_df = df.loc[[id]].reset_index()

    image_list = image_df["EncodedPixels"].to_list()

    len_df = len(image_list)

    # Iterate through the dataframe
    for index in range(len_df):
        # Process encoded pixels

        # nans are being read as floats
        if type(image_list[index]) == float:
            continue
        else:
            # Decode
            encoded = image_list[index]

            # Split the encoded string on " "
            encode_list = encoded.split(" ")

            # Convert each item in list to int
            encode_list = [int(x) for x in encode_list]

            # Initialize lists to separate items into x- and y-coordinates
            xs = []
            ys = []

            # Iterate through every other item in the encoded list
            len_encode = len(encode_list)
            for i in range(0, len_encode - 1, 2):
                pixel_pos = encode_list[i]
                pixel_len = encode_list[i + 1]

                # Compute the x- and y-coordinates of the pixel column
                x_pixel_pos = pixel_pos // im_width
                y_pixel_pos = pixel_pos % im_height
                lower_y = y_pixel_pos + pixel_len - 1

                xs.append(x_pixel_pos)
                ys.append(y_pixel_pos)
                ys.append(lower_y)

            # Corners of the bounding box
            x_min = min(xs)
            x_max = max(xs)
            y_min = min(ys)
            y_max = max(ys)

            # Compute coordinates of the bounding box
            width = x_max - x_min
            height = y_max - y_min
            x_center = x_min + width / 2
            y_center = y_min + height / 2

            # Normalize the coordinates
            x_center = x_center / im_width
            y_center = y_center / im_height
            width = width / im_width
            height = height / im_height
        
        # Append x_center, y_center, width, height to boxes
        boxes.append([x_center, y_center, width, height])
    
    return boxes