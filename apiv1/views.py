from .models import DataTS
from rest_framework import permissions, generics, parsers, status, response
from .serializers import DataTSSerializer


class ListDataTSView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated|HasAPIKey]
    permission_classes = [permissions.AllowAny]

    queryset = DataTS.objects.all()
    serializer_class = DataTSSerializer


class CreateDataTSView(generics.CreateAPIView):
    serializer_class = DataTSSerializer

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            status=status.HTTP_201_CREATED,
            headers=headers
        )