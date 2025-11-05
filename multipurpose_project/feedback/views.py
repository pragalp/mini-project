from django.shortcuts import render

# Create your views here.

def feedback_view(request):
    message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        feedback = request.POST.get('feedback')
        message = f"Thank you, {name}! Your feedback is {feedback}"
    return render(request, 'feedback.html', {'message': message})
