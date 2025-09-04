from django.db import models

# Create your models here.
class Itinerary(models.Model):
    id = models.AutoField(primary_key=True)
    destination = models.CharField(max_length=200)
    days = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    transport_type = models.CharField(max_length=100)
    preferences = models.TextField(help_text="Lista de preferências separadas por vírgula")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Itinerary to {self.destination} ({self.days} days)"


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transport(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    co2_emissions = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class TouristSpot(models.Model):
    spot_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    average_daily_cost = models.DecimalField(max_digits=10, decimal_places=2)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="spots")

    def __str__(self):
        return self.name


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, related_name="activities")
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Preference(models.Model):
    preference_id = models.AutoField(primary_key=True)
    spot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, related_name="preferences")
    preference_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.preference_type} - {self.spot.name}"