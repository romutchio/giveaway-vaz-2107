from app.models import Slot
from django.http import JsonResponse
from django.template.loader import get_template
from django.http import HttpResponse
from django.conf import settings


def get_active_slots(request):
    slots = [{'id': x.id, 'is_free': x.is_free} for x in Slot.objects.all().order_by('id')]
    return JsonResponse(slots, safe=False)


def get_index_page(request):
    template = get_template('index.html')
    return HttpResponse(template.render({'FRONT_URL': settings.FRONT_URL}, request))
