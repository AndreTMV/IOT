from django.db import models

# Create your models here.


class Sensor(models.Model):
    class tipoSensor(models.TextChoices):
        ULTRASONICO = "ultrasonico", "ULTRASONICO"
        TEMPERATURA = "temperatura", "TEMPERATURA"
        FOTORESISTOR = "fotoresistor", "FOTORESISTOR"
    tipo = models.CharField(max_length=12, choices=tipoSensor.choices)
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.tipo}"


class Reading(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.SET_NULL, null=True, related_name="readings")
    value = models.DecimalField(max_digits=12, decimal_places=4, db_index=True)
    readed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(
                fields=["sensor", "readed_at"],
                name="idx_sensor_readed_at"
            ),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["sensor", "readed_at"],
                name="uniq_sensor_read_at",
            ),
        ]
        ordering = ["-readed_at"]

    def __str__(self):
        return f"{self.sensor} @ {self.readed_at}: {self.value}"
