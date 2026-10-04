from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import EmergencyFacility, EmergencyRequest

from math import radians, sin, cos, sqrt, atan2

# Create your views here.
def emergency_search(request):
    return render(request, "emergency/search.html")

def calculate_distance(lat1, lon1, lat2, lon2):

    """
    Calculate distance between two coordinates
    using the Haversine formula.
    Returns distance in kilometers.
    """

    earth_radius = 6371

    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius * c


def emergency_results(request):
    emergency_type = request.GET.get("type")
    location = request.GET.get("location")

    facility_type = emergency_type

    # Accident cases need medical assistance
    if emergency_type == "accident":
        facility_type = "medical"

    facilities = EmergencyFacility.objects.filter(
        facility_type = facility_type,
        is_active = True,
        emergency_service = True
    )

    processed_facilties = []

    # check whether location contains coordinates
    try:

        latitude, longitude = map(
            float, location.split(",")
        )

        for facility in facilities:
            distance = calculate_distance(
                latitude, longitude, facility.latitude, facility.longitude
            )

            facility.distance = round(distance, 2)

            processed_facilties.append(facility)

        # Nearest facility first
        processed_facilties.sort(
            key=lambda facility: facility.distance
        )

    except(ValueError, AttributeError):

        # If user entered a normal location name,
        # show facilities without distance calculation.

        processed_facilties = list(facilities)

    # First facility is the recommended one
    if processed_facilties:

        processed_facilties[0].is_recommended = True

        for facility in processed_facilties[1:]:
            facility.is_recommended = False

    context = {
        "emergency_type" : emergency_type,
        "location" : location,
        "facilities" : facilities,
    }

    return render(request, "emergency/results.html", context)

def route_view(request, facility_id):

    facility = EmergencyFacility.objects.get(
        id=facility_id
    )

    location = request.GET.get("location", "")

    latitude = None
    longitude = None

    try:
        latitude, longitude = map(
            float,
            location.split(",")
        )
    except (ValueError, AttributeError):
        pass

    EmergencyRequest.objects.create(
        user=request.user if request.user.is_authenticated else None,
        emergency_type=facility.facility_type,
        source_location=location,
        destination=facility.name,
        status="pending"
    )

    context = {
        "facility": facility,
        "location": location,
        "latitude": latitude,
        "longitude": longitude,
    }

    return render(
        request,
        "emergency/route.html",
        context
    )

@login_required(login_url="/login/")

def emergency_history(request):

    if request.user.is_authenticated:

        requests = EmergencyRequest.objects.filter(
            user=request.user
        ).order_by("-created_at")

    else:

        requests = EmergencyRequest.objects.none()

    return render(
        request,
        "emergency/history.html",
        {
            "requests": requests
        }
    )

def facilities_list(request):

    facilities = EmergencyFacility.objects.filter(
        is_active=True
    ).order_by("facility_type", "name")

    return render(
        request,
        "emergency/facilities.html",
        {
            "facilities": facilities
        }
    )


def facility_detail(request, facility_id):

    facility = EmergencyFacility.objects.get(
        id=facility_id,
        is_active=True
    )

    return render(
        request,
        "emergency/facility_detail.html",
        {
            "facility": facility
        }
    )