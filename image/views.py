# Create your views here.

from rest_framework.generics import CreateAPIView
from rest_framework import parsers

from .models import Image
from .serializers import ImageSerializer


class ImageView(CreateAPIView):
    model = Image
    serializer_class = ImageSerializer
    parser_classes = (parsers.MultiPartParser,)

def image_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ImageObjects = Image.objects.all()
        serializer = ImageSerializer(ImageObjects, many=True)
        return JSONResponse(serializer.data)