
import cv2
import numpy as np
import os

def iou(box1, box2):
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])
    
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    
    box1Area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2Area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)
    
    iou = interArea / float(box1Area + box2Area - interArea)
    
    return iou

def merge_boxes_and_crop(image, boxes, classes, iou_threshold=0.5, output_folder="output"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    final_boxes = []
    
    for i in range(len(boxes)):
        keep = True
        for j in range(i + 1, len(boxes)):
            if iou(boxes[i], boxes[j]) > iou_threshold:
                if classes[i] == 1 and classes[j] == 0:
                    # Keep class 1, discard class 0
                    keep = True
                elif classes[i] == 0 and classes[j] == 1:
                    # Discard class 0, as class 1 overlaps
                    keep = False
        if keep:
            final_boxes.append(boxes[i])
    
    for idx, box in enumerate(final_boxes):
        x1, y1, x2, y2 = box
        cropped_img = image[y1:y2, x1:x2]
        cv2.imwrite(os.path.join(output_folder, f"crop_{idx}.png"), cropped_img)
    
    return final_boxes

# Example usage:

# Load your image
image_path = "path_to_your_image.png"
image = cv2.imread(image_path)

# Example bounding boxes and corresponding classes
# Boxes are in format [x1, y1, x2, y2]
boxes = [
    [10, 20, 100, 200],  # Example box 1
    [15, 25, 110, 210],  # Overlapping box 2
    [300, 400, 400, 500],  # Non-overlapping box 3
    [305, 405, 395, 495]   # Overlapping box 4
]
classes = [0, 1, 0, 1]  # Corresponding classes for boxes

# Merge boxes and crop images
merged_boxes = merge_boxes_and_crop(image, boxes, classes, iou_threshold=0.5, output_folder="output")

print("Final bounding boxes after merging:", merged_boxes)
