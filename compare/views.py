from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize

from compare.models import WorldBorder
from compare.forms import ComparisonForm

# Create your views here.
def lookup(request):
    if request.method == "POST":
        form = ComparisonForm(request.POST)
        if form.is_valid():
            # pull country ids from POST and GET objects
            country_1_id = request.POST.get('country_1')
            country_2_id = request.POST.get('country_2')
            country_1_db = WorldBorder.objects.filter(id=country_1_id)
            country_2_db = WorldBorder.objects.filter(id=country_2_id)

            # pull country names and areas
            country_1_name = country_1_db.values_list('name', flat=True)[0]
            country_2_name = country_2_db.values_list('name', flat=True)[0]
            country_1_area = country_1_db.values_list('area', flat=True)[0]
            country_2_area = country_2_db.values_list('area', flat=True)[0]
            
            # determine large and small country, multiplier
            if country_1_area > country_2_area:
                large_country = country_1_name
                small_country = country_2_name
                multiplier = round(country_1_area / country_2_area, 1)
                large_country_geojson = serialize('geojson', country_1_db.all())
                small_country_geojson = serialize('geojson', country_2_db.all())
            else:
                large_country = country_2_name
                small_country = country_1_name
                multiplier = round(country_2_area / country_1_area, 1)
                large_country_geojson = serialize('geojson', country_2_db.all())
                small_country_geojson = serialize('geojson', country_1_db.all())
            
            # return relevant points
            # ADD COUNTRY LABELS TO GEOJSON!!!!!
            return render(
                request, 'results.html', {
                    'small_country': small_country,
                    'large_country': large_country, 
                    'multiplier': multiplier,
                    'small_country_geojson': small_country_geojson,
                    'large_country_geojson': large_country_geojson,
                    }
                )
        else:
            return render(request, 'error.html', {'form': form})
    else:
        form = ComparisonForm()
        return render(
            request, 'lookup.html', {'form': form}
        )