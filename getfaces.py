import cv2
import os
import pandas as pd
import dlib
import re

# Paths
videos_folder = "videos"  # Directory containing videos
faces_folder = "faces"  # Directory to save extracted face images
grouped_results_csv = "grouped_results.csv"  # CSV with grouped results
output_dataset_csv = "face_avg_scores_dataset.csv"  # Final dataset

# Ensure faces folder exists
os.makedirs(faces_folder, exist_ok=True)

# Initialize face detector
detector = dlib.get_frontal_face_detector()

# Function to extract and save prominent face from a video
def extract_prominent_face(video_path, save_path):
    cap = cv2.VideoCapture(video_path)
    face_detected = False
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        if len(faces) > 0:
            # Use the first detected face (most prominent)
            x, y, w, h = (faces[0].left(), faces[0].top(), faces[0].width(), faces[0].height())
            face = frame[y:y+h, x:x+w]
            # Save the face image
            cv2.imwrite(save_path, cv2.resize(face, (224, 224)))
            face_detected = True
            break
    cap.release()
    return face_detected

# Read grouped results
grouped_results = pd.read_csv(grouped_results_csv)

# Process each video and extract its prominent face
face_data = []
for index, row in grouped_results.iterrows():
    primary_video = row["primary_video_group"]  # Example: video(3)
    avg_score = row["combined_average_performance"]
    
    # Extract video index (e.g., "3" from "video(3)")
    video_index = primary_video.replace("video(", "").replace(")", "")
    
    # Find the video file matching this index
    video_filename = None
    for file in os.listdir(videos_folder):
        if re.match(rf"video_{video_index}_perf_.*\.mp4", file):
            video_filename = file
            break
    
    if not video_filename:
        print(f"No matching video found for index {video_index}")
        continue
    
    video_path = os.path.join(videos_folder, video_filename)
    face_image_path = os.path.join(faces_folder, f"face_{video_index}.jpg")
    
    # Extract face and save image
    if extract_prominent_face(video_path, face_image_path):
        face_data.append({"image": face_image_path, "average_score": avg_score})
    else:
        print(f"No face detected in video {video_filename}")

# Create the new dataset
face_dataset = pd.DataFrame(face_data)

# Save the dataset to a CSV
face_dataset.to_csv(output_dataset_csv, index=False)

print(f"Dataset created: {output_dataset_csv}")
