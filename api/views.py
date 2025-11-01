from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DistrictPerformance
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

@api_view(['GET'])
def fetch_and_store(request):
    try:
        res = requests.get(API_URL, timeout=10)
        res.raise_for_status()
        data = res.json()
        if not isinstance(data, list):
            return Response({"error": "Invalid API response"}, status=400)

        saved = 0
        for r in data:
            district = r.get("address", {}).get("city", "Unknown City")
            year = "2025"
            month = "October"
            person_days = r.get("id", 0)
            expenditure = r.get("company", {}).get("name", "")

            DistrictPerformance.objects.update_or_create(
                district=district,
                report_year=year,
                report_month=month,
                defaults={"person_days": person_days, "expenditure": expenditure}
            )
            saved += 1

        return Response({"message": f"✅ Synced {saved} records successfully!"})

    except Exception as e:
        return Response({"error": str(e)})


@api_view(['GET'])
def get_districts(request):
    districts = DistrictPerformance.objects.values_list('district', flat=True).distinct()
    formatted = [{"district_code": d, "name": d} for d in districts]
    return Response(formatted)


@api_view(['GET'])
def get_by_district(request, district_name):
    qs = DistrictPerformance.objects.filter(district__iexact=district_name)
    if not qs.exists():
        return Response({"message": f"No data found for {district_name}"})

    data = [
        {
            "year": d.report_year,
            "month": d.report_month,
            "total_people": d.person_days,
            "amount_spent": d.expenditure
        }
        for d in qs
    ]
    return Response({"district": district_name, "data": data})


@api_view(['POST'])
def add_record(request):
    """
    Add a new record manually
    """
    try:
        data = request.data
        rec = DistrictPerformance.objects.create(
            district=data.get("district"),
            report_year=data.get("report_year"),
            report_month=data.get("report_month"),
            person_days=data.get("person_days"),
            expenditure=data.get("expenditure")
        )
        return Response({"message": "✅ Record inserted successfully!", "id": rec.id})
    except Exception as e:
        return Response({"error": str(e)}, status=400)