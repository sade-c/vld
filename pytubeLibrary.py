#pip install pytube


# named as pytube.py , then error
# The circular import error happens because you named your script pytube.py.
# Python prioritises modules in the working directory so you are trying to import your script pytube recursively.

#  Search for youtube videos related to a topic
#  Search all the videos related to a channel and playlist
#  Open the video to play (video by video)
#  Download a Youtube video
#  Download the Youtube Video's audio. -check whether we can do it.
#  Download the Youtube Video's subtitle.
from moviepy.editor import *  

def download_video(url):
    import pytube
    from pytube import Playlist,YouTube

    try :
        yt = YouTube(url) # or can use a youtube object directly.
    except pytube.exceptions.VideoUnavailable:
        print("Video Unavailable")
    else:
        stream  = yt.streams 
        #.get_by_itag(134) # Itag is a youtube is a static youtube video format
        #youtube format identifier code = 134 means mp4 in 360p resolution
        # print("Size: "+str(stream.filesize))
        vid = stream.filter(progressive=True,res = "360p", file_extension = "mp4").first()
        print("Size: "+str(round(vid.filesize/2**20,2))+" MB")
        filepath = vid.download()
        print("Saved in: "+ filepath)
    return filepath

# download_video("https://youtu.be/JqyIzFXm9vk")

def download_audio_track(url):
    from pytube import YouTube
    import os
    yt = YouTube(url) # or can use a youtube object directly.
    stream  = yt.streams.filter(only_audio=True ).first()
    # print("Size: "+str(round(vid.filesize/2**20,2))+" MB")
    filepath = stream.download()

    # Pytube does not support "mp3" format but you can download audio in webm format
    # so use os module for conversion
    base, ext = os.path.splitext(filepath)
    audio_file = base + '.mp3'
    os.rename(filepath, audio_file)
    print("Saved in: "+ audio_file)

# download_audio_track("https://youtu.be/JqyIzFXm9vk")

#  ...........................................................
#  Check error in download_captions(url):
#  Solution : https://stackoverflow.com/questions/68780808/xml-to-srt-conversion-not-working-after-installing-pytube #change caption.py sourcecode file
def download_captions(url):
    from pytube import YouTube
    yt = YouTube(url)
    print("All Avaible Captions : \n",yt.captions)
    en_caption_data = yt.captions['a.en']
    print("\nCaption Data in SRT Format: \n")
    srt_format = en_caption_data.xml_caption_to_srt(en_caption_data.xml_captions)
    print(srt_format)

 # ............................................................

def download_from_playlist(url_playlist):
    from pytube import Playlist,YouTube
    playlist = Playlist(url_playlist)
    print("Playlist Title: "+playlist.title+"\n")

    video_urls = playlist.video_urls

    for i in range(len(playlist.videos)):
        video = playlist.videos[i]
        print("Title: "+video.title)
        print("URL: "+video_urls[i])
        # download_video(video.watch_url)
        # download_audio_track(video.watch_url)
        print()

def download_from_playlist_mp3(url_playlist):
    
    from pytube import Playlist,YouTube
    
    import os # importing os module
    playlist = Playlist(url_playlist)
    print("Playlist Title: "+playlist.title+"\n")

    video_urls = playlist.video_urls

    for i in range(len(playlist.videos)):
        video = playlist.videos[i]
        print("Title: "+video.title)
        print("URL: "+video_urls[i])
        str= download_video(video.watch_url)
        
        video = VideoFileClip(os.path.join(os.getcwd(),f'{str}')) # Getting mp4 file.
        video.audio.write_audiofile(os.path.join(os.getcwd(),f"{str}_converted.mp3")) # Converting mp4 file to mp3.
        print()

# download_from_playlist("https://youtube.com/playlist?list=PLEw03wP6R0QCwyRl4yGHgowPzG9VIYD0q")

def download_from_channel(url_channel):
    from pytube import Channel,YouTube
    channel = Channel(url_channel)
    print("Channel Name: "+channel.channel_name+"\n")

    video_urls = channel.video_urls

    for i in range(len(channel.videos)):
        video = channel.videos[i]
        print("Title: "+video.title)
        print("URL: "+video_urls[i])
        # download_video(video.watch_url)
        # download_audio_track(video.watch_url)
        print()

# download_from_channel("https://www.youtube.com/channel/UC23wTY7YzLCla5Qg3IWauMw")


