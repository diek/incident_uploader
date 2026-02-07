# forms.py
from django import forms

from .models import IncidentReport


class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = [
            "shift",
            "date_time_incident",
            "summary",
            "merchandise_cost",
            "is_multiple_person",
            "number_persons",
            "merchandise_description",
            "is_theft",
        ]
        widgets = {
            "date_time_incident": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "datetime-input"},
                format="%Y-%m-%dT%H:%M",
            ),
            "summary": forms.Textarea(
                attrs={"rows": 5, "placeholder": "Describe the incident in detail..."}
            ),
            "merchandise_description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Describe the merchandise involved..."}
            ),
            "merchandise_cost": forms.NumberInput(
                attrs={"step": "0.01", "min": "0", "placeholder": "0.00"}
            ),
            "number_persons": forms.NumberInput(attrs={"min": "1", "max": "99"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the input format for datetime field
        self.fields["date_time_incident"].input_formats = ["%Y-%m-%dT%H:%M"]
