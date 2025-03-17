import torch
from diffusers import StableDiffusionPipeline
import cv2
import numpy as np
import os
from moviepy.editor import ImageSequenceClip, AudioFileClip
import gtts

# Load Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipeline.to("cuda")  # Use GPU if available

# Function to generate frames from text prompt
def generate_frames(video_prompt, num_frames=16):
    frames = []
    filenames = []
    for i in range(num_frames):
        image = pipeline(video_prompt).images[0]
        frame_path = f"frame_{i}.png"
        image.save(frame_path)
        frames.append(cv2.imread(frame_path))  # Read as numpy array for direct use
        filenames.append(frame_path)  # Store filename
    return frames, filenames

# Function to interpolate frames for smoother video
def interpolate_frames(frames):
    output_frames = []
    
    for i in range(len(frames) - 1):
        output_frames.append(frames[i])
        for alpha in np.linspace(0, 1, num=5):
            interpolated = cv2.addWeighted(frames[i], 1 - alpha, frames[i + 1], alpha, 0)
            output_frames.append(interpolated)
    output_frames.append(frames[-1])
    
    return output_frames

# Function to create a video from frames
def create_video(frames, output_path="generated_video.mp4", fps=30):
    clip = ImageSequenceClip([cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames], fps=fps)
    clip.write_videofile(output_path, codec="libx264", audio=False)
    return output_path

# Function to generate audio from a different text prompt
def text_to_audio(audio_prompt, output_file="generated_audio.mp3"):
    tts = gtts.gTTS(audio_prompt, lang="en")
    tts.save(output_file)
    return output_file

# Function to merge audio and video
def merge_audio_video(video_path, audio_path, frames, output_path="final_video.mp4"):
    video_clip = ImageSequenceClip([cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames], fps=30)
    audio_clip = AudioFileClip(audio_path)
    
    # Set audio to video
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write final video
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Main execution
if __name__ == "__main__":
    # Separate prompts for video and audio
    video_prompt = "A futuristic AI-powered city with robots and flying cars, realistic animation"
    audio_prompt = "Welcome to the future! This AI-powered city is full of advanced robots and flying cars."

    # Generate video frames (returns both images & filenames)
    generated_frames, frame_filenames = generate_frames(video_prompt, num_frames=20)

    # Interpolate frames
    interpolated_frames = interpolate_frames(generated_frames)

    # Create video from frames
    video_path = create_video(interpolated_frames, "generated_video.mp4", fps=30)

    # Generate audio from separate text prompt
    audio_path = text_to_audio(audio_prompt, "generated_audio.mp3")

    # Merge audio and video
    merge_audio_video(video_path, audio_path, interpolated_frames, "final_video_with_audio.mp4")

    print("Final video with audio generated successfully: final_video_with_audio.mp4")

