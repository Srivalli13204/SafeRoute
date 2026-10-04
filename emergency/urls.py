from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.emergency_search,
        name="emergency_search"
    ),

    path(
        "results/",
        views.emergency_results,
        name="emergency_results"
    ),

    path(
        "route/<int:facility_id>/",
        views.route_view,
        name="route_view"
    ),

    path(
        "history/",
        views.emergency_history,
        name="emergency_history"
    ),

    path(
        "facilities/",
        views.facilities_list,
        name="facilities"
    ),

    path(
        "facilities/<int:facility_id>/",
        views.facility_detail,
        name="facility_detail"
    ),
]