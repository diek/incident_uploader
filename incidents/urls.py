from django.urls import path

from .views import (
    create_incident_report,
    delete_incident_image,
    incident_detail,
    incident_list,
    upload_incident_image,
)

urlpatterns = [
    path("incidents/", incident_list, name="incident_list"),
    path("incident/create/", create_incident_report, name="create_incident_report"),
    path("incident/<int:pk>/", incident_detail, name="incident_detail"),
    path(
        "incident/<int:incident_id>/upload-image/",
        upload_incident_image,
        name="upload_incident_image",
    ),
    path(
        "incident/image/<int:image_id>/delete/",
        delete_incident_image,
        name="delete_incident_image",
    ),
]
