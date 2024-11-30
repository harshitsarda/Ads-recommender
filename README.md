
README for Face Extraction and Performance Score Dataset Creation
Overview
This project processes a set of videos stored in the videos directory to extract the most prominent face from each video, saves these faces as images, and creates a dataset with the average performance scores associated with the faces. The project uses a file naming convention like video_<index>_perf_<performance>.mp4 to identify and process the videos.

Output
Extracted Faces:

Saved in the faces directory.
Images are named as face_<index>.jpg.
Final Dataset:

Saved as face_avg_scores_dataset.csv.
Contains two columns:
Image: Path to the extracted face image.
Average Score: The performance score associated with the face.
Prerequisites
Python 3.8+
Required libraries:
cv2 (OpenCV)
dlib
pandas
os
re
To install the dependencies, run:

bash
Copy code
**pip install opencv-python dlib pandas**
Project Structure
Directories:
videos/: Directory containing video files in the format video_<index>_perf_<performance>.mp4.
faces/: Directory where extracted face images will be stored (auto-created).
Files:
getfaces.py: Script to extract faces and create the dataset.
grouped_results.csv: Input CSV containing video groupings and average performance scores.
face_avg_scores_dataset.csv: Output CSV with face image paths and average performance scores.
How It Works
Input Video Naming Convention
The videos must follow this format:

php
Copy code
video_<index>_perf_<performance>.mp4
Examples:

video_0_perf_0.111732.mp4
video_5_perf_1.796113.mp4
Script Workflow
Read Grouped Results:

The script reads the grouped_results.csv file, which contains information about video groupings and their average performance scores.
Find Matching Videos:

Based on the video index (e.g., 3 from video(3)), the script finds the corresponding video file in the videos directory.
Extract Prominent Face:

For each video, the most prominent face is detected using dlib.
The detected face is saved as face_<index>.jpg in the faces/ directory.
Create Dataset:

Combines the extracted face image paths with their average performance scores into face_avg_scores_dataset.csv.
**How to Run
Step 1: Prepare Files**
Place all videos in the videos/ directory.
Ensure grouped_results.csv is in the root folder and contains the following columns:
primary_video_group: Video index (e.g., video(3)).
combined_average_performance: Average performance score.
**Step 2: Run the Script
Run the Python script:**

**python getfaces.py**
**Step 3: Output**
Extracted face images will be saved in the faces/ directory.
The final dataset face_avg_scores_dataset.csv will be created with the following format:
**Image	Average Score
faces/face_0.jpg	0.111732
faces/face_5.jpg	1.796113
faces/face_9.jpg	0.284253
Example grouped_results.csv**
An example of the input grouped_results.csv:

**primary_video_group	combined_average_performance
video(0)	0.111732
video(5)	1.796113
video(9)	0.284253**
