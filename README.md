## car_objects_detection-classification_system 
Custom YOLOv8 object detection_classification project with dataset preprocessing, model training on Colab, and offline video prediction on local system.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-red.svg)
![Google Colab](https://img.shields.io/badge/Google%20Colab-Ready-orange.svg)

This project demonstrates **Object Detection_classification** using the **YOLOv8 model** trained on a custom dataset.  
It includes preprocessing scripts, model training on Google Colab, and video stream inference on local systems.

---

##  Features
-  Preprocessing of dataset (images + labels)  
-  YOLOv8 training on Google Colab with GPU support  
-  Offline video stream inference using trained weights  
-  End-to-end pipeline (dataset → training → inference)


##  Repository Structure
├── utils.py # Preprocess dataset (resize, RGB convert, copy labels)
├── model_train.ipynb # YOLOv8 model training notebook (Colab)
├── stream_inference.ipynb # Offline video stream inference notebook
├── dataset.yml # Dataset configuration file
└── README.md # Project documentation


##  Installation

### 1. Clone the Repository
git clone https://github.com/Abdul-Hamidd/car_objects_detection-classification_system.git
cd car_objects_detection-classification_system
2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
3. Install Dependencies
pip install ultralytics opencv-python
 Usage Guide
1. Dataset Preprocessing
Run preprocessing script to resize images, convert them to RGB, and copy labels:

python utils.py
2. Training on Google Colab
Open train_model.ipynb in Google Colab.

Update the dataset path in dataset.yml.

Run all cells to train YOLOv8 (yolov8s.pt used as base).

The trained model weights will be saved in your Google Drive.

3. Offline Video Inference
Run video_inference.ipynb on local system:

Update paths for:

VIDEO_PATH → input video file

MODEL_PATH → trained model weights (best.pt)

OUTPUT_VIDEO_PATH → output video file

Run the notebook, and the processed video will be saved with bounding boxes.

## Example Results
Preprocessed dataset 

Trained YOLOv8 model 

Inference video with bounding boxes 

 Future Improvements
 Add support for multiple classes (currently only car).

 Deploy model as a Flask/FastAPI web app.

 Real-time webcam inference.

 Hyperparameter tuning for higher accuracy.

## Tech Stack
Language: Python 3.10+

Libraries: Ultralytics YOLOv8, OpenCV

Platform: Google Colab (for training), Local System (for inference)

## Author
Developed by Abdul Hamidd 


