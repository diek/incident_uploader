from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Location(models.Model):
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.location


class Shift(models.Model):
    shift = models.CharField(max_length=255, blank=True)
    employee = models.ForeignKey(User, models.PROTECT, related_name="employees")
    location = models.ForeignKey(
        Location, models.PROTECT, related_name="incident_locations"
    )

    def __str__(self):
        return self.shift

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["shift", "location"], name="unique_shift_location"
            )
        ]


class IncidentReport(models.Model):
    shift = models.ForeignKey(Shift, models.PROTECT, related_name="incident_reports")
    date_time_incident = models.DateTimeField(db_index=True)
    summary = models.TextField()
    merchandise_cost = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    is_multiple_person = models.BooleanField("Multiple People", default=False)
    number_persons = models.SmallIntegerField("Number Persons Involved", default=1)
    merchandise_description = models.TextField(blank=True)
    is_theft = models.BooleanField("Theft", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shift.location}: {self.date_time_incident}"


class IncidentImage(models.Model):
    incident_report = models.ForeignKey(
        IncidentReport, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="incident_reports/%Y/%m/%d/")
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)  # For ordering images

    class Meta:
        ordering = ["order", "uploaded_at"]

    def __str__(self):
        return f"Image for {self.incident_report.id}"
