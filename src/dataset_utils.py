from pathlib import Path

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def read_yolo_labels(label_path):
    '''
    Read YOLO format label file
    Return list of dictionaries containing label information
    '''

    annotations=[]
    with open(label_path,"r") as file:
        for line in file:
            values= line.strip().split()

            if not values:
                continue

            class_id= int(values[0])
            x_center = float(values[1])
            y_center = float(values[2])
            width = float(values[3])
            height = float(values[4])

            annotations.append({
                "class_id": class_id,
                "x_center": x_center,
                "y_center": y_center,
                "width": width,
                "height": height
            })

    return annotations

def yolo_to_box(annotation, image_width, image_height):
    '''
    Convert YOLO coordinates to pixel bounding box coordinates
    '''

    

