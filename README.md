# Breed Cutter

Breed Cutter is a Python script that uses YOLOv5 object detection to crop dog images to a specific size while maintaining the aspect ratio and avoiding white or black bars.

## Requirements

- Python 3.x
- PyTorch
- Pillow
- YOLOv5

## Installation

1. Clone the repository or download the script files.

2. Create a new conda environment and activate it:
conda create --name breed-cutter python=3.x
conda activate breed-cutter

3. Install PyTorch by following the instructions on the [PyTorch website](https://pytorch.org) based on your operating system and CUDA version.

4. Install the required dependencies by running the following command:
pip install -r requirements.txt

5. Download YOLOv5 by running the following command:
git clone https://github.com/ultralytics/yolov5.git

6. Change to the YOLOv5 directory and install the required packages:
cd yolov5
pip install -r requirements.txt


## Usage

1. Place the dog images you want to crop in a directory (e.g., `input_images`).

2. Open the `breed_cutter.py` script and modify the following variables if necessary:
- `image_dir`: Set the path to the directory containing the input images.
- `output_dir`: Set the path to the directory where the cropped images will be saved.

3. Run the script using the following command:
python breed_cutter.py

4. The script will process the images, crop them to 300x300 pixels while maintaining the aspect ratio, and save the cropped images in the specified output directory.

## License

This project is licensed under the [MIT License](LICENSE).
