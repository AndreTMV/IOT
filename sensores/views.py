from django.shortcuts import render
from rest_framework import views, viewsets
from .serializer import SensorSerializer, ReadingSerializer
from .models import Sensor, Reading
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


class SensorView(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class ReadingView(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()


@api_view(['GET'])
def sensor_readings(request):
    sensor = request.query_params.get('sensor')
    if sensor:
        try:
            readings = Reading.objects.filter(sensor=sensor)

            serialized_readings = ReadingSerializer(readings, many=True).data
            return Response({
                "lectures": serialized_readings,
            })
        except:
            return Response({'status': 'Error al obtener los datos.'}, status=500)
    else:
        return Response
