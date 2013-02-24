
from .models import Conference


def last_conferences(request):
    return {
        "last_conferences": Conference.objects.active()[:4]
    }
