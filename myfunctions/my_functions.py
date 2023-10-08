import os
import shutil
from datetime import datetime
from pytube import YouTube
from moviepy.editor import VideoFileClip
import whisper
import glob
import yt_dlp




def get_video_info(url):
    video = YouTube(url)

    video_info = {
    "title": video.title,
    "length": video.length,
    "thumbnail_url": video.thumbnail_url,
    "description": video.description,
    "views": video.views,
    "rating": video.rating,
    "age_restricted": video.age_restricted,
    "video_id": video.video_id,
    "author": video.author,
    "publish_date": video.publish_date,
    "captions": video.captions,
    "keywords": video.keywords,
    #"video_streams": video.streams,
    #"audio_streams": video.streams.filter(only_audio=True),
    #"video_tags": video.video_tags,
    #"length_seconds": video.length_seconds,
    #"average_rating": video.average_rating,
    #"is_closed_captioned": video.is_closed_captioned,
    "channel_url": video.channel_url,
    "channel_id": video.channel_id,
    #"channel_subscribers": video.channel_subscribers,
    #"related_videos": video.related_videos,
    #"captions_available": video.captions_available,
    #"thumbnail_resolution": video.thumbnail_resolution,
    #"captions_tracks": video.captions_tracks,

}


    return video_info

def current_directory(n):
    # Get the current directory
    current_directory = os.getcwd()
    # Get a list of all directories in the current directory
    directories = [name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))]
    # Filter directories that start with "My_Folder_"
    matching_directories = [name for name in directories if name.startswith("Folder_")]

    # Check if there are more than n matching directories
    if len(matching_directories) > n:
        # Remove the matching directories
        for directory in matching_directories:
            directory_path = os.path.join(current_directory, directory)
            shutil.rmtree(directory_path)
            print(f"Removed directory: {directory_path}")
    else:
        print("There are not enough matching directories to remove.")




def create_folder_and_directories():
    # Get the current date and time
    now = datetime.now()

    # Create a new folder with the current hour
    current_folder = f"Folder_{now.strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(current_folder)

    # Create the subdirectories within the current folder
    mp4_directory = os.path.join(current_folder, 'media', 'mp4')
    mp3_directory = os.path.join(current_folder, 'media', 'mp3')
    txt_directory = os.path.join(current_folder, 'media', 'txt')

    # Create the subdirectories
    os.makedirs(mp4_directory)
    os.makedirs(mp3_directory)
    os.makedirs(txt_directory)
    return mp4_directory, mp3_directory, txt_directory



def download_youtube(video_url, mp4_directory):
    # Create a YouTube object
    yt = YouTube(video_url)
    # Get the lowest resolution video stream
    stream = yt.streams.get_lowest_resolution()
    # Download the video
    stream.download(mp4_directory)  
    return "mp4"



# https://gist.github.com/space-pope/977b0d15cf01932332014194fc80c1f0
def download_youtube1(video_url, download_path):

  opts = {
    "external_downloader": "ffmpeg",
    #"external_downloader_args": ffmpeg_args,
    # though not required, I'm including the subtitles options here for a reason; see below
    "writesubtitles": False,
    "writeautomaticsub": False,
    # to suppress ffmpeg's stdout output
    "quiet": True,
    "outtmpl": download_path + "/%(title)s.%(ext)s"
  }

  with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download(video_url)
    info = ydl.extract_info(video_url, download=False)
    duration = info.get("duration")
    return "webm",duration
  
def download_youtube2(video_url, download_path):
    opts = {
        "external_downloader": "ffmpeg",
        #"external_downloader_args": ffmpeg_args,
        # though not required, I'm including the subtitles options here for a reason; see below
        "writesubtitles": False,
        "writeautomaticsub": False,
        # to suppress ffmpeg's stdout output
        "quiet": True,
        "outtmpl": download_path + "/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download(video_url)
        info = ydl.extract_info(video_url, download=False)
        duration = info.get("duration")
        return duration




def rename_videos(mp4_directory):
    # Get a list of all files in the directory
    files = os.listdir(mp4_directory)

    if len(files) > 1:
        # Iterate over each file and rename it
        for i, filename in enumerate(files, start=1):
            # Construct the current file path
            current_path = os.path.join(mp4_directory, filename)

            # Split the current filename and extension
            name, extension = os.path.splitext(filename)

            # Construct the new filename with numbering
            new_name = f"video_{i}{extension}"

            # Construct the new file path
            new_path = os.path.join(mp4_directory, new_name)

            # Rename the file
            os.rename(current_path, new_path)
    elif len(files) == 1:
        # Rename the single file as "video"
        filename = files[0]
        current_path = os.path.join(mp4_directory, filename)
        new_name = "video" + os.path.splitext(filename)[1]
        new_path = os.path.join(mp4_directory, new_name)
        os.rename(current_path, new_path)
    else:
        # No files in the directory
        print("No files found in the directory.")


def mp4_to_mp3(mp4_directory, video_extension, mp3_directory):
     # Load the video file
    video = VideoFileClip(f"{mp4_directory}/video.{video_extension}")

    # Extract the audio from the video file
    audio = video.audio

    # Save the audio as an MP3 file
    audio.write_audiofile(f"{mp3_directory}/my_audio.mp3", codec='mp3')

    # Close the video and audio files
    video.close()
    audio.close()




def transcribe_mp3(mp3_directory, name):
    model = whisper.load_model("tiny")
    result = model.transcribe(f"{mp3_directory}/{name}.mp3")
    return result


def with_opencv(filename):
    # video = cv2.VideoCapture(filename)
    # # count the number of frames
    # frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # fps = video.get(cv2.CAP_PROP_FPS)
    
    # # calculate duration of the video
    # seconds = round(frames / fps)
    # video_time = timedelta(seconds=seconds).total_seconds()
      
    video = VideoFileClip(filename)
    video_time = video.duration
    return video_time






def concatenate_txt_files(directory):
    # Get a list of all text files in the directory
    txt_files = glob.glob(os.path.join(directory, "*.txt"))

    # Concatenate the contents of all text files
    concatenated_text = ""
    for txt_file in txt_files:
        with open(txt_file, "r") as file:
            text = file.read()
            concatenated_text += text

    return concatenated_text
