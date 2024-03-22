from rest_framework.serializers import Serializer, URLField, ListField, CharField
from pytube import YouTube
from django.conf import settings

class YoutubeVideoSerializer(Serializer):
    yt_video_url = URLField(required=True)
    available_video_resolutions = ListField(required=False)

    def validate(self, attrs):
        yt_video_url = attrs.get('yt_video_url')
        yt = YouTube(yt_video_url)
        video_streams = yt.streams.all()
        available_video_resolutions = [stream.resolution for stream in video_streams if stream.mime_type == 'video/mp4' and stream.is_progressive]
        available_video_resolutions = list(set(available_video_resolutions))
        attrs['available_video_resolutions'] = available_video_resolutions
        return super().validate(attrs)

class DownloadYoutubeVideoSerializer(Serializer):
    yt_video_url = URLField(required=True)
    resolution = CharField(required=False)
    format = CharField(required=False)

    def validate(self, attrs):
        yt_video_url = attrs.get('yt_video_url')
        resolution = attrs.get('resolution')
        format = attrs.get('format')
        if resolution == None and format == None:
            raise ValueError('Please provide resolution or format')
        
        yt = YouTube(yt_video_url)
        if resolution != None:
            video = yt.streams.filter(resolution=resolution, file_extension="mp4", progressive=True).first().download(filename=f"media/{yt.title}.mp4")
        if format == 'mp3':
            yt.streams.filter(only_audio=True).first().download(filename=f"media/{yt.title}.mp3")
        return super().validate(attrs)
