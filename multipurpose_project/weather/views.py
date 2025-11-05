from django.shortcuts import render
def weather_view(request):
    data = {'city': 'vaniyambadi', 'temp': '25°C', 'condition': 'Sunny'}
    return render(request, 'weather.html', data)
