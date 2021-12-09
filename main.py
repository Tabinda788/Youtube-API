from youtube_statistics import YTstats

API_KEY = "your developer key"
channel_id = "your channel id"

yt = YTstats(API_KEY,channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
# yt.get_channel_video_data()