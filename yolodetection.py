# installing required modules

!pip install pyswarm

# importing required modules

import os
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
from collections import Counter as cnt
from pyswarm import pso
import numpy as np

# training the UA-DETRAC dataset

os.environ["YoLOv8_NUM_WORKERS"]="0"
model=YOLO('yolov8n') #yolo version 8
data_path=r"E:\ProjectPSO\traffic\UA-DETRAC_UPD_ANN\uadetrac.yaml"
model.train(
    data=data_path,
    epochs=5, #increase the number of epochs for better accuracy, but the training time would be more in such case
    device=0, #0-GPU, specify "cpu" if there is no GPU
    imgsz=640,
    batch=4,
    name='ua-detrac-yolov8n',
)
print("Training complete!")

# Computing the accuracy and valuation metrics

model=YOLO(r"E:\ProjectPSO\traffic\UA-DETRAC_UPD_ANN\yolo11n.pt")
metrics=model.val(data=r"E:\ProjectPSO\traffic\UA-DETRAC_UPD_ANN\uadetrac.yaml")
print(metrics)

# Sample predicted output for one of the validation/testing image data

model=YOLO(r"E:\ProjectPSO\traffic\UA-DETRAC_UPD_ANN\yolo11n.pt")
img_path=r"E:\ProjectPSO\traffic\UA-DETRAC_UPD_ANN\images\val\MVI_39031_img00039.jpg"
results=model(img_path,show=True)
results[0].save(filename="predicted_output.jpg")
img=cv2.imread("predicted_output.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

# from the sample output image detect the number of classes that are present in the image

boxes = results[0].boxes
class_ids = boxes.cls.tolist()
class_counts = cnt(class_ids)
print("Detected vehicle counts:", class_counts)

# Define vehicle weights

vehicle_weights = {
    0: 1.0,  # car
    1: 3.0,  # bus
    2: 3.0,  # truck
    3: 1.5,  # van
    4: 1.0,  # others
    5: 0.5,  # motorcycle
    6: 0.3,  # bicycle
    7: 0.2,  # pedestrian
    8: 1.0,  # unknown
}

# Calculate weighted load

weighted_total = 0
print("\nClass-wise weighted contribution:")
for cls_id, count in class_counts.items():
    weight = vehicle_weights.get(int(cls_id), 1.0)
    weighted_total += weight * count
    print(f"Class {int(cls_id)}: Count = {count}, Weight = {weight}, Total = {weight * count}")

print(f"\nTotal Weighted Load: {weighted_total}")

# Calculate the vehicle load

vehicle_loads = [weighted_total / 2, weighted_total / 2]
total_green_time=60

# Minimize the delay caused by the traffic

def objective(green_times):
    delay=abs(weighted_total/green_times)
    return sum(load/max(g,1) for load,g in zip(vehicle_loads,green_times))

# Ensures total green time allocated all lanes equals a fixed value

def constraint(green_times):
    return abs(sum(green_times)-total_green_time)
lb=[10,10]
ub=[50,50]

# Ensures solution is near to the 'total_green_time'

def penalized_objective(x):
    penalty=1000*constraint(x)
    return objective(x)+penalty

# Calculate the optimal green time using PSO

best_green_times,_ =pso(penalized_objective,lb,ub,swarmsize=30,maxiter=100)
print("Optimal Green Light Durations(in seconds):",best_green_times)