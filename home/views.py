from django.shortcuts import render, redirect
from pytube import YouTube

from home.models import YouTubeData


def home(request):
    return render(request, template_name="home/index.html")


def download_video(request):
    if request.method == 'POST':
        link_address = request.POST.get('link_address', '').strip()
        if link_address:
            try:

                yt = YouTube(link_address)
                video_stream = yt.streams.get_highest_resolution()
                video_filename = f'Videos/{yt.title}.mp4'
                video_stream.download(output_path='Videos', filename=yt.title)

                file_size = video_stream.filesize
                youtube_data = YouTubeData(link=link_address, file=video_filename, file_size=file_size)
                youtube_data.save()

                print("Video downloaded and details saved to the database.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Please enter a valid YouTube video URL.")

    return redirect("home:home")
