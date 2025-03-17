AI-Powered Text-to-Video Generation

📌 Overview
This project generates AI-powered videos from text prompts using Stable Diffusion and MoviePy. It creates a sequence of images based on a given prompt, interpolates frames for smooth transitions, and compiles them into a video. Additionally, it supports text-to-audio conversion to generate voiceovers for the videos.


🚀 Technologies Used
•	Python (Primary language)
•	Stable Diffusion (Image generation)
•	OpenCV (Frame processing)
•	NumPy (Mathematical operations)
•	MoviePy (Video creation)
•	gTTS (Google Text-to-Speech) (Audio generation)
•	CUDA (For GPU acceleration, if available)
🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Text-to-Video.git
cd AI-Text-to-Video
2️⃣ Install Dependencies
pip install torch diffusers opencv-python numpy moviepy gtts
3️⃣ Download the Stable Diffusion Model
from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipeline.to("cuda")  # Use GPU if available
🎥 How It Works
1️⃣ Image Generation
•	The model generates multiple images based on the given text prompt.
•	These images serve as frames for the video.
2️⃣ Frame Interpolation
•	OpenCV is used to smooth the transition between frames.
•	Interpolation helps in creating a more natural animation.
3️⃣ Video Compilation
•	MoviePy compiles the interpolated frames into an MP4 video.
4️⃣ Audio Generation
•	gTTS generates speech from the text prompt.
•	The generated audio is merged with the video.
🎬 Usage
Run the script with your custom text prompt:
python generate_video.py
Modify the prompt inside the script:
text_prompt = "How Artificial Intelligence works"

🔥 Features
✅ AI-generated videos from text prompts
✅ Smooth frame transitions
✅ Automatic voiceover generation
✅ GPU acceleration support
📌 Future Enhancements
•	Use advanced text-to-video models for more realistic animations.
•	Implement real-time rendering with video diffusion models.
•	Allow custom voice selection for text-to-speech.
•	Integrate a user-friendly web interface.
________________________________________
📌 Contributor: Manasa 
📌 License: MIT
📌 GitHub Repository: AI-Text-to-Video

