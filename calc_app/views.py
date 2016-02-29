from django.shortcuts import render

# Create your views here.


def index_view(request):
    operator = '+'
    try:
        first_value = float(request.GET.get('first_value'))
        operator = request.GET.get('operator')
        second_value = float(request.GET.get('second_value'))
    except (ValueError, TypeError):
        return render(request, 'index.html', {"answer": "Please enter valid data"})

    if operator == '+':
        return_value = first_value + second_value
    elif operator == '-':
        return_value = first_value - second_value
    elif operator == '*':
        return_value = first_value * second_value
    elif operator == '/':
        return_value = first_value / second_value
    return render(request, 'index.html', {"answer": return_value})
