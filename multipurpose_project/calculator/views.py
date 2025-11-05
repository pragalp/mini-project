from django.shortcuts import render

# Create your views here.

def calculator_view(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            if num1==num2 :
                result=0
                return result
            result = num1 - num2 
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2 if num2 != 0 else 'Error'

    return render(request, 'calculator.html', {'result': result})
