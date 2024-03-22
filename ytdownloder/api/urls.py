from django.urls import path
from ytdownloder.api.views import GetYTVideoResolutionAPIView, DownloadYoutubeVideoAPIView

urlpatterns = [
    path('get-video-resolutions', GetYTVideoResolutionAPIView.as_view(), name='get-video-resolutions'),
    path('download-yt-video', DownloadYoutubeVideoAPIView.as_view(), name='download-yt-video')
]
