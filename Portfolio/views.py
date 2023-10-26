from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'template.html')


def about(request):
    return render(request, 'template.html')


def contact(request):
    return render(request, 'template.html')


def education(request):
    return render(request, 'template.html')


def work_exp(request):
    return render(request, 'template.html')


def honours(request):
    return render(request, 'template.html')


def certifications(request):
    return render(request, 'template.html')


def projects(request):
    return render(request, 'template.html')
