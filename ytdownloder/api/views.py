from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from ytdownloder.api.serializers import YoutubeVideoSerializer, DownloadYoutubeVideoSerializer

class GetYTVideoResolutionAPIView(GenericAPIView):
    serializer_class = YoutubeVideoSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)

            response = {
                'success': True,
                'message': 'Video details get successfully',
                'data': serializer.data
            }

        except Exception as e:
            response = {
                'success': False,
                'error_message': str(e),
                'message': 'Something went wrong while fetching video details.',
                'data': None
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        
        return Response(response, status=status.HTTP_200_OK)
    
class DownloadYoutubeVideoAPIView(GenericAPIView):
    serializer_class = DownloadYoutubeVideoSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            response = {
                'success': True,
                'message': 'Video downloaded successfully',
                'data': None
            }

        except Exception as e:
            response = {
                'success': False,
                'error_message': str(e),
                'message': 'Something went wrong while fetching video details.',
                'data': None
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        
        return Response(response, status=status.HTTP_200_OK)