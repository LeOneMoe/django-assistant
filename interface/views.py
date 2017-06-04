from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def rendering(request):

    return render(request, 'index.html')