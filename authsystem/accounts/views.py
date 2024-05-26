from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import FileResponse, Http404
from .models import AudioFile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import AudioFileSerializer
from rest_framework.response import Response


class AudioFileListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        audio_files = AudioFile.objects.all()
        data = [{'name': audio_file.name, 'file': audio_file.file.url} for audio_file in audio_files]
        return Response(data, status=status.HTTP_200_OK)


class AudioFileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, filename, format=None):
        try:
            audio_file = AudioFile.objects.get(name=filename)
        except AudioFile.DoesNotExist:
            raise Http404("File not found")

        return FileResponse(audio_file.file.open(), content_type='audio/mpeg')


class AudioFileUploadView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = AudioFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
