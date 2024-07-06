from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


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


def get_duration(visit):
    if visit.leaved_at:
        leaved_at_time = timezone.localtime(visit.leaved_at)
    else:
        leaved_at_time = timezone.localtime()
    time_entered = timezone.localtime(visit.entered_at)
    duration = leaved_at_time - time_entered
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours}ч {minutes}мин'
