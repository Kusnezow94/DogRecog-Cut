# Breed Cutter

Breed Cutter is a Python script that uses YOLOv5 object detection to crop dog images to a specific size while maintaining the aspect ratio and avoiding any bars.

## Requirements

- Python 3.x
- PyTorch
- Pillow

## Installation

1. Clone the repository or download the script files.

2. Install the required dependencies by running the following command:

pip install -r requirements.txt


## Usage

1. Place the dog images you want to crop in a directory (e.g., `input_images`).

2. Open the `breed_cutter.py` script and modify the following variables if necessary:
- `image_dir`: Set the path to the directory containing the input images.
- `output_dir`: Set the path to the directory where the cropped images will be saved.

3. Run the script using the following command:

python run.py

4. The script will process the images, crop them to 300x300 pixels while maintaining the aspect ratio, and save the cropped images in the specified output directory.

## License

This project is licensed under the [MIT License](LICENSE).


