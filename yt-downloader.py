import yt_dlp
opt = {
    'format': 'best',  # Downloads the best quality available
    'outtmpl': '%(title)s.%(ext)s',  # Save file as the video title with extension
    'noplaylist': True  # Ensures only a single video is downloaded if the link is a playlist
}

def downloading(video_link):
    with yt_dlp.YoutubeDL(opt) as ydl:
        ydl.download([video_link])

channel = 1
while channel == 1:
    link = input("Enter Link:")
    x = link.strip()

    downloading(x)
    channel = int(input('Enter 1 for more , 0 for ending:'))
