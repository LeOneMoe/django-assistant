from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import asker

@csrf_exempt
def processing(request):

    user_says = request.POST["data"]

    return HttpResponse(asker.asker(user_says),
                        content_type="text/plain",
                        status=200
                        )
