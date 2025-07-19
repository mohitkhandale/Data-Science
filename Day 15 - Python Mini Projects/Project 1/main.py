import os 
from moviepy import VideoFileClip

def get_total_video_duration(folder_path):
    total_duration = 0.0
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4','.mkv','.avi')):
            video_path = os.path.join(folder_path, filename)
            try:
                video = VideoFileClip(video_path)
                total_duration += video.duration
                video.close()
            except Exception as e:
                print(f"Could not process video: {filename}")
            
    hours = int(total_duration // 3600)
    minutes = int((total_duration % 3600)//60)
    seconds = int(total_duration % 60)
    
    return f"Total Duration: {hours} hours, {minutes} minutes, {seconds} seconds"
                
folder_paths = 'D:\Movies\Gotham.S02.1080p.10Bit.BluRay.AAC5.1.HEVC.English.Esubs.MoviesVerse.Me'
print(get_total_video_duration(folder_paths))