from django.utils import timezone


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


def is_visit_long(visit, minutes=None):
    seconds = 60
    duration_seconds = get_duration(visit).total_seconds()
    return duration_seconds >= minutes * seconds


