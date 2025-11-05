from django.shortcuts import render

# Create your views here.
def clock_view(request):
    return render(request, 'clock.html')

