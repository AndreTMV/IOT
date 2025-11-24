from django.shortcuts import render
import json
from rest_framework import views, viewsets
from .serializer import SensorSerializer, ReadingSerializer
from .models import Sensor, Reading
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import timedelta

from django.utils import timezone
from django.views.generic import TemplateView
from django.db.models import Avg, Max, Min, Count
from django.db.models.functions import TruncDay

# Create your views here.


class SensorView(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class ReadingView(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()


@api_view(['GET'])
def sensor_readings(request):
    sensor_id = request.query_params.get('sensor')
    if sensor_id:
        try:
            readings = Reading.objects.filter(
                sensor_id=sensor_id).order_by('-readed_at')
            serialized_readings = ReadingSerializer(readings, many=True).data
            return Response({"lectures": serialized_readings})
        except Exception as e:
            return Response(
                {'status': f'Error al obtener los datos: {e}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return Response(
            {'status': 'Debes enviar el parámetro ?sensor=<id>'},
            status=status.HTTP_400_BAD_REQUEST
        )


class SensorsDashboardView(TemplateView):
    template_name = "sensores/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = timezone.now()
        last_24h = now - timedelta(hours=24)
        last_7d = now - timedelta(days=7)

        total_sensors = Sensor.objects.count()
        total_readings = Reading.objects.count()
        last_reading = Reading.objects.order_by("-readed_at").first()

        context["overall"] = {
            "total_sensors": total_sensors,
            "total_readings": total_readings,
            "last_reading_at": last_reading.readed_at if last_reading else None,
        }

        per_sensor_24h = (
            Reading.objects.filter(readed_at__gte=last_24h)
            .values("sensor_id", "sensor__name", "sensor__tipo")
            .annotate(
                avg_value=Avg("value"),
                min_value=Min("value"),
                max_value=Max("value"),
                count=Count("id"),
                last_read_at=Max("readed_at"),
            )
            .order_by("sensor__name")
        )
        context["per_sensor_24h"] = per_sensor_24h

        series_7d = (
            Reading.objects.filter(readed_at__gte=last_7d)
            .annotate(day=TruncDay("readed_at"))
            .values("day", "sensor__tipo")
            .annotate(avg_value=Avg("value"))
            .order_by("day", "sensor__tipo")
        )

        series_7d_list = [
            {
                "day": row["day"].strftime("%Y-%m-%d"),
                "tipo": row["sensor__tipo"],
                "avg": float(row["avg_value"]) if row["avg_value"] is not None else None,
            }
            for row in series_7d
        ]

        context["series_7d_json"] = json.dumps(series_7d_list)

        return context
