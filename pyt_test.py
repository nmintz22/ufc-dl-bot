from pytube import YouTube, Channel
from datetime import date
import logging

logging.basicConfig(
    level=logging.INFO,
    format = "{asctime} {levelname:<8} {message}",
    style = '{',
    filename = "downloads.log",
    filemode = "a"
)

channel = Channel("https://www.youtube.com/c/ufc")


url_list = []
yest = date(2022, 8, 8)
def get_url_list():
    for url in channel.video_urls:
        yt = YouTube(url)
        print(yt)
        if yt.publish_date.day == yest.day and yt.publish_date.month == yest.month and yt.publish_date.year == yest.year:
            if "promo" in yt.title.lower() or "trailer" in yt.title.lower() or "cold open" in yt.title.lower():
                url_list.append(url)
        elif yt.publish_date.day < yest.day:
            break

def download_streams(vids):
    # stream_list = yt.streams.filter(progressive=True, res="720p")
    for vid in vids:
        yt = YouTube(vid)
        stream = yt.streams.get_by_itag(22)
        #stream.download()
        logging.info(yt.title)

get_url_list()
if len(url_list) > 0:
    download_streams(url_list)
else:
    logging.info("Nothing to download")