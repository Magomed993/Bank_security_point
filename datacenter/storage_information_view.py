from datacenter.models import Visit
from django.shortcuts import render
from datacenter.visit_time_scripts import get_duration, format_duration


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in active_visits:
        passcard = visit.passcard
        non_closed_visits.append({
            'who_entered': passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
