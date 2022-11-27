from .models import DataTS
from rest_framework import permissions, generics, parsers, status, response
from .serializers import DataTSSerializer
from django.shortcuts import render
from datetime import datetime


class ListDataTSView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated|HasAPIKey]
    permission_classes = [permissions.AllowAny]

    queryset = DataTS.objects.all()
    serializer_class = DataTSSerializer


class CreateDataTSView(generics.CreateAPIView):
    serializer_class = DataTSSerializer

    parser_classes = (parsers.JSONParser,)
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
def index(request):
    labels = []
    data = []
    u= DataTS.objects.order_by('timestamp').reverse()[:10]
    queryset = [u[9],u[8],u[7],u[6],u[5],u[4],u[3],u[2],u[1],u[0]]
    for i in queryset:
        labels.append(str(datetime.fromisoformat(str(i.timestamp))).split('.')[0])
        data.append(i.value)
    return render(request, 'index.html', 
        {'labels': labels,
        'data': data}
    )
def reportes(request):
    datats = []
    queryset = DataTS.objects.order_by('timestamp')
    for item in queryset:
        datats.append(dict(tag=item.tag,device=item.device.name, value=item.value, timestamp=item.timestamp, location=item.device.location))
    return render(request, 'reportes.html', {'datats':datats})