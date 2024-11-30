# Ads-recommender
Video Embedding and Similarity Analysis
This project processes videos to extract facial embeddings, computes similarity scores between embeddings, and analyzes their performance scores to identify clusters of related videos based on similarity.

Table of Contents
Overview
Requirements
Workflow
Step 1: Download Videos
Step 2: Extract Embeddings
Step 3: Compute Similarity Scores
Step 4: Group Similar Videos
Outputs
How to Run
Future Enhancements
Overview
This project automates the process of:

Downloading videos from a dataset.
Detecting faces in each video and extracting their embeddings.
Comparing embeddings to compute cosine similarity scores.
Aggregating similar videos into groups and calculating their average performance scores.
Requirements
Install the required Python libraries:

bash
Copy code
pip install pandas numpy opencv-python-headless dlib requests sklearn
You will also need a dataset in CSV format containing video URLs and performance scores, with columns:

Performance
Video URL
Workflow
Step 1: Download Videos
Videos are downloaded from a dataset containing URLs. Each video is saved with a filename derived from its row index and performance score.

Script: download_videos.py

Input: CSV file with Performance and Video URL.

Output: Videos saved in the videos/ directory.

Step 2: Extract Embeddings
The embeddings are generated for the most prominent face detected in each video.

Script: generate_embeddings.py

Input: Videos in the videos/ directory.

Output: .npy files (embeddings) saved in the embeddings/ directory.

Step 3: Compute Similarity Scores
Cosine similarity is calculated between all pairs of embeddings. Pairs with a similarity score above a defined threshold (e.g., 95%) are stored, along with the average performance score of the videos in the pair.

Script: compute_similarity.py

Input: Embeddings from the embeddings/ directory.

Output: similar_pairs_with_avg_performance.csv

Step 4: Group Similar Videos
Videos sharing a common reference (e.g., video(3)) are grouped into clusters. For each group:

All associated video pairs are combined into a single row.
The average performance score of the group is calculated.
Script: group_results.py

Input: similar_pairs_with_avg_performance.csv.

Output: grouped_results.csv.

Outputs
videos/: Directory containing the downloaded videos.
embeddings/: Directory containing .npy files for each video embedding.
similar_pairs_with_avg_performance.csv: File containing pairs of videos with similarity scores above the threshold.
grouped_results.csv: File containing grouped video clusters and their average performance scores.
How to Run
Download Videos:
bash
Copy code
python download_videos.py
Generate Embeddings:
bash
Copy code
python generate_embeddings.py
Compute Similarity Scores:
bash
Copy code
python compute_similarity.py
Group Similar Videos:
bash
Copy code
python group_results.py
Future Enhancements
Advanced Face Detection: Integrate advanced models for multi-face detection in videos.
Dynamic Thresholding: Use dynamic thresholds based on dataset statistics for similarity score computation.
Visualization: Add visualizations for clusters of similar videos.
Performance Analysis: Extend analysis with more sophisticated metrics.
