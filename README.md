# Youtube-Video-Downloader

This script allows you to download YouTube videos in the best quality using the **`yt_dlp`** library. It provides a simple interface where you can input a video link, and the script will download the video for you. Additionally, it lets you continue downloading multiple videos in a single session.

---

## Features:
1. **Download Best Quality**: The script fetches and downloads the best available quality of the video.
2. **Custom File Naming**: Videos are saved using their title as the filename.
3. **Single Video Mode**: Ensures only one video is downloaded even if the link is part of a playlist.
4. **Interactive Input**: Lets you input links one at a time, with an option to continue downloading or exit.

---

## How to Use:
1. **Install `yt_dlp`**:
   Make sure `yt_dlp` is installed in your environment. Use the following command if it's not already installed:
   ```bash
   pip install yt-dlp
   ```

2. **Run the Script**:
   Execute the script in your Python environment.

3. **Input a Video Link**:
   - When prompted, enter the YouTube video URL you want to download.
   - Example:
     ```
     Enter Link: https://www.youtube.com/watch?v=exampleID
     ```

4. **Choose to Continue or Exit**:
   - After each download, the script asks:
     ```
     Enter 1 for more , 0 for ending:
     ```
     - Enter `1` to download another video.
     - Enter `0` to exit the script.

---

## Code Explanation:
### **1. Options for `yt_dlp`**
```python
opt = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True
}
```
- **`format: 'best'`**: Ensures the highest available video quality is downloaded.
- **`outtmpl: '%(title)s.%(ext)s'`**: Saves the video with its title as the filename and appropriate file extension.
- **`noplaylist: True`**: Downloads only the single video provided in the link.

### **2. `downloading(video_link)` Function**
This function handles the downloading process using `yt_dlp`. It:
- Accepts a YouTube video link as input.
- Initializes a `YoutubeDL` instance with the specified options.
- Downloads the video.

### **3. Loop for Multiple Downloads**
```python
channel = 1
while channel == 1:
    link = input("Enter Link:")
    x = link.strip()

    downloading(x)
    channel = int(input('Enter 1 for more , 0 for ending:'))
```
- Prompts the user to enter a video link.
- Cleans up the input using `.strip()`.
- Calls the `downloading` function to download the video.
- Asks the user whether to continue or exit:
  - `1` to enter another link.
  - `0` to stop the program.

---

## Example Usage:
1. User runs the script and enters a link:
   ```
   Enter Link: https://www.youtube.com/watch?v=exampleID
   ```
   The script downloads the video titled `exampleID` in the best quality available.

2. After the download:
   ```
   Enter 1 for more , 0 for ending:
   ```
   - If the user enters `1`, they can provide another link.
   - If the user enters `0`, the program exits.

---

## Notes:
1. Make sure you have an active internet connection to download videos.
2. The downloaded video is saved in the same directory as the script unless specified otherwise in the `outtmpl` path.
3. YouTube's terms of service may restrict downloading videos without proper permissions. Use this tool responsibly.

---

Enjoy your video downloading! 🎥
