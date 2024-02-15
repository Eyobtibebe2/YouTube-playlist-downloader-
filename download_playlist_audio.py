from pytube import Playlist, YouTube
import re 

def download_audio_playlist(url, save_path):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    
    print(f"Downloading audio from {len(playlist.video_urls)} videos in the playlist...")
    
    for video_url in playlist.video_urls:
        video = YouTube(video_url)
        print(f"Downloading audio from: {video.title}...")
        audio_stream = video.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=save_path)
        print(f"Audio from {video.title} downloaded successfully!")
        
    print("Audio download from playlist completed.")

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    save_path = input("Enter the directory to save the audio files: ")
    
    download_audio_playlist(playlist_url, save_path)
