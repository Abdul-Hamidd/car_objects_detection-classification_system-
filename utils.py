import os
import cv2
import shutil

# ==============================
# Function 1: Process Stored Dataset
# ==============================
def process_dataset(input_images, input_labels, output_images, output_labels, img_size=640):
    os.makedirs(output_images, exist_ok=True)
    os.makedirs(output_labels, exist_ok=True)

    images = [f for f in os.listdir(input_images) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    labels = [f for f in os.listdir(input_labels) if f.endswith('.txt')]

    for img_file in images:
        name, _ = os.path.splitext(img_file)
        label_file = f"{name}.txt"

        # Skip if label is missing
        if label_file not in labels:
            continue

        img_path = os.path.join(input_images, img_file)
        lbl_path = os.path.join(input_labels, label_file)

        # Read & check corrupt image
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Convert to RGB, resize, and save as JPG
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (img_size, img_size))
        out_img_path = os.path.join(output_images, f"{name}.jpg")
        cv2.imwrite(out_img_path, img)

        # Copy label file
        shutil.copy(lbl_path, os.path.join(output_labels, label_file))

    print("✅ Dataset preprocessing completed.")


# ==============================
# Function 2: Process Video Stream Frame
# ==============================
def process_stream_frame(frame, img_size=640):
    # Convert to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize
    frame = cv2.resize(frame, (img_size, img_size))

    return frame





