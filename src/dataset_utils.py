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

def yolo_to_bbox(annotation, image_width, image_height):
    '''
    Convert YOLO normalized coordinates to pixel bounding box coordinates
    '''

    x_center= annotation["x_center"]*image_width
    y_center= annotation["y_center"]*image_height

    width= annotation["width"]*image_width
    height= annotation["height"]*image_height

    x_min = x_center - width / 2
    y_min = y_center - height / 2

    x_max = x_center + width / 2
    y_max = y_center + height / 2

    return x_min, y_min, x_max, y_max

def visualize_annotations(image_path, label_path):
    '''
    Draw the ground-truth bounding box annotations for an image and display it.
    '''

    image= Image.open(image_path)
    image_width, image_height= image.size
    annotations= read_yolo_labels(label_path)

    fig,ax= plt.subplots(figsize=(10,10))
    ax.imshow(image)

    for annotation in annotations:
        x_min, y_min, x_max, y_max= yolo_to_bbox(annotation, image_width, image_height)

        width = x_max - x_min
        height = y_max - y_min

        rectangle = patches.Rectangle(
            (x_min, y_min),
            width,
            height,
            linewidth=2,
            edgecolor="blue",
            facecolor="none"
        )

        ax.add_patch(rectangle)

        ax.text(
            x_min,
            y_min,
            f"Class {annotation['class_id']}",
            color="darkblue",
            backgroundcolor="white"
        )

    ax.axis("off")
    plt.show()


