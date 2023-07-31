import requests
from django.shortcuts import render, redirect
from .models import YouTubeData
from pytube import YouTube

def download_video(request):
    if request.method == 'POST':
        link_address = request.POST.get('link_address', '').strip()
        if link_address:
            try:
                # Use the proxy for the requests made by pytube
                proxy_url = 'http://your-proxy-url:port'  # Replace with your actual proxy URL and port
                proxies = {
                    'http': proxy_url,
                    'https': proxy_url,
                }

                # Configure pytube to use the proxy
                YouTube.request = requests.Session()
                YouTube.request.proxies = proxies

                # Download the video using pytube
                yt = YouTube(link_address)
                video_stream = yt.streams.get_highest_resolution()
                video_filename = f'Videos/{yt.title}.mp4'
                video_stream.download(output_path='Videos', filename=yt.title)

                # Save the video details to the database using the model
                file_size = video_stream.filesize
                youtube_data = YouTubeData(link=link_address, file=video_filename, file_size=file_size)
                youtube_data.save()

                print("Video downloaded and details saved to the database.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Please enter a valid YouTube video URL.")

    return redirect("home:home")
