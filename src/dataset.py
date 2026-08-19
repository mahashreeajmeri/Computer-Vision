from pathlib import Path
import torch
from torch.utils.data import Dataset
from PIL import Image
from .dataset_utils import read_yolo_labels, yolo_to_bbox

class SunspotDataset(Dataset):

    def __init__(self, image_dir, label_dir):
        self.image_dir = Path(image_dir)
        self.label_dir = Path(label_dir)

        self.image_files = sorted(self.image_dir.glob("*.jpg"))

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):

        #  get image
        image_path = self.image_files[index]
        image = Image.open(image_path).convert("RGB")
        image_width, image_height = image.size

        # find label
         