# views.py
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import IncidentReportForm
from .models import IncidentImage, IncidentReport


def incident_list(request):
    """Display list of all incident reports"""
    incidents = IncidentReport.objects.all().order_by("-date_time_incident")
    return render(request, "incidents/incident_list.html", {"incidents": incidents})


def create_incident_report(request):
    if request.method == "POST":
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            incident = form.save()
            return redirect("incident_detail", pk=incident.pk)  # ← Go to detail view
    else:
        form = IncidentReportForm()
    return render(request, "incidents/incident_create.html", {"form": form})


def incident_detail(request, pk):
    """View/manage existing incident including images"""
    incident = get_object_or_404(IncidentReport, pk=pk)
    return render(request, "incidents/incident_detail.html", {"incident": incident})


@require_POST
def upload_incident_image(request, incident_id):
    incident = get_object_or_404(IncidentReport, pk=incident_id)

    if "image" in request.FILES:
        image = IncidentImage.objects.create(
            incident_report=incident,
            image=request.FILES["image"],
            caption=request.POST.get("caption", ""),
        )
        # Return the new image HTML
        return render(
            request, "incidents/partials/incident_image_item.html", {"image": image}
        )

    return HttpResponse("Error uploading image", status=400)


@require_POST
def delete_incident_image(request, image_id):
    image = get_object_or_404(IncidentImage, pk=image_id)
    image.delete()
    return HttpResponse("")  # Empty response removes the element


def get_image_upload_form(request):
    """Return empty upload form for adding more images"""
    return render(request, "incidents/partials/image_upload_form.html")
