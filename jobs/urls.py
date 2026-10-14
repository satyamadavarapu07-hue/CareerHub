from django.urls import path

from .views import (
    JobListView,
    JobDetailView,
    RegisterView,
    ApplicationListCreateView
)


urlpatterns = [

    path(
        "jobs/",
        JobListView.as_view()
    ),

    path(
        "jobs/<int:pk>/",
        JobDetailView.as_view()
    ),

    path(
        "register/",
        RegisterView.as_view()
    ),

    path(
        "applications/",
        ApplicationListCreateView.as_view()
    ),
]