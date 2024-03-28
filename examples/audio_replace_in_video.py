import moviepy.editor as mpe
import speech_recognition as sr

# Load the video file
video = mpe.VideoFileClip("video.mp4")

# Extract the audio from the video
audio = video.audio

# Convert the audio to text
r = sr.Recognizer()
with sr.AudioFile(audio.filename) as source:
    audio = r.record(source)
text = r.recognize_google(audio)

# Generate new audio from the text
new_audio = mpe.AudioFileClip("new_audio.mp3")

# Replace the audio in the video with the new audio
video.audio = new_audio

# Export the final video
video.write_videofile("new_video.mp4")import moviepy.editor as mpe
import speech_recognition as sr

# Load the video file
video = mpe.VideoFileClip("video.mp4")

# Extract the audio from the video
audio = video.audio

# Convert the audio to text
r = sr.Recognizer()
with sr.AudioFile(audio.filename) as source:
    audio = r.record(source)
text = r.recognize_google(audio)

# Generate new audio from the text
new_audio = mpe.AudioFileClip("new_audio.mp3")

# Replace the audio in the video with the new audio
video.audio = new_audio

# Export the final video
video.write_videofile("new_video.mp4")