import os
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip

fc=0
def split_video_into_frames(video_name, output_dir):
    global fc
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the video
    clip = VideoFileClip(video_name)

    # Calculate the number of frames to extract (one every 0.5 seconds)
    n_frames = int(clip.duration // 0.5)

    for i in range(n_frames):
        # Extract the frame
        frame = clip.get_frame(i * 0.5)

        # Save the frame as a JPEG image
        frame_path = os.path.join(output_dir, f"frame_{fc}.jpg")
        plt.imsave(frame_path, frame)
        fc+=1

# List of video names
video_names = ["yes1.mov", "yes2.mov", "yes3.mov", "yes4.mov"]

# Output directory
output_dir = "Result-Yes"

# Call the function for each video
for video_name in video_names:
    split_video_into_frames(video_name, output_dir)
