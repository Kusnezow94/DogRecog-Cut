import torch
from PIL import Image, ImageOps
import os

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def expand_crop_area(img, detection_box, expansion_factor=1.5, target_size=(1080, 924)):
    # Extract detection box coordinates and calculate its center and dimensions
    x1, y1, x2, y2 = detection_box
    center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
    det_width, det_height = x2 - x1, y2 - y1

    # Calculate expanded crop dimensions
    exp_width, exp_height = det_width * expansion_factor, det_height * expansion_factor

    # Calculate new crop box, ensuring it does not exceed the image boundaries
    crop_x1 = max(center_x - exp_width // 2, 0)
    crop_y1 = max(center_y - exp_height // 2, 0)
    crop_x2 = min(center_x + exp_width // 2, img.width)
    crop_y2 = min(center_y + exp_height // 2, img.height)

    # Crop the image to the new expanded area
    cropped_img = img.crop((crop_x1, crop_y1, crop_x2, crop_y2))

    # Calculate the aspect ratio of the cropped image and the target size
    cropped_aspect_ratio = cropped_img.width / cropped_img.height
    target_aspect_ratio = target_size[0] / target_size[1]

    if cropped_aspect_ratio > target_aspect_ratio:
        # Cropped image is wider than the target size
        new_height = target_size[1]
        new_width = int(new_height * cropped_aspect_ratio)
        resized_img = cropped_img.resize((new_width, new_height), Image.LANCZOS)
        left = (new_width - target_size[0]) // 2
        top = 0
        right = left + target_size[0]
        bottom = target_size[1]
    else:
        # Cropped image is taller than the target size
        new_width = target_size[0]
        new_height = int(new_width / cropped_aspect_ratio)
        resized_img = cropped_img.resize((new_width, new_height), Image.LANCZOS)
        left = 0
        top = (new_height - target_size[1]) // 2
        right = target_size[0]
        bottom = top + target_size[1]

    final_img = resized_img.crop((left, top, right, bottom))
    return final_img

# Specify the directory containing images
image_dir = "/BreedCutter/Files"
output_dir = "/BreedCutter/Cut"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process images
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_dir, filename)
        output_path = os.path.join(output_dir, "cropped_" + filename)

        # Load the image into 'img' using PIL
        img = Image.open(image_path)

        # Perform inference
        results = model(image_path)
        
        # Extract dog bounding boxes (class ID for dog in COCO is 16)
        dog_boxes = results.xyxy[0]  # Bounding boxes
        dog_boxes = [box for box in dog_boxes if box[5] == 16]  # Filter for dogs

        # Inside your loop, replace the centered_crop call
        if dog_boxes:
            for box in dog_boxes:
                x1, y1, x2, y2 = map(int, box[:4])  # Corrected unpacking
                detection_box = (x1, y1, x2, y2)

                final_img = expand_crop_area(img, detection_box)
                final_img.save(output_path)
                print(f"Expanded cropped image saved to {output_path}")

