from django.core.management.base import BaseCommand
from emergency.models import EmergencyFacility


FACILITIES = [

    # =========================
    # BANGALORE - MEDICAL
    # =========================

    {
        "name": "Apollo Hospital Bangalore",
        "facility_type": "medical",
        "address": "Bannerghatta Road, Bangalore",
        "latitude": 12.8956,
        "longitude": 77.5996,
        "contact": "08026304050",
    },

    {
        "name": "Manipal Hospital Old Airport Road",
        "facility_type": "medical",
        "address": "Old Airport Road, Bangalore",
        "latitude": 12.9591,
        "longitude": 77.6470,
        "contact": "08025024444",
    },

    {
        "name": "Narayana Health City",
        "facility_type": "medical",
        "address": "Bommasandra, Bangalore",
        "latitude": 12.8008,
        "longitude": 77.6848,
        "contact": "08071222222",
    },

    {
        "name": "Fortis Hospital Bannerghatta Road",
        "facility_type": "medical",
        "address": "Bannerghatta Road, Bangalore",
        "latitude": 12.8944,
        "longitude": 77.5970,
        "contact": "08066214444",
    },

    {
        "name": "Columbia Asia Hospital Hebbal",
        "facility_type": "medical",
        "address": "Hebbal, Bangalore",
        "latitude": 13.0358,
        "longitude": 77.5970,
        "contact": "08039898960",
    },

    {
        "name": "St. John's Medical College Hospital",
        "facility_type": "medical",
        "address": "Koramangala, Bangalore",
        "latitude": 12.9298,
        "longitude": 77.6197,
        "contact": "08049467000",
    },

    {
        "name": "Victoria Hospital",
        "facility_type": "medical",
        "address": "K R Road, Bangalore",
        "latitude": 12.9634,
        "longitude": 77.5758,
        "contact": "08026701150",
    },

    {
        "name": "Bangalore Baptist Hospital",
        "facility_type": "medical",
        "address": "Hebbal, Bangalore",
        "latitude": 13.0352,
        "longitude": 77.5890,
        "contact": "08022024700",
    },


    # =========================
    # BANGALORE - FIRE
    # =========================

    {
        "name": "Fire Station Koramangala",
        "facility_type": "fire",
        "address": "Koramangala, Bangalore",
        "latitude": 12.9345,
        "longitude": 77.6269,
        "contact": "101",
    },

    {
        "name": "Fire Station Indiranagar",
        "facility_type": "fire",
        "address": "Indiranagar, Bangalore",
        "latitude": 12.9784,
        "longitude": 77.6408,
        "contact": "101",
    },

    {
        "name": "Fire Station Jayanagar",
        "facility_type": "fire",
        "address": "Jayanagar, Bangalore",
        "latitude": 12.9250,
        "longitude": 77.5938,
        "contact": "101",
    },

    {
        "name": "Fire Station Rajajinagar",
        "facility_type": "fire",
        "address": "Rajajinagar, Bangalore",
        "latitude": 12.9912,
        "longitude": 77.5521,
        "contact": "101",
    },

    {
        "name": "Fire Station Yeshwanthpur",
        "facility_type": "fire",
        "address": "Yeshwanthpur, Bangalore",
        "latitude": 13.0280,
        "longitude": 77.5400,
        "contact": "101",
    },


    # =========================
    # BANGALORE - POLICE
    # =========================

    {
        "name": "Koramangala Police Station",
        "facility_type": "police",
        "address": "Koramangala, Bangalore",
        "latitude": 12.9344,
        "longitude": 77.6220,
        "contact": "100",
    },

    {
        "name": "Indiranagar Police Station",
        "facility_type": "police",
        "address": "Indiranagar, Bangalore",
        "latitude": 12.9784,
        "longitude": 77.6408,
        "contact": "100",
    },

    {
        "name": "Jayanagar Police Station",
        "facility_type": "police",
        "address": "Jayanagar, Bangalore",
        "latitude": 12.9250,
        "longitude": 77.5938,
        "contact": "100",
    },

    {
        "name": "Whitefield Police Station",
        "facility_type": "police",
        "address": "Whitefield, Bangalore",
        "latitude": 12.9698,
        "longitude": 77.7499,
        "contact": "100",
    },

    {
        "name": "Hebbal Police Station",
        "facility_type": "police",
        "address": "Hebbal, Bangalore",
        "latitude": 13.0358,
        "longitude": 77.5970,
        "contact": "100",
    },

    {
        "name": "Malleswaram Police Station",
        "facility_type": "police",
        "address": "Malleswaram, Bangalore",
        "latitude": 13.0035,
        "longitude": 77.5709,
        "contact": "100",
    },


    # =========================
    # MYSORE - MEDICAL
    # =========================

    {
        "name": "Apollo BGS Hospitals Mysore",
        "facility_type": "medical",
        "address": "Adichunchanagiri Road, Mysore",
        "latitude": 12.2958,
        "longitude": 76.6394,
        "contact": "08212422222",
    },

    {
        "name": "Columbia Asia Hospital Mysore",
        "facility_type": "medical",
        "address": "Bannur Road, Mysore",
        "latitude": 12.2858,
        "longitude": 76.6547,
        "contact": "08214200000",
    },

    {
        "name": "JSS Hospital Mysore",
        "facility_type": "medical",
        "address": "MG Road, Mysore",
        "latitude": 12.3072,
        "longitude": 76.6480,
        "contact": "08212334444",
    },

    {
        "name": "Narayana Multispeciality Hospital Mysore",
        "facility_type": "medical",
        "address": "Bannur Road, Mysore",
        "latitude": 12.2750,
        "longitude": 76.6650,
        "contact": "08214250000",
    },

    {
        "name": "K R Hospital Mysore",
        "facility_type": "medical",
        "address": "Irwin Road, Mysore",
        "latitude": 12.3052,
        "longitude": 76.6546,
        "contact": "08212425100",
    },


    # =========================
    # MYSORE - FIRE
    # =========================

    {
        "name": "Fire Station Saraswathipuram",
        "facility_type": "fire",
        "address": "Saraswathipuram, Mysore",
        "latitude": 12.3160,
        "longitude": 76.6020,
        "contact": "101",
    },

    {
        "name": "Fire Station Bannimantap",
        "facility_type": "fire",
        "address": "Bannimantap, Mysore",
        "latitude": 12.3380,
        "longitude": 76.6310,
        "contact": "101",
    },

    {
        "name": "Fire Station Kuvempunagar",
        "facility_type": "fire",
        "address": "Kuvempunagar, Mysore",
        "latitude": 12.2840,
        "longitude": 76.6230,
        "contact": "101",
    },

    {
        "name": "Fire Station Hebbal",
        "facility_type": "fire",
        "address": "Hebbal Industrial Area, Mysore",
        "latitude": 12.3510,
        "longitude": 76.6170,
        "contact": "101",
    },


    # =========================
    # MYSORE - POLICE
    # =========================

    {
        "name": "Devaraja Police Station Mysore",
        "facility_type": "police",
        "address": "Devaraja Mohalla, Mysore",
        "latitude": 12.3075,
        "longitude": 76.6548,
        "contact": "100",
    },

    {
        "name": "Vijayanagar Police Station Mysore",
        "facility_type": "police",
        "address": "Vijayanagar, Mysore",
        "latitude": 12.3300,
        "longitude": 76.6050,
        "contact": "100",
    },

    {
        "name": "Kuvempunagar Police Station Mysore",
        "facility_type": "police",
        "address": "Kuvempunagar, Mysore",
        "latitude": 12.2850,
        "longitude": 76.6240,
        "contact": "100",
    },

    {
        "name": "Nazarbad Police Station Mysore",
        "facility_type": "police",
        "address": "Nazarbad, Mysore",
        "latitude": 12.3000,
        "longitude": 76.6650,
        "contact": "100",
    },


    # =========================
    # OTHER KARNATAKA
    # =========================

    {
        "name": "Manipal Hospital Whitefield",
        "facility_type": "medical",
        "address": "Whitefield, Bangalore",
        "latitude": 12.9698,
        "longitude": 77.7499,
        "contact": "08025023333",
    },

    {
        "name": "Fortis Hospital Cunningham Road",
        "facility_type": "medical",
        "address": "Cunningham Road, Bangalore",
        "latitude": 12.9889,
        "longitude": 77.5946,
        "contact": "08066214444",
    },

    {
        "name": "Fire Station Whitefield",
        "facility_type": "fire",
        "address": "Whitefield, Bangalore",
        "latitude": 12.9698,
        "longitude": 77.7490,
        "contact": "101",
    },

    {
        "name": "Police Station Whitefield",
        "facility_type": "police",
        "address": "Whitefield, Bangalore",
        "latitude": 12.9695,
        "longitude": 77.7500,
        "contact": "100",
    },

    {
        "name": "Mangalore Government Wenlock Hospital",
        "facility_type": "medical",
        "address": "Hampankatta, Mangalore",
        "latitude": 12.8700,
        "longitude": 74.8430,
        "contact": "08242421141",
    },

    {
        "name": "Hubli KIMS Hospital",
        "facility_type": "medical",
        "address": "Vidya Nagar, Hubli",
        "latitude": 15.3647,
        "longitude": 75.1240,
        "contact": "08362260000",
    },

]


class Command(BaseCommand):

    help = "Populate SafeRoute with emergency facilities"

    def handle(self, *args, **kwargs):

        created = 0

        for data in FACILITIES:

            facility, was_created = (
                EmergencyFacility.objects.get_or_create(
                    name=data["name"],
                    defaults={
                        "facility_type": data["facility_type"],
                        "address": data["address"],
                        "latitude": data["latitude"],
                        "longitude": data["longitude"],
                        "contact": data["contact"],
                        "emergency_service": True,
                        "is_active": True,
                    }
                )
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added {created} facilities."
            )
        )