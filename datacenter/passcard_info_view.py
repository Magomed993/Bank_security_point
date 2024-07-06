from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.storage_information_view import get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    closed_visits = visits.filter(leaved_at__isnull=False)
    this_passcard_visits = []
    for visit in closed_visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit, 60)
        })
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


def is_visit_long(visit, minutes=60):
    duration_seconds = get_duration(visit).total_seconds()
    return duration_seconds >= minutes * 60
